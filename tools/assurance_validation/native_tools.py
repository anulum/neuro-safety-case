# SPDX-License-Identifier: AGPL-3.0-or-later
# Commercial license available
# © Concepts 1996–2026 Miroslav Šotek. All rights reserved.
# © Code 2020–2026 Miroslav Šotek. All rights reserved.
# ORCID: 0009-0009-3560-0851
# Contact: www.anulum.li | protoscience@anulum.li
# NEURO-SAFETY-CASE — exact native validation tool identities

"""Bind actual native executables and bootstrap commands to reviewed release bytes."""

import hashlib
import stat
from pathlib import Path
from typing import cast

from assurance_validation.inputs import read_file, read_json
from assurance_validation.report import Finding, Refusal

MAKEFILE_SHA256 = "05d2a4dc3965d1a06a6aba60520c8e6db9d8af4ac3698c9501dab51d4319a681"
PROVENANCE_SHA256 = "c642d79e9aa9d85c7a47969b92a8ae08e820e235c798655a46c434771c2df080"


def verify_native_tools(root: Path) -> list[Finding]:
    """Verify exact native payloads and the explicit reproducible bootstrap recipe.

    Parameters
    ----------
    root : Path
        Repository owning its native cache, source pins and Makefile.

    Returns
    -------
    list[Finding]
        Actual source, payload or setup drift; no installation or network fallback.
    """
    findings: list[Finding] = []
    try:
        provenance, raw = read_json(root, "native-tool-provenance.json")
        if hashlib.sha256(raw).hexdigest() != PROVENANCE_SHA256:
            raise Refusal(
                Finding(
                    "native.provenance",
                    "native-tool-provenance.json",
                    "Native tool sources differ from reviewed release identities.",
                    4,
                )
            )
        recipe = read_file(root, "Makefile").decode("utf-8", errors="strict")
        # The independently bound exact source record establishes every field type.
        records = cast(list[dict[str, str]], provenance["tools"])
        for record in records:
            relative = record["local_path"]
            path = root / relative
            try:
                if path.is_symlink() or not stat.S_ISREG(path.stat().st_mode):
                    raise Refusal(
                        Finding(
                            "native.file",
                            relative,
                            "Native tool must be a regular owned executable.",
                        )
                    )
                with path.open("rb") as stream:
                    digest = hashlib.file_digest(stream, "sha256").hexdigest()
                if digest != record["binary_sha256"]:
                    findings.append(
                        Finding(
                            "native.identity",
                            relative,
                            "Native executable differs from the verified release payload.",
                        )
                    )
                if hashlib.sha256(recipe.encode()).hexdigest() != MAKEFILE_SHA256:
                    findings.append(
                        Finding(
                            "native.bootstrap",
                            "Makefile",
                            "Native bootstrap differs from exact verified source and payload pins.",
                        )
                    )
            except Refusal as exc:
                findings.append(exc.finding)
            except OSError:
                findings.append(
                    Finding(
                        "native.unavailable",
                        relative,
                        "Required native executable is unavailable.",
                        3,
                    )
                )
    except Refusal as exc:
        findings.append(exc.finding)
    except UnicodeError:
        findings.append(
            Finding("native.recipe", "Makefile", "Native bootstrap must be valid UTF-8.")
        )
    return findings

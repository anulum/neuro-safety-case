<!--
SPDX-License-Identifier: AGPL-3.0-or-later
Commercial license available
© Concepts 1996–2026 Miroslav Šotek. All rights reserved.
© Code 2020–2026 Miroslav Šotek. All rights reserved.
ORCID: 0009-0009-3560-0851
Contact: www.anulum.li | protoscience@anulum.li
NEURO-SAFETY-CASE — repository governance and provenance
-->

# Validation tooling API

The metadata command accepts `--root` and `--json`. The inventory command additionally accepts `--mode generate|verify` and requires `--output` only for generation. All commands emit safe structured JSON. Exits are 0 for the requested scope, 2 for refusal, 3 for unavailable required inputs or tools, and 4 for invalid invocation or configuration.

Metadata validation accepts no generated inventory dependency. Inventory generation publishes deterministic new bytes; verification requires the canonical inventory and complete initial paths. A successful operation does not qualify argument relevance, human review or assurance conclusions or establish release readiness.

## Metadata acceptance

::: assurance_validation.metadata.validate_metadata

## Finite input

::: assurance_validation.inputs.read_file

::: assurance_validation.inputs.read_json

## Capability inventory

::: assurance_validation.capabilities.inventory_bytes

::: assurance_validation.capabilities.create_inventory

::: assurance_validation.capabilities.validate_capabilities

## Diagnostics

::: assurance_validation.report.Finding

::: assurance_validation.report.Report

## Command interfaces

::: assurance_validation.cli.metadata_main

::: assurance_validation.cli.inventory_main

## Source ownership and maintained tree

::: assurance_validation.provenance.validate_notice

::: assurance_validation.provenance.validate_provenance

::: assurance_validation.structure.maintained_paths

::: assurance_validation.structure.validate_structure

## YAML and workflow policy

::: assurance_validation.yaml_input.read_yaml

::: assurance_validation.workflows.validate_workflows

## Complete dependency observations

Release candidates and observed installed metadata are separate records. The hash lock covers the entire selected development graph. Exact source-builder constraints also use that lock. Recorded installation RECORD hashes are observations; relocated entry-script paths prevent treating them as universal build identities. Custom licence references retain exact source terms and do not infer permissions.

::: assurance_validation.dependency_lock.parse_direct

::: assurance_validation.dependency_lock.parse_lock

::: assurance_validation.dependency_records.Artifact

::: assurance_validation.dependency_records.LicenseEvidence

::: assurance_validation.dependency_records.LicenseSource

::: assurance_validation.dependency_records.PackageRecord

::: assurance_validation.dependency_records.read_provenance

::: assurance_validation.dependencies.verify_records

::: assurance_validation.dependencies.verify_installed

::: assurance_validation.dependencies.verify_configuration

::: assurance_validation.dependencies.validate_dependencies

::: assurance_validation.native_tools.verify_native_tools

## Actual documentation rendering

::: assurance_validation.documentation.References

::: assurance_validation.documentation.render_markdown

::: assurance_validation.documentation.inspect_markdown

::: assurance_validation.documentation.build_site

::: assurance_validation.documentation.inspect_projection

::: assurance_validation.documentation.validate_documentation

## Tool completion and scoped preflight

Every tool uses a fixed absolute executable, literal arguments and a finite deadline. Actual exits survive communication errors where observed. Output limits apply to accepted completed output; the caller reserves process memory separately. A named preflight subset reports its narrower scope. The complete operation requires the entire compiled profile. Missing tools, invalid protocol and native failures retain their real states.

::: assurance_validation.execution.ToolResult

::: assurance_validation.execution.run_tool

::: assurance_validation.preflight.Check

::: assurance_validation.preflight.Outcome

::: assurance_validation.preflight.PreflightReport

::: assurance_validation.preflight.validate_checker_report

::: assurance_validation.preflight.run_check

::: assurance_validation.preflight.run_checks

::: assurance_validation.preflight.source_payload

::: assurance_validation.validation_profile.scaffold_checks

::: assurance_validation.preflight_cli.preflight_main

## Shared command and protocol interfaces

::: assurance_validation.inputs.parse_json

::: assurance_validation.report.Refusal

::: assurance_validation.cli.Parser

::: assurance_validation.cli.check_main

::: assurance_validation.cli.emit_report

::: assurance_validation.ci_dependencies.verify_ci_dependencies

## Native workflow composition

The coordinator executes the eight complete native jobs from the maintained workflow sources. Each of four category gates requires every actual descendant result, and the stable required gate checks all four category results. The workflow policy verifies exact job equality with each source and rejects missing descendants, masked outcomes, altered commands and workflow calls. This preserves all category checks without depending on an unsupported reusable-workflow syntax. Both native syntax and unchanged pedantic workflow checks inspect the actual executable configuration; no projected input or suppressed finding is used.

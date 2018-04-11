#!/usr/bin/env bash
curl -X POST \
  https://xq7fhrn5t4.execute-api.us-east-1.amazonaws.com/dev/generate \
  -H 'Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: f328d526-7bb3-c158-3760-10ffec23fee4' \
  -o Custom_template_spreadsheet_userFriendlyHeaders.xlsx \
  -d '{
  "schema_base_uri": "https://schema.humancellatlas.org/",
  "schema_types": [
    "type/project/5.1.0/project",
    "type/biomaterial/5.1.0/donor_organism",
    "type/biomaterial/5.1.0/specimen_from_organism",
    "type/biomaterial/5.1.0/organoid",
    "type/process/biomaterial_collection/5.1.0/dissociation_process",
    "type/process/sequencing/5.1.0/library_preparation_process",
    "type/process/sequencing/5.1.0/sequencing_process",
    "type/file/5.1.0/sequence_file",
    "type/protocol/5.1.0/protocol"
  ],
  "schema_modules": [
    "module/project/5.1.0/contact",
    "module/biomaterial/5.1.0/cell_morphology",
    "module/biomaterial/5.1.0/homo_sapiens_specific",
    "module/biomaterial/5.1.0/medical_history",
    "module/process/sequencing/5.1.0/barcode",
    "module/process/sequencing/5.1.0/smartseq2"
  ],
  "output_filename": "Custom_template_spreadsheet_userFriendlyHeaders.xlsx"
}'
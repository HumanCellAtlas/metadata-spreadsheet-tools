# Metadata Spreadsheet Tools
Tools for generating metadata spreadsheets

## Commands


Execute
```
serverless invoke local --function generate --path ./example/generate.json
```

Deploy
```
serverless deploy -v
```

Check logs
```
serverless logs --function generate
```

## Curl Command

```
curl -X POST \
  https://xq7fhrn5t4.execute-api.us-east-1.amazonaws.com/dev/generate \
  -H 'Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: f328d526-7bb3-c158-3760-10ffec23fee4' \
  -o output.xlsx \
  -d '{
  "schema_base_uri": "https://schema.humancellatlas.org/",
  "schema_types": [
    "type/project/5.0.0/project",
    "type/biomaterial/5.0.0/donor_organism",
    "type/biomaterial/5.0.0/specimen_from_organism",
    "type/biomaterial/5.0.0/cell_suspension",
    "type/biomaterial/5.0.0/cell_line",
    "type/biomaterial/5.0.0/organoid",
    "type/process/biomaterial_collection/5.0.0/collection_process",
    "type/process/biomaterial_collection/5.0.0/dissociation_process",
    "type/process/biomaterial_collection/5.0.0/enrichment_process",
    "type/process/sequencing/5.0.0/library_preparation_process",
    "type/process/sequencing/5.0.0/sequencing_process",
    "type/protocol/5.0.0/protocol",
    "type/file/5.0.0/sequence_file"
  ],
  "schema_modules": [
	"module/project/5.0.0/contact",
	"module/project/5.0.0/publication",
	"module/biomaterial/5.0.0/cell_morphology",
	"module/biomateria/5.0.0l/death",
	"module/biomaterial/5.0.0/homo_sapiens_specific",
	"module/biomaterial/5.0.0/medical_history",
	"module/biomaterial/5.0.0/non_homo_sapiens_specific",
	"module/biomaterial/5.0.0/state_of_specimen",
	"module/biomaterial/5.0.0/familial_relationship",
	"module/process/sequencing/5.0.0/barcode",
	"module/process/sequencing/5.0.0/well"
  ],
  "output_filename": "output.xlsx"
}'
```

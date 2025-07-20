#!/bin/bash

# This script will regenerate the generated code based on a new swagger.yaml.
# It expects the swagger-codegen repo is already set up, and will initialize a python venv
# environment to run a script to replace the changelog in the summary file (api-changes.md).

# path to swagger-codegen (https://github.com/swagger-api/swagger-codegen/tree/3.0.0)
swaggerCodegenPath=./swagger-codegen

# path to the new swagger specification file in the ReCodEx api repository
# CHANGE THIS IN CASE THE PATH TO RECODEX API DIFFERS
recodexSwaggerDocsPath=../api/docs/swagger.yaml

# path to the generated code
generatedPath=./src/recodex_cli_lib/generated

# path to the old swagger
oldSwaggerDocsPath=./src/recodex_cli_lib/generated/swagger.yaml

if ! test -d ./venv; then
   echo "Initializing Python venv"
   python3.11 -m venv venv
   ./venv/bin/pip install -r requirements.txt
fi

echo "Updating API change summary"
./venv/bin/activate
python3 src/swaggerDiffchecker.py $oldSwaggerDocsPath $recodexSwaggerDocsPath

echo "Removing old generated code"
rm -r $generatedPath

echo "Generating new client code"
java -jar "$swaggerCodegenPath/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar" generate \
   -i $recodexSwaggerDocsPath \
   -l python \
   -o $generatedPath

# copy the swagger spec
cp $recodexSwaggerDocsPath "$generatedPath/swagger.yaml"

# make import adjustments in the generated code
# the raw generated code expects to be used as a top-level package using absolute import,
# but that is not the case here, the absolute imports need to be converted to relative ones by
# adding a correct number of dots before them (based on directory depth)
sed -i 's/\bswagger_client\b/..swagger_client/g' src/recodex_cli_lib/generated/swagger_client/__init__.py
sed -i 's/import swagger_client\.models/from swagger_client import models/g' src/recodex_cli_lib/generated/swagger_client/api_client.py
sed -i 's/\bswagger_client\.models\b/models/g' src/recodex_cli_lib/generated/swagger_client/api_client.py
sed -i 's/\bswagger_client\b/..swagger_client/g' src/recodex_cli_lib/generated/swagger_client/api_client.py
sed -i 's/\bswagger_client\b/...swagger_client/g' src/recodex_cli_lib/generated/swagger_client/api/__init__.py
sed -i 's/\bswagger_client\b/...swagger_client/g' src/recodex_cli_lib/generated/swagger_client/api/default_api.py
sed -i 's/\bswagger_client\b/...swagger_client/g' src/recodex_cli_lib/generated/swagger_client/models/__init__.py

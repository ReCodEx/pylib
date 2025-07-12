#!/bin/bash

# This script is intended for the initial setup of the repository.
# It will clone the swagger-codegen repository, install it, generate code, and use
# the swagger.yaml file used for testing (no other swagger is available).
# For regenerating the code from new swagger.yaml files, use the replaceGenerated.sh script instead.

# path to swagger-codegen (https://github.com/swagger-api/swagger-codegen/tree/3.0.0)
swaggerCodegenPath=./swagger-codegen

# path to the target swagger specification file
recodexSwaggerDocsPath=./tests/swagger.yaml

# generated code output path
generatedPath=./src/recodex_cli_lib/generated

# donwload swagger-codegen
git clone https://github.com/swagger-api/swagger-codegen.git
cd $swaggerCodegenPath
# checkout a stable commit
git checkout fd6f4216b

echo "Installing swagger-codegen"
mvn clean package > /dev/null
cd ..

echo "Generating new client code"
java -jar "$swaggerCodegenPath/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar" generate \
   -i $recodexSwaggerDocsPath \
   -l python \
   -o $generatedPath \
   > /dev/null

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

# set up venv
if ! test -d ./venv; then
  echo "Initializing Python venv"
  python3.11 -m venv venv
  ./venv/bin/pip install -r requirements.txt
  ./venv/bin/pip install -e .
fi
#!/bin/bash

# This script will re-generate the generated code based on a new swagger.yaml.
# Changes in the API are listed in the api-changes.md (diff) file.
# If a local venv is set up, it will use its Python, otherwise it expects a global Python 3.
# Java is required to run the swagger codegen tool.

# switch to the repository root
cd `dirname "$0"`/..

# path to the target swagger specification file
SWAGGER_YAML_FILE=./swagger.yaml
OLD_SWAGGER_YAML_FILE=./src/recodex/generated/swagger.yaml

# download the new swagger specification
if [ -f "$SWAGGER_YAML_FILE" ]; then
  rm "$SWAGGER_YAML_FILE"
fi
wget 'https://raw.githubusercontent.com/ReCodEx/api/refs/heads/master/docs/swagger.yaml' -O "$SWAGGER_YAML_FILE"

# use the local venv if available
if [ -d "./venv" ]; then
	echo "Using internal Python venv"
	./venv/bin/pip install -r requirements.txt
	./venv/bin/activate
fi

# make the diff
python3 ./bin/swagger-diffchecker.py $OLD_SWAGGER_YAML_FILE $SWAGGER_YAML_FILE ./api-changes.md

# generate the new code
. ./bin/.generate-swagger.sh

#!/bin/bash

# This script is intended for the initial setup of the repository.
# It will download the current swagger specification from the ReCodEx api repository
# and generate the client code based on it.
# Java is required to run the swagger codegen tool.

# switch to the repository root
cd `dirname "$0"`/..

# path to the target swagger specification file
SWAGGER_YAML_FILE=./swagger.yaml
if [ -f "$SWAGGER_YAML_FILE" ]; then
  rm "$SWAGGER_YAML_FILE"
fi
wget 'https://raw.githubusercontent.com/ReCodEx/api/refs/heads/master/docs/swagger.yaml' -O "$SWAGGER_YAML_FILE"

. ./bin/.generate-swagger.sh

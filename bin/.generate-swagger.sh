# Shared script that generates the client code from the swagger specification.
# It expects Java to be installed to run the swagger-codegen tool.

SWAGGER_YAML_FILE=./swagger.yaml
if [ ! -f "$SWAGGER_YAML_FILE" ]; then
	echo "Missing ${SWAGGER_YAML_FILE}!"
	exit 1
fi

# ensure we have the codegen jar (up to date)
SWAGGER_JAR_FILE=./bin/swagger-codegen-cli.jar
if [ -f "$SWAGGER_JAR_FILE" ]; then
	rm "$SWAGGER_JAR_FILE"
fi
wget 'https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.72/swagger-codegen-cli-3.0.72.jar' -O "$SWAGGER_JAR_FILE"

# generated code output path
GENERATED_PATH=./src/recodex/generated
if [ -d "$GENERATED_PATH" ]; then
	# remove old code if exists
	rm -r "$GENERATED_PATH"
fi

echo "Generating new client code"
java -jar "$SWAGGER_JAR_FILE" generate \
	-i "$SWAGGER_YAML_FILE" \
	-l python \
	-o "$GENERATED_PATH"

# copy the swagger spec
cp "$SWAGGER_YAML_FILE" "$GENERATED_PATH/swagger.yaml"

# make import adjustments in the generated code
# the raw generated code expects to be used as a top-level package using absolute import,
# but that is not the case here, the absolute imports need to be converted to relative ones by
# adding a correct number of dots before them (based on directory depth)
sed -i 's/\bswagger_client\b/..swagger_client/g' "$GENERATED_PATH/swagger_client/__init__.py"
sed -i 's/import swagger_client\.models/from swagger_client import models/g' "$GENERATED_PATH/swagger_client/api_client.py"
sed -i 's/\bswagger_client\.models\b/models/g' "$GENERATED_PATH/swagger_client/api_client.py"
sed -i 's/\bswagger_client\b/..swagger_client/g' "$GENERATED_PATH/swagger_client/api_client.py"
sed -i 's/\bswagger_client\b/...swagger_client/g' "$GENERATED_PATH/swagger_client/api/__init__.py"
sed -i 's/\bswagger_client\b/...swagger_client/g' "$GENERATED_PATH/swagger_client/api/default_api.py"
sed -i 's/\bswagger_client\b/...swagger_client/g' "$GENERATED_PATH/swagger_client/models/__init__.py"

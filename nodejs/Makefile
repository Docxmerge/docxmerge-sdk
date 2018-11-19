NPM_REGISTRY=https://registry.npmjs.org/
# SWAGGER_URL=https://api.docxmerge.com/api/swagger/v1/swagger.json
SWAGGER_URL=http://localhost:5030/api/swagger/v1/swagger.json
update_api:
	docker run --rm --network=host -v ${PWD}/src/swagger:/local openapitools/openapi-generator-cli generate -i ${SWAGGER_URL} -l typescript-node -o /local --additional-properties supportsES6=true
	sudo chmod 777 -R ./src/swagger

build: update_api
	yarn
	yarn build

publish: build
	tsc -p ./tsconfig.json && npm publish --registry ${NPM_REGISTRY}
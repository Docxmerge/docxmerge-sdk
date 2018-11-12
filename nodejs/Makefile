NPM_REGISTRY=https://registry.npmjs.org/

build: update_api
	yarn
	yarn build

update_api:
	docker run --rm --network=host -v ${PWD}/src/swagger:/local swaggerapi/swagger-codegen-cli:v2.3.1 generate -i http://localhost:5030/api/swagger/v1/swagger.json -l typescript-node -o /local --additional-properties supportsES6=true
	# docker run --rm -v ${PWD}/src/swagger:/local swaggerapi/swagger-codegen-cli:v2.3.1 generate -i https://api.docxmerge.com/api/swagger/v1/swagger.json -l typescript-node -o /local
	sudo chmod 777 ./src/swagger

publish_local: build
	tsc -p ./tsconfig.json && npm publish --registry ${NPM_REGISTRY}
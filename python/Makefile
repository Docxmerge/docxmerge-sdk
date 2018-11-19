SWAGGER_URL=https://api.docxmerge.com/api/swagger/v1/swagger.json

update_api:
	docker run --rm --network=host -v ${PWD}/docxmerge_sdk/swagger_client:/local/docxmerge_replace_me openapitools/openapi-generator-cli generate -i ${SWAGGER_URL} -l python -o /local --additional-properties packageName=docxmerge_replace_me
	sudo chmod 777 -R ${PWD}/docxmerge/swagger_client
	# https://github.com/swagger-api/swagger-codegen/issues/8351
	find ${PWD}/docxmerge_sdk/swagger_client -name "*.py" -exec sed -i 's/docxmerge_replace_me/docxmerge_sdk\.swagger_client/' {} +

build:
	python setup.py sdist bdist_wheel

clean:
	rm -rf build
	rm -rf dist

publish_test: clean build
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

publish_prod: clean build
	twine upload dist/*
update_api:
	curl http://localhost:5101/swagger/v1/swagger.json -o v1-docxmerge.json
	./gradlew generateSwaggerCode
publish:
	./gradlew uploadArchives
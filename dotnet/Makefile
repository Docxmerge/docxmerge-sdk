include .env
export
VERSION := $(shell cat ./Docxmerge/Docxmerge.csproj | grep -oPm1 "(?<=<Version>)[^<]+")
publish_nuget:
	
	dotnet pack
	dotnet nuget push ./Docxmerge/bin/Debug/Docxmerge.${VERSION}.nupkg -k ${NUGET_API_KEY} -s https://api.nuget.org/v3/index.json

update_api:
	docker run --rm --network=host -v ${PWD}/Docxmerge/swagger:/local/src/main/CsharpDotNet2 swaggerapi/swagger-codegen-cli:v2.3.1 generate -i https://api.docxmerge.com/api/swagger/v1/swagger.json -l csharp-dotnet2 -o /local
	sudo chmod 777 -R ${PWD}/Docxmerge/swagger

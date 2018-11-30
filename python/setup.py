import setuptools

setuptools.setup(
    name="docxmerge_sdk",
    version="0.0.7",
    author="David viejo pomata",
    author_email="davidviejopomata@gmail.com",
    description="Sdk for docxmerge",
    url="https://github.com/Docxmerge/docxmerge-sdk",
    packages=['docxmerge_sdk', 'docxmerge_sdk.swagger_client', 'docxmerge_sdk.swagger_client.api',
              'docxmerge_sdk.swagger_client.models'],
    package_dir={
        'docxmerge_sdk': 'docxmerge_sdk',
        'docxmerge_sdk/swagger_client': 'docxmerge_sdk.swagger_client',
        'docxmerge_sdk/swagger_client/api': 'docxmerge_sdk.swagger_client.api',
        'docxmerge_sdk/swagger_client/models': 'docxmerge_sdk.swagger_client.models',
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'aiohttp==3.4.4',
        'async-timeout==3.0.1',
        'attrs==18.2.0',
        'bleach==3.0.2',
        'certifi==2018.10.15',
        'chardet==3.0.4',
        'docutils==0.14',
        'idna==2.7',
        'idna-ssl==1.1.0',
        'multidict==4.4.2',
        'pkginfo==1.4.2',
        'pprint==0.1',
        'Pygments==2.2.0',
        'python-dateutil==2.7.5',
        'readme-renderer==24.0',
        'requests==2.20.1',
        'requests-toolbelt==0.8.0',
        'six==1.11.0',
        'tqdm==4.28.1',
        'twine==1.12.1',
        'urllib3==1.24.1',
        'webencodings==0.5.1',
        'yarl==1.2.6',
    ],

)

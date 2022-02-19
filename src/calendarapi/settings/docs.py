SPECTACULAR_SETTINGS = {
    'TITLE': 'Calendar API',
    'DESCRIPTION': 'Авторизация через Authorize -> `<jwt access token>`',
    'VERSION': 'v1',
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "persistAuthorization": True,
        "displayOperationId": False,
        "operationsSorter": 'alpha',
        'tagsSorter': 'alpha',
        'filter': True
    },
    'SCHEMA_PATH_PREFIX': r'/api/v[0-9]+',
    # 'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
    # 'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    # 'REDOC_DIST': 'SIDECAR',
}


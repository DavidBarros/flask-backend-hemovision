class Config:
    MONGO_URI = "mongodb://localhost:27017/hemovision-db"
    JWT_SECRET_KEY = "5514823929849782381218388725824384277"
    JWT_ACCESS_TOKEN_EXPIRES = 7200

    API_TITLE = "Hemovision API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    PROPAGATE_EXCEPTIONS = True

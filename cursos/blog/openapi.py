from fastapi.openapi.utils import get_openapi
from settings import Settings


class CustomOpenApi:
    def __init__(self, app):
        self.app = app

    def custom_openapi(self):
        # Load .env file
        settings = Settings()

        if self.app.openapi_schema:
            return self.app.openapi_schema

        title = settings.TITLE
        version = settings.VERSION
        summary = settings.SUMMARY
        description = settings.DESCRIPTION

        openapi_schema = get_openapi(
            title=title,
            version=version,
            summary=summary,
            description=description,
            routes=self.app.routes,
        )
        openapi_schema["info"]["x-logo"] = {
            "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
        }
        self.app.openapi_schema = openapi_schema
        return self.app.openapi_schema
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from controllers import api_router
from errors import validation

app = FastAPI()
app.include_router(api_router, prefix="/api")
app.add_exception_handler(
    RequestValidationError, validation.validation_exception_handler
)

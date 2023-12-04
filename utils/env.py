import databases
from starlette.config import Config

config = Config(".env")

[DB_CONNECTION] = (config("DB_CONNECTION", cast=databases.DatabaseURL),)

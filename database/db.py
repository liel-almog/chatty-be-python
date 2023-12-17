from typing import Annotated
from databases import Database
from fastapi import Depends
from utils import env


async def get_db():
    database = Database(env.DB_CONNECTION)
    await database.connect()
    return database


CommonDB = Annotated[Database, Depends(get_db, use_cache=True)]

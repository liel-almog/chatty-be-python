from databases import Database
from utils import env

async def get_db():
    database = Database(env.DB_CONNECTION)
    await database.connect()

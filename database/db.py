from databases import Database
from utils import env

async def get_db():
    print("Connecting to database...")
    database = Database(env.DB_CONNECTION)
    await database.connect()
    return database

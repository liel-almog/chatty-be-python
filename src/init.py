import psycopg2
import utils.env 
from dotenv import load_dotenv

load_dotenv()

DB_CONNECTION = utils.env.get_env("DB_CONNECTION")
conn = psycopg2.connect(DB_CONNECTION)
cur = conn.cursor()


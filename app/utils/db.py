from databases import Database

from utils import consts


async def connect_db():
    db = Database(
        f"postgresql://{consts.DB_NAME}:{consts.DB_PASSWORD}"
        f"@{consts.DB_HOST}:{consts.DB_PORT}/{consts.DB_NAME}"
    )
    await db.connect()
    return db


async def disconnect_db(db: Database):
    await db.disconnect()


async def execute(query, values, is_many):
    pass

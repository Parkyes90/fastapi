import sqlalchemy
from utils.consts import DB_URL

metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DB_URL)
metadata.create_all(engine)

authors = sqlalchemy.Table(
    "authors",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.Text),
    sqlalchemy.Column("books", sqlalchemy.ARRAY(sqlalchemy.Text)),
)

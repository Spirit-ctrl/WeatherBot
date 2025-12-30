from sqlalchemy.ext.asyncio import create_async_engine

from sqlalchemy.ext.asyncio import async_sessionmaker,  AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


from settings import get_db_url

DATABASE_URL = get_db_url()

engine = create_async_engine(DATABASE_URL, echo=True)
Session = async_sessionmaker(engine, expire_on_commit=False)

class Base(AsyncAttrs, DeclarativeBase):
    pass


async def get_db():
    async with Session() as db:
        yield db

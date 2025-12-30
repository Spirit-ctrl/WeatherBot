from routers.start import models
from bd import get_db
from sqlalchemy import select


async def get_city(user_tg_id) -> str:
    async for db in get_db():
        result = await db.execute(
            select(models.User).where(models.User.telegram_id == user_tg_id)
        )
        user = result.scalars().first()
        if user and user.city:
            return user.city
        return ""

async def change_city(user_tg_id: int, new_city: str) -> None:
    async for db in get_db():
        result = await db.execute(
            select(models.User).where(models.User.telegram_id == user_tg_id)
        )
        user = result.scalars().first()
        if user:
            user.city = new_city
            db.add(user)
            await db.commit()
            return
        else:
            new_user = models.User(telegram_id=user_tg_id, city=new_city)
            db.add(new_user)
            await db.commit()
            return
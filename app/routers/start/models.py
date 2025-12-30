from bd import Base
from sqlalchemy import Column, Integer, String



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True, nullable=False)
    city = Column(String, nullable=True)

    def __repr__(self) -> str:
        return f"<User id={self.id} telegram_id={self.telegram_id} city={self.city}>"
    

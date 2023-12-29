from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Prompts(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    
class Socials(Base):
    __tablename__ = "socials"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    post = Column(String)
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:1234@localhost:5432/Troyki_db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()


class GodSlaveModel(Base):
    __tablename__ = "godSlave"
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String)
    password = Column(String)
    position = Column(String)
    fullname = Column(String)
    photo_URL = Column(String)
    ifTrockist = Column(Boolean)


class TroykaModel(Base):
    __tablename__ = "troyka"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    gebist_id = Column(Integer, ForeignKey("godSlave.id"))
    commy_id = Column(Integer, ForeignKey("godSlave.id"))
    prokuror_id = Column(Integer, ForeignKey("godSlave.id"))


class SentenceModel(Base):
    __tablename__ = "sentence"
    id = Column(Integer, primary_key=True, index=True)
    troyka_id = Column(Integer, ForeignKey("troyka.id"))
    description = Column(String)
    ifExecution = Column(Boolean)


class PolitburoModel(Base):
    __tablename__ = "politburo"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)


Base.metadata.create_all(bind=engine)

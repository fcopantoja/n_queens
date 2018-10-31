import os

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.environ.get('DATABASE_URL', 'postgresql://localhost:5432/nqueens'), echo=False)
Base = declarative_base()


class Solution(Base):
    __tablename__ = 'solutions'
    id = Column(Integer, primary_key=True)
    positions = Column(String)
    number_of_queens = Column(Integer)

    def __repr__(self):
        return "<Solution(positions='%s', number_of_queens='%s'>" % (self.positions, self.number_of_queens)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

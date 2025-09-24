from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Author(Base):
    __tablename__= "authors"
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String(100),nullable=False)

    books = relationship("Book", back_populates="author",cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Author(id={self.id},name={self.name!r})>"

class Book(Base):
    __tablename = "book"
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String(200),nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id", ondelete="CASCADE"))

    author = relationship("Author",back_populates="books")

    
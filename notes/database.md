SQLAlchemy is a Python ORM (Object Relational Mapper).
Instead of writing raw SQL, you define models (classes) and SQLAlchemy translates them into SQL queries for 
PostgreSQL.

Database connection string: "postgresql://<username>:<password>@<host>:<port>/<database>"
DATABASE_URL="postgresql://postgres:password@localhost:5432/mydatabase"
This string is how your Python app tells SQLAlchemy where PostgreSQL lives.

Engine = the core connection to PostgreSQL.
It doesn’t open a DB connection immediately, but it knows how to connect.
When you call create_engine(), SQLAlchemy prepares the PostgreSQL driver (psycopg2 ).

Session = the actual “conversation” with the DB.
sessionmaker() → creates a factory that generates new sessions whenever you need one.
Params:
autocommit=False → you must call session.commit() manually.
autoflush=False → changes are not auto-pushed until you commit/flush.
bind=engine → this session will use the PostgreSQL engine defined above.
When you use SessionLocal(), it actually opens a TCP connection to PostgreSQL at localhost:5432.

Base = declarative_base()
Base class for ORM models.
When you define a table as a Python class, it must inherit from Base. 
Later, Base.metadata.create_all(bind=engine) will create all tables in PostgreSQL

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
This is a session dependency function.
It opens a database session (db = SessionLocal()).
yield db → gives the session to the code that needs it.
Each request gets its own session, reused throughout the request.
The get_db() function + dependency injection ensures sessions are created and cleaned up automatically.
This avoids messy manual session handling and prevents connection leaks.

SQL shell/psql

pg admin

psycopg2




from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

db_user = 'postgres'
db_port = 5432
db_host = 'localhost'
db_password = 'admin'
db_name = 'penjat_ac11'

uri = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

engine = create_engine(uri)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_PATH = "rpg_tool.db"
engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)
SessionLocal = sessionmaker(bind=engine)
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./learningTest.db")

# Detectar si es PostgreSQL para ajustar connect_args
if DATABASE_URL.startswith("postgresql"):
    engine = create_engine(DATABASE_URL)
else:
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Palabra(Base):
    __tablename__ = "palabras"
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, index=True)
    ingles = Column(String, unique=True, index=True)
    espanol = Column(String, index=True)

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/palabra/")
def agregar_palabra(tipo: str, ingles: str, espanol: str):
    db = SessionLocal()
    palabra = Palabra(tipo=tipo, ingles=ingles, espanol=espanol)
    db.add(palabra)
    try:
        db.commit()
        db.refresh(palabra)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Palabra ya existe o error de datos")
    finally:
        db.close()
    return palabra

@app.get("/palabra/aleatoria/")
def palabra_aleatoria():
    db = SessionLocal()
    palabras = db.query(Palabra).all()
    db.close()
    if not palabras:
        raise HTTPException(status_code=404, detail="No hay palabras registradas")
    palabra = random.choice(palabras)
    return {"tipo": palabra.tipo, "ingles": palabra.ingles, "espanol": palabra.espanol}

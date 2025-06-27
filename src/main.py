from fastapi import FastAPI


app = FastAPI()



# @app.get("/")
# def root():
#     return {"message": "Welcome to the English-Spanish Vocabulary API!"}

# @app.post("/palabras")
# def create_palabra(palabra: str):
#     return {"message": f"Palabra '{palabra}' creada exitosamente!"}

# @app.get("/palabras/{palabra_id}")
# def read_palabra(palabra_id: int):
#     return {"message": f"Detalles de la palabra con ID {palabra_id}"}
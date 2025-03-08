from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_attributes():
    return {"id": 1234, "name": "Juan", "last_name": "Rodriguez", "age": 27, "email": "juan@hotmail.com"}

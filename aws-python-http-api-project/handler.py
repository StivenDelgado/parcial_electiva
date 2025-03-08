import json


def five_atributte(event, context):
    body = {
        "id": 1,
        "name": "Yamaha",
        "color": "Red",
        "price": 1000,
        "description": "Moto de fábrica"
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def ten_atributte(event, context):
    body = {
        "id": 1,
        "name": "Stiven",   
        "lastname": "Parcial",
        "age": 25,
        "city": "Armenia",
        "country": "Colombia",
        "email": "stiven.parcial@gmail.com",
        "phone": "+57 324 281 5979",
        "address": "Calle 50 #A mnz C #9",
        "description": "Estudiante de Ingeniería Informática"
    }
    response = {"statusCode": 200, "body": json.dumps(body)}
    return response
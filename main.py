import uvicorn
from fastapi import FastAPI
from redis import Redis
from models import WriteDataModel


app = FastAPI()
redis = Redis(host='redis', port=6379)


@app.get('/check_data')
def check_data(phone: str):
    """
    Метод получения данных (адреса) из БД по номеру телефона
    :param phone: номер телефона
    :return: str адрес
    """
    if phone:
        return redis.get(phone)


@app.post('/write_data')
def write_data(input_model: WriteDataModel):
    """
    Метод записи данных (телефона и адреса) в БД
    :param input_model: модель входных данных
    :return: None
    """
    redis.set(input_model.phone, input_model.address)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

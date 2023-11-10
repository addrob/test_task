import uvicorn
from fastapi import FastAPI
from schemas import WriteDataModel
from redis import Redis
from config import REDIS_PORT, REDIS_HOST

app = FastAPI()
redis = Redis(host=REDIS_HOST,
              port=REDIS_PORT)


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

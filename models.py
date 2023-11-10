from typing import Optional

from pydantic import BaseModel


class WriteDataModel(BaseModel):
    """
    Модель входных данных для метода записи данных в БД
    """
    phone: str      # номер телефона
    address: Optional[str]      # адрес
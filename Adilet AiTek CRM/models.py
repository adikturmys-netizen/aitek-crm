from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Branch(Base):
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    city = Column(String)

    users = relationship("User", back_populates="branch")
    clients = relationship("Client", back_populates="branch")
    requests = relationship("Request", back_populates="branch")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    role = Column(String)
    branch_id = Column(Integer, ForeignKey("branches.id"))

    branch = relationship("Branch", back_populates="users")
    assigned_requests = relationship("Request", back_populates="assigned_user")

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    branch_id = Column(Integer, ForeignKey("branches.id"))

    branch = relationship("Branch", back_populates="clients")
    requests = relationship("Request", back_populates="client")

class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    branch_id = Column(Integer, ForeignKey("branches.id"))

    # Поля по образцу Google Sheets таблицы отчетности
    date = Column(String, nullable=True)             # ДАТА
    manager = Column(String, nullable=True)          # МЕНЕДЖЕР
    amount = Column(Integer, nullable=True)          # СУММА
    tv_model = Column(String, nullable=True)         # ТЕЛЕВИЗОР (диагональ/модель)
    address = Column(String, nullable=True)          # АДРЕС
    gift = Column(String, nullable=True)             # ПОДАРОК
    bank = Column(String, nullable=True)             # БАНК (например, Каспи)
    prepayment = Column(Integer, nullable=True)      # ПРЕДОПЛАТА
    delivery_type = Column(String, nullable=True)    # Способ доставки (почта, такси, indriver и т.д.)
    
    # Новые поля для логистики
    courier_contact = Column(String, nullable=True)  # Контакт доставщика
    car_number = Column(String, nullable=True)       # Госномер машины

    tv_setup_status = Column(String, default="Ожидает") # Статус настройки каналов / Кинопоиск по видеосвязи

    description = Column(String, nullable=True)      # Доп. описание
    status = Column(String, default="Новая")         # Статус (Новая, Отправлено [зеленый], Возврат [красный], В пути)

    client = relationship("Client", back_populates="requests")
    assigned_user = relationship("User", back_populates="assigned_requests")
    branch = relationship("Branch", back_populates="requests")

    @property
    def remaining_amount(self) -> int:
        return (self.amount or 0) - (self.prepayment or 0)
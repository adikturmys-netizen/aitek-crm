from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

branches = [
    {"id": 1, "name": "Главный офис", "city": "Алматы"},
    {"id": 2, "name": "Северный филиал", "city": "Астана"}
]

users = [
    {"id": 1, "name": "Адилет Бекенович", "role": "IT / Технический специалист", "branch_id": 1},
    {"id": 2, "name": "Темирлан Канатович", "role": "Начальник логистики", "branch_id": 1},
    {"id": 3, "name": "Жулдыз Батырбек", "role": "Бухгалтер", "branch_id": 1}
    ]

clients = [
    {"id": 1, "name": "Спанбетов Нурлан", "phone": "87074151154", "branch_id": 1},
    {"id": 2, "name": "Оразбай Жансай", "phone": "87770987654", "branch_id": 1}
]

requests_db = [
    {
        "id": 1,
        "client_id": 2,
        "user_id": 2,
        "branch_id": 1,
        "date": "04.09",
        "manager": "Эльмира",
        "amount": 499000,
        "tv_model": "55 дюйм",
        "address": "Алматы Наурызбай...",
        "gift": "Пылесос кр...",
        "bank": "Каспи рассрочка",
        "prepayment": 0,
        "delivery_type": "Такси",
        "courier_contact": None,
        "car_number": None,
        "tv_setup_status": "Ожидает",
        "description": "",
        "status": "Новая"
    }
]

class RequestCreate(BaseModel):
    client_id: int
    user_id: int
    branch_id: int
    date: Optional[str] = None
    manager: Optional[str] = None
    amount: Optional[int] = None
    tv_model: Optional[str] = None
    address: Optional[str] = None
    gift: Optional[str] = None
    bank: Optional[str] = None
    prepayment: Optional[int] = None
    delivery_type: Optional[str] = "Почта"
    courier_contact: Optional[str] = None
    car_number: Optional[str] = None
    tv_setup_status: Optional[str] = "Ожидает"
    description: Optional[str] = None
    status: str = "Новая"

class ClientCreate(BaseModel):
    name: str
    phone: str
    branch_id: int

@app.get("/branches/")
def get_branches():
    return branches

@app.get("/users/")
def get_users():
    return users

@app.get("/clients/")
def get_clients():
    return clients

@app.get("/requests/")
def get_requests():
    return requests_db

@app.post("/requests/")
def create_request(item: RequestCreate):
    new_id = len(requests_db) + max([r["id"] for r in requests_db], default=0) + 1
    new_req = item.dict()
    new_req["id"] = new_id
    requests_db.append(new_req)
    return new_req

@app.post("/clients/")
def create_client(item: ClientCreate):
    new_id = len(clients) + max([c["id"] for c in clients], default=0) + 1
    new_client = item.dict()
    new_client["id"] = new_id
    clients.append(new_client)
    return new_client

@app.put("/requests/{req_id}/field")
def update_request_field(req_id: int, field: str, value: Any):
    for r in requests_db:
        if r["id"] == req_id:
            r[field] = value
            return r
    raise HTTPException(status_code=404, detail="Request not found")

@app.put("/requests/{req_id}/status")
def update_status(req_id: int, status: str):
    for r in requests_db:
        if r["id"] == req_id:
            r["status"] = status
            return r
    raise HTTPException(status_code=404, detail="Request not found")

@app.delete("/requests/{req_id}")
def delete_request(req_id: int):
    global requests_db
    requests_db = [r for r in requests_db if r["id"] != req_id]
    return {"ok": True}
from typing import Optional, Union
from pydantic import BaseModel

class BranchCreate(BaseModel):
    name: str
    city: str

class BranchResponse(BranchCreate):
    id: int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    name: str
    role: str
    branch_id: int

class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True

class ClientCreate(BaseModel):
    name: str
    phone: str
    branch_id: int

class ClientResponse(ClientCreate):
    id: int

    class Config:
        from_attributes = True

class RequestCreate(BaseModel):
    client_id: int
    user_id: Union[int, str]
    branch_id: int
    date: Optional[str] = None
    manager: Optional[str] = None
    amount: Optional[int] = None
    tv_model: Optional[str] = None
    address: Optional[str] = None
    gift: Optional[str] = None
    bank: Optional[str] = None
    prepayment: Optional[int] = None
    delivery_type: Optional[str] = None
    courier_contact: Optional[str] = None
    car_number: Optional[str] = None
    tv_setup_status: Optional[str] = "Ожидает"
    description: Optional[str] = None
    status: Optional[str] = "Новая"

class RequestUpdate(BaseModel):
    client_id: Optional[int] = None
    user_id: Optional[Union[int, str]] = None
    branch_id: Optional[int] = None
    date: Optional[str] = None
    manager: Optional[str] = None
    amount: Optional[int] = None
    tv_model: Optional[str] = None
    address: Optional[str] = None
    gift: Optional[str] = None
    bank: Optional[str] = None
    prepayment: Optional[int] = None
    delivery_type: Optional[str] = None
    courier_contact: Optional[str] = None
    car_number: Optional[str] = None
    tv_setup_status: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class RequestResponse(RequestCreate):
    id: int
    remaining_amount: int = 0

    class Config:
        from_attributes = True
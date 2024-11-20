from app.domain.DTOs.base_dto import BaseDTO
from datetime import datetime


class UserDTO(BaseDTO):
  def __init__(self, userName: str = "", role: str = "", id: int = None, created_at: datetime = None):
    super().__init__(id)
    self.userName = userName
    self.role = role
    self.created_at = created_at
    

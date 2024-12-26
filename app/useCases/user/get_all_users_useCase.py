from typing import Dict, List
from flask import jsonify
from app.domain.DTOs.user_dto import UserDTO
from app.domain.mappers.user_mapper import UserMapper
from app.repository.implementations.user_repository import UserRepository


class GetAllUsersUseCase:
  def __init__(self, respository: UserRepository):
    self.user_repository: UserRepository = respository
  
  def execute(self) -> List[Dict]:
    users = self.user_repository.read_all()
    usersDto = [UserMapper().userEntityToUserDto(user) for user in users]
    
    return jsonify({"message": "Usuários obtidos com sucesso!",
                    "data": [UserMapper().convertFromDtoToJson(user) for user in usersDto]}), 200

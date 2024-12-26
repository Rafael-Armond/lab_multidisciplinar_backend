from typing import Dict
from flask import jsonify
from app.domain.DTOs.user_dto import UserDTO
from app.domain.mappers.base_mapper import BaseMapper
from app.domain.mappers.user_mapper import UserMapper
from app.repository.implementations.user_repository import UserRepository


class GetUserByIdUseCase:
  def __init__(self, respository: UserRepository):
    self.user_repository: UserRepository = respository
    self.user_mapper: BaseMapper = UserMapper()
  
  def execute(self, userId: int) -> Dict:
    userEntity = self.user_repository.read(userId)
    userDTO = UserMapper().userEntityToUserDto(userEntity)
    if userDTO:
        return jsonify({"message": "Usuário encontrado.",
                        "data": self.user_mapper.convertFromDtoToJson(userDTO)}), 200
    raise ValueError(f"User with ID {userId} not found")

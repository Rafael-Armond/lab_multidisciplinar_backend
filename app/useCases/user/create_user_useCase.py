from typing import Dict
from app.domain.DTOs.user_dto import UserDTO
from app.domain.mappers.base_mapper import BaseMapper
from app.domain.mappers.user_mapper import UserMapper
from app.domain.models.user import User
from app.repository.implementations.user_repository import UserRepository

class CreateUserUseCase:
  def __init__(self, respository: UserRepository):
    self.user_repository: UserRepository = respository
    self.user_mapper: BaseMapper = UserMapper()
  
  def execute(self, userData: Dict) -> UserDTO:
    userDto: UserDTO = self.user_mapper.convertFromJsonToDto(userData)
    userEntity: User = UserMapper().userDtoToUserEntityMapper(userDto) 
    created_user: User = self.user_repository.create(userEntity)
    
    return UserMapper().userEntityToUserDto(created_user)

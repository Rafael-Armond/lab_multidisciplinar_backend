from app.domain.DTOs.user_dto import UserDTO
from app.domain.mappers.base_mapper import BaseMapper
from app.domain.mappers.user_mapper import UserMapper
from app.repository.implementations.user_repository import UserRepository


class UpdateUserUseCase:
  def __init__(self, respository: UserRepository):
    self.user_repository: UserRepository = respository
    self.user_mapper: BaseMapper = UserMapper()
  
  def execute(self, id: int, userData: dict) -> UserDTO:
    userDto = self.user_mapper.convertFromJsonToDto(userData)
    userEntity = UserMapper().userDtoToUserEntityMapper(userDto)
    userEntity.id = id 
    updatedUser = self.user_repository.update(userEntity)
    
    return UserMapper().userEntityToUserDto(updatedUser)

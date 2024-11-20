from typing import Dict
from app.domain.DTOs.user_dto import UserDTO
from app.domain.mappers.base_mapper import BaseMapper
from app.domain.models.user import User


class UserMapper(BaseMapper[UserDTO]):
  @staticmethod
  def userDtoToUserEntityMapper(userDto: UserDTO) -> User:
    user_entity = User(
      username=userDto.userName,
      role=userDto.role,
    )
    return user_entity

  @staticmethod
  def userEntityToUserDto(userEntity: User) -> UserDTO:
    return UserDTO(id=userEntity.id,
                   userName=userEntity.username,
                   role=userEntity.role,
                   created_at=userEntity.created_at)
  
  @classmethod
  def convertFromJsonToDto(self, json: Dict) -> UserDTO:
    return UserDTO(
        userName=json.get("username"),
        role=json.get("role")
    )
    
  @classmethod
  def convertFromDtoToJson(cls, userDto: UserDTO) -> Dict:
    return {
        "id": userDto.id,
        "username": userDto.userName,
        "role": userDto.role,
        "created_at": userDto.created_at.isoformat() if userDto.created_at else None,
    }
  

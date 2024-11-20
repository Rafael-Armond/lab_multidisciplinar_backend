from app.domain.DTOs.user_dto import UserDTO
from app.domain.mappers.user_mapper import UserMapper
from app.repository.implementations.user_repository import UserRepository


class GetUserByIdUseCase:
  def __init__(self, respository: UserRepository):
    self.user_repository: UserRepository = respository
  
  def execute(self, userId: int) -> UserDTO:
    user = self.user_repository.read(userId)
    if user:
        return UserMapper().userEntityToUserDto(user)
    raise ValueError(f"User with ID {userId} not found")

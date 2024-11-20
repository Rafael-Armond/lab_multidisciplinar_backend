from app.repository.implementations.user_repository import UserRepository


class DeleteUserUseCase:
  def __init__(self, respository: UserRepository):
    self.user_repository: UserRepository = respository
  
  def execute(self, userId: int) -> bool:
    try:
        self.user_repository.delete(userId)
        return True
    except ValueError as e:
        print(f"Error deleting user: {e}")
        return False

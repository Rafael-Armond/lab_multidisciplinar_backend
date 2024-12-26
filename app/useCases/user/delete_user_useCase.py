from typing import Dict

from flask import jsonify
from app.repository.implementations.user_repository import UserRepository


class DeleteUserUseCase:
  def __init__(self, respository: UserRepository):
    self.user_repository: UserRepository = respository
  
  def execute(self, userId: int) -> Dict:
    try:
        self.user_repository.delete(userId)
        return jsonify({"message": "Usuário deletado com sucesso.", "data": True})
    except ValueError as e:
        raise Exception(f"Error deleting user: {e}")

from flask import Blueprint, request, jsonify
from app.domain.DTOs.user_dto import UserDTO
from app.domain.models.user import User
from app.repository.implementations.user_repository import UserRepository
from app.useCases.user.create_user_useCase import CreateUserUseCase
from app.useCases.user.get_all_users_useCase import GetAllUsersUseCase
from core.db import get_session

class UserRoutes:
    def __init__(self, blueprint: Blueprint):
        userRepository = UserRepository(session=get_session(), model=User)
        
        self.router = blueprint
        self.register_routes(controllerName="/users")
        self.createUserUseCase = CreateUserUseCase(respository = userRepository)
        self.getAllUsersUseCase = GetAllUsersUseCase(respository = userRepository)

    def register_routes(self, controllerName: str) -> None:
        self.router.add_url_rule(controllerName, view_func=self.create_user, methods=['POST'])
        self.router.add_url_rule(controllerName, view_func=self.get_users, methods=['GET'])
        self.router.add_url_rule(f'{controllerName}/<int:id>', view_func=self.get_user, methods=['GET'])

    def create_user(self):
        createdUser: UserDTO = self.createUserUseCase.execute(userData = request.get_json())
        return jsonify({"message": "Success User Created!", "data": createdUser.id}), 201
        
    def get_users(self):
        allUsers = self.getAllUsersUseCase.execute()
        return allUsers, 200

    def get_user(self, id):
        user = User.query.get_or_404(id)
        return jsonify(user.to_dict()), 200


user_routes = UserRoutes(Blueprint('user_routes', __name__))

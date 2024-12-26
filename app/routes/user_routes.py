from flask import Blueprint, request, jsonify
from app.domain.DTOs.user_dto import UserDTO
from app.domain.models.user import User
from app.repository.implementations.user_repository import UserRepository
from app.routes.base_routes import BaseRoutes
from app.useCases.user.create_user_useCase import CreateUserUseCase
from app.useCases.user.delete_user_useCase import DeleteUserUseCase
from app.useCases.user.get_all_users_useCase import GetAllUsersUseCase
from app.useCases.user.get_user_by_id_useCase import GetUserByIdUseCase
from app.useCases.user.update_user_UseCase import UpdateUserUseCase
from core.db import get_session


class UserRoutes(BaseRoutes):
    def __init__(self, blueprint: Blueprint):
        userRepository = UserRepository(session=get_session(), model=User)

        self.router = blueprint
        self.register_routes(controllerName="/users")
        self.createUserUseCase = CreateUserUseCase(respository=userRepository)
        self.getAllUsersUseCase = GetAllUsersUseCase(respository=userRepository)
        self.getUserByIdUseCase = GetUserByIdUseCase(respository=userRepository)
        self.deleteUserUseCase = DeleteUserUseCase(respository=userRepository)
        self.updateUserUseCase = UpdateUserUseCase(respository=userRepository)

    def register_routes(self, controllerName: str) -> None:
        self.router.add_url_rule(
            controllerName, view_func=self.create_user, methods=["POST"]
        )
        self.router.add_url_rule(
            controllerName, view_func=self.get_users, methods=["GET"]
        )
        self.router.add_url_rule(
            f"{controllerName}/<int:id>", view_func=self.get_user, methods=["GET"]
        )
        self.router.add_url_rule(
            f"{controllerName}/<int:id>", view_func=self.delete_user, methods=["DELETE"]
        )
        self.router.add_url_rule(
            f"{controllerName}/<int:id>", view_func=self.update_user, methods=["PUT"]
        )

    def create_user(self):
        createdUser: UserDTO = self.createUserUseCase.execute(
            userData=request.get_json()
        )
        return (
            jsonify({"message": "Success User Created!", "data": createdUser.id}),
            201,
        )

    def get_users(self):
        return self.getAllUsersUseCase.execute()

    def get_user(self, id):
        return self.getUserByIdUseCase.execute(userId=id)

    def update_user(self, id):
        return self.updateUserUseCase.execute(userId=id, userData=request.get_json())

    def delete_user(self, id):
        return self.deleteUserUseCase.execute(userId=id)


user_routes = UserRoutes(Blueprint("user_routes", __name__))

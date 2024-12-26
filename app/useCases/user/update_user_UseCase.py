from typing import Dict

from flask import jsonify
from app.domain.DTOs.user_dto import UserDTO
from app.domain.mappers.base_mapper import BaseMapper
from app.domain.mappers.user_mapper import UserMapper
from app.domain.models.user import User
from app.repository.implementations.user_repository import UserRepository


class UpdateUserUseCase:
    def __init__(self, respository: UserRepository):
        self.user_repository: UserRepository = respository
        self.user_mapper: BaseMapper = UserMapper()

    def execute(self, userId: int, userData: dict) -> dict:
        try:
            userDto: UserDTO = self.user_mapper.convertFromJsonToDto(userData)
            existing_user = self.user_repository.read(userId)

            if not existing_user:
                raise Exception("Usuário não encontrado")

            userEntity: User = UserMapper().userDtoToUserEntityMapper(userDto)
            userEntity.id = userId
            updatedUser: UserDTO = UserMapper().userEntityToUserDto(
                self.user_repository.update(userEntity)
            )

            return (
                jsonify(
                    {
                        "message": "Usuário atualizado com sucesso.",
                        "data": self.user_mapper.convertFromDtoToJson(updatedUser),
                    }
                ),
                200,
            )
        except Exception as e:
            return (
                jsonify({"message": f"Erro ao atualizar usuário. {e}", "data": None}),
                500,
            )

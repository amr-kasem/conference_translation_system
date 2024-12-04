from domain.value_objects.register_user import UserRegister
from infrastructure.dtos.sql_alchemy_models.user import UserModel


class UserRegisterModelMapper:
    def to_model(self, register_data: UserRegister) -> UserModel:
        model = UserModel()
        model.name = register_data.name
        model.home_language_id = register_data.home_language
        return model
        
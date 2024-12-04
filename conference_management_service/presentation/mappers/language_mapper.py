from presentation.dtos.register_user import RegisterUserDto
from domain.value_objects.register_user import UserRegister


class RegisterUserMapper:
    def to_user(self,register_user: RegisterUserDto) -> UserRegister:
        user = UserRegister(
            name=register_user.name,
            home_language=register_user.home_language,
        )
        return user
    
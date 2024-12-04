from conference_management_service.presentation.dtos.register_user import RegisterUserDto
from domain.usecases.add_language import RegisterUser
from presentation.mappers.language_mapper import RegisterUserMapper


class UserController:
    @inject
    def __init__(
                    self,
                    register_user: RegisterUser,
                    register_user_mapper: RegisterUserMapper,
                 ) -> None:
        self.register_user = register_user
        self.register_user_mapper = register_user_mapper


    async def register_user_handler(self, dto: RegisterUserDto):
        """Endpoint to register a new user."""
        # try:
        # For simplicity, let's simulate a user registration
        # This can be replaced with actual logic such as saving to a database
        register_data = self.register_user_mapper.to_user(register_user=dto)
        self.register_user(user_register=register_data)
        # Return success response
        return {"message": 'success'}
        # except Exception as e:
        #     # Handle any exceptions and raise HTTP 503 service unavailable error
        #     raise HTTPException(status_code=503, detail=f"Error registering user: {str(e)}")
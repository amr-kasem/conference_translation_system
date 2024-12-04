from fastapi import FastAPI, HTTPException
from injector import inject
from domain.usecases.register_user import RegisterUser
from presentation.messaging import MessagingServices
from presentation.dtos.register_user import RegisterUserDto
from presentation.mappers.register_user_mapper import RegisterUserMapper
# FastAPI App class
class ApiServices:
    @inject
    def __init__(
        self,
        register_user: RegisterUser,
        register_user_mapper: RegisterUserMapper,
    ):
        self.app : FastAPI = FastAPI()  # FastAPI instance
        self.register_user = register_user
        self.register_user_mapper = register_user_mapper

    def init(self,messaging_interface : MessagingServices):
        self.messaging_interface = messaging_interface

        # Register routes
        self.app.add_api_route("/register", self._register_user_handler, methods=["POST"])
        
        # Add startup and shutdown events
        self.app.add_event_handler("startup", self.on_startup)
        self.app.add_event_handler("shutdown", self.on_shutdown)


    async def _register_user_handler(self, dto: RegisterUserDto):
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

    async def on_startup(self):
        """FastAPI startup event handler."""
        await self.messaging_interface.connect()

    async def on_shutdown(self):
        """FastAPI shutdown event handler."""
        await self.messaging_interface.close()

    def get_app(self):
        """Returns the FastAPI instance."""
        return self.app

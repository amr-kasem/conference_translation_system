from fastapi import FastAPI, HTTPException
from injector import inject
from presentation.messaging import MessagingServices
from presentation.dtos.register_user import RegisterUserDto
from presentation.api.user_controller import UserController
# FastAPI App class
class ApiServices:
    @inject
    def __init__(
        self,
        user_controller: UserController
    ):
        self.app : FastAPI = FastAPI()  # FastAPI instance
        self.user_controller = user_controller


    def init(self,messaging_interface : MessagingServices):
        self.messaging_interface = messaging_interface

        # user routes
        self.app.add_api_route("/register", self.user_controller.register_user, methods=["POST"])
        
        
        # language routes
        self.app.add_api_route("/languages/", self._register_user_handler, methods=["POST"])
        
        # Add startup and shutdown events
        self.app.add_event_handler("startup", self.on_startup)
        self.app.add_event_handler("shutdown", self.on_shutdown)
        


    async def on_startup(self):
        """FastAPI startup event handler."""
        await self.messaging_interface.connect()

    async def on_shutdown(self):
        """FastAPI shutdown event handler."""
        await self.messaging_interface.close()

    def get_app(self):
        """Returns the FastAPI instance."""
        return self.app

from fastapi import FastAPI, HTTPException
from injector import inject
from presentation.messaging.messaging import MessagingServices
from presentation.api.controllers.user_controller import UserController
from presentation.api.controllers.language_controller import LanguageController
from presentation.api.controllers.conference_controller import ConferenceController
from presentation.api.controllers.attendance_controller import AttendanceController
# FastAPI App class
class RestApi:
    @inject
    def __init__(
        self,
        user_controller: UserController,
        language_controller: LanguageController,
        conference_controller: ConferenceController,
        attendance_controller: AttendanceController,
    ):
        self.app : FastAPI = FastAPI()  # FastAPI instance
        self.user_controller = user_controller
        self.language_controller = language_controller
        self.conference_controller = conference_controller
        self.attendance_controller = attendance_controller


    def init(self,messaging_interface : MessagingServices):
        self.messaging_interface = messaging_interface

        # user routes
        self.app.add_api_route("/register", self.user_controller.register_user_handler, methods=["POST"])
        self.app.add_api_route("/join/{conference_id}", self.attendance_controller.join_handler, methods=["POST"])
        
        # language routes
        self.app.add_api_route("/languages", self.language_controller.add_language_handler, methods=["POST"])
        self.app.add_api_route("/languages", self.language_controller.get_languages_handler, methods=["GET"])
        self.app.add_api_route("/languages/{language_id}", self.language_controller.delete_language_handler, methods=["DELETE"])
        
        # conference routes
        self.app.add_api_route("/conferences", self.conference_controller.add_conference_handler, methods=["POST"])
        self.app.add_api_route("/conferences", self.conference_controller.get_conferences_handler, methods=["GET"])
        self.app.add_api_route("/conferences/{conference_id}/invitation_code", self.conference_controller.get_qr_code, methods=["GET"])
        self.app.add_api_route("/conferences/{conference_id}/start", self.conference_controller.start_conference, methods=["GET"])
        self.app.add_api_route("/conferences/{conference_id}/stop", self.conference_controller.end_conference, methods=["GET"])
        self.app.add_api_route("/conferences/{conference_id}/raise_hand", self.user_controller.raise_hand_handler, methods=["POST"])
        self.app.add_api_route("/conferences/{conference_id}/finish_speech", self.user_controller.finish_speech_handler, methods=["POST"])
        
        
        # attendance routes
        self.app.add_api_route("/join/{conference_id}", self.attendance_controller.join_handler, methods=["POST"])
        self.app.add_api_route("/leave/{conference_id}", self.attendance_controller.leave_handler, methods=["POST"])
        
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

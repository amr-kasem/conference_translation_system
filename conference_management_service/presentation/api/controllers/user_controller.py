from fastapi import  HTTPException

from injector import inject

from domain.usecases.user.end_speech import FinishSpeech
from presentation.api.dtos.attendance.attendance_request import AttendanceRequestDto
from domain.usecases.user.register_user import RegisterUser
from domain.usecases.user.raise_hand import RaiseHand
from presentation.api.mappers.user_mapper import UserMapper
from presentation.api.dtos.user.register_user import RegisterUserDto


class UserController:
    @inject
    def __init__(
                    self,
                    register_user: RegisterUser,
                    raise_hand:RaiseHand,
                    finish_speaking: FinishSpeech,
                    register_user_mapper: UserMapper,
                    
                 ) -> None:
        self.register_user = register_user
        self.raise_hand = raise_hand
        self.finish_speech = finish_speaking
        self.user_mapper = register_user_mapper

    async def register_user_handler(self, dto: RegisterUserDto):
        """Endpoint to register a new user."""
        try:
            # For simplicity, let's simulate a user registration
            # This can be replaced with actual logic such as saving to a database
            register_data = self.user_mapper.to_user(register_user=dto)
            self.register_user(user_register=register_data)
            # Return success response
            return {"message": 'success'}
        except Exception as e:
            # Handle any exceptions and raise HTTP 503 service unavailable error
            raise HTTPException(status_code=503, detail=f"Error registering user: {str(e)}")
        


    async def finish_speech_handler(self, conference_id :str, attendance_id:str):
        """Endpoint to register a new user."""
        try:
            # For simplicity, let's simulate a user registration
            # This can be replaced with actual logic such as saving to a database
            req = self.user_mapper.to_stop_speaking(attendance_id=attendance_id,conference_id=conference_id)
            self.finish_speech(req)
            # Return success response
            return {"message": 'success'}
        except Exception as e:
            # Handle any exceptions and raise HTTP 503 service unavailable error
            raise HTTPException(status_code=503, detail=f"Error registering user: {str(e)}")
        


    async def raise_hand_handler(self, conference_id :str, attendance: str):
        """Endpoint to register a new user."""
        try:
            # For simplicity, let's simulate a user registration
            # This can be replaced with actual logic such as saving to a database
            req = self.user_mapper.to_raise_hand(attendance_id=attendance,conference_id=conference_id)
            self.raise_hand(req)
            # Return success response
            return {"message": 'success'}
        except Exception as e:
            # Handle any exceptions and raise HTTP 503 service unavailable error
            raise HTTPException(status_code=503, detail=f"Error registering user: {str(e)}")
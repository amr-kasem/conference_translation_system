from injector import inject

from domain.value_objects.language import LanguageData
from presentation.api.mappers.language_mapper import LanguageDtoMapper
from presentation.api.dtos.user.user import UserDto
from presentation.api.dtos.user.register_user import RegisterUserDto
from domain.value_objects.user import UserData
from domain.value_objects.attendance_data import AttendanceData
from domain.value_objects.raise_hand_request import RaiseHandRequest
from domain.value_objects.stop_speaking_request import StopSpeakingRequest


class UserMapper:
    @inject
    def __init__(self, language_mapper: LanguageDtoMapper) -> None:
        self.language_mapper = language_mapper
        
    def to_rigster_user(self,register_user: RegisterUserDto) -> UserData:
        user = UserData(
            id=None,
            name=register_user.name,
            home_language=LanguageData(
                id=register_user.home_language,
                translation_id='',
                name='',
                asr=False,
                t2t=False,
                tts=False,
            ),
        )
        return user
    
    def to_dto(self,user:UserData) -> UserDto :
        user = UserDto(
            id=user.id,
            name=user.name,
            home_language=self.language_mapper.to_dto(user.home_language),
        )
        return user
    
    def to_stop_speaking(self, attendance_id: str, conference_id: str):
        return StopSpeakingRequest(
            attendence=attendance_id,
            conference_id=conference_id,
        )
            
    def to_raise_hand(self, attendance_id: str, conference_id: str):
        return RaiseHandRequest(
            attendence=attendance_id,
            conference_id=conference_id,
        )
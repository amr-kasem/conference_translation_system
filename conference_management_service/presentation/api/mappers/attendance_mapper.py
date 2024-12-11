from injector import inject

from presentation.api.dtos.attendance.attendance import AttendanceDto
from presentation.api.mappers.language_mapper import LanguageDtoMapper
from presentation.api.mappers.user_mapper import UserMapper
from domain.value_objects.join_request import JoinRequest
from domain.value_objects.language import LanguageData
from domain.value_objects.user import UserData
from presentation.api.dtos.attendance.attendance_request import AttendanceRequestDto
from domain.value_objects.conference import AttendanceData



class AttendanceDtoMapper:
    @inject
    def __init__(self,user_mapper:UserMapper, language_mapper: LanguageDtoMapper) -> None:
        self.user_mapper = user_mapper
        self.language_mapper = language_mapper
        
        pass
    def to_attendance(self,dto:AttendanceRequestDto) -> AttendanceData:
        data = AttendanceData(
            user=UserData(
                    id=dto.user,
                    home_language= None,
                    name=None,
                ),
            language=LanguageData(
                id=dto.language,
                translation_id=None,
                name=None,
                asr=None,
                t2t=None,
                tts=None,
                ),
            end=None,
            id=None,
            start=None,
        )
        return data
    
    def to_join_request(self, attendance: AttendanceData, conference_id: str):
        return JoinRequest(
            attendence=attendance,
            conference_id=conference_id,
        )
    def to_dto(self,data: AttendanceData) -> AttendanceDto :
        dto = AttendanceDto(
            id = data.id,
            user =  self.user_mapper.to_dto(data.user),
            language = self.language_mapper.to_dto(data.language),
            start = data.start,
            end = data.end,
        )
        return dto
    
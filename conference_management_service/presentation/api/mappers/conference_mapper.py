from injector import inject

from presentation.api.mappers.attendance_mapper import AttendanceDtoMapper
from presentation.api.mappers.user_mapper import UserMapper
from domain.entities.conference import Conference
from domain.value_objects.conference import ConferenceData
from presentation.api.dtos.conference.conference import ConferenceDto
from presentation.api.dtos.conference.create_conference import CreateConference



class ConferenceDtoMapper:
    @inject
    def __init__(self,user_mapper:UserMapper,attendance_mapper: AttendanceDtoMapper) -> None:
        self.user_mapper = user_mapper
        self.attendance_mapper = attendance_mapper
        pass
    def to_conference(self,dto: CreateConference) -> Conference:
        data = Conference(
            data=ConferenceData(
                name=dto.name,
                id = None, 
                start = None, 
                end = None, 
                attendees = None, 
                speaker = None, 
            )
        )
        return data
    
    def to_dto(self,conference: Conference) -> ConferenceDto :
        dto = ConferenceDto(
            name = conference.data.name, 
            id = conference.data.id, 
            start = conference.data.start, 
            end = conference.data.end, 
            attendees = [self.attendance_mapper.to_dto(a) for a in conference.data.attendees],# conference.data.attendees, 
            speaker =  self.user_mapper.to_dto(conference.data.speaker) if conference.data.speaker is not None else None, 
        )
        return dto
    
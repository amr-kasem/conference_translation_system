from injector import inject

from domain.value_objects.conference import ConferenceData
from infrastructure.dtos.sql_alchemy_models.conference import ConferenceModel
from infrastructure.mappers.attendance_model_mapper import AttendanceModelMapper
from infrastructure.mappers.user_model_mapper import UserModelMapper


class ConferenceModelMapper:
    @inject
    def __init__(self, user_mapper: UserModelMapper, attendance_mapper:AttendanceModelMapper) -> None:
        self.user_mapper = user_mapper
        self.attendance_mapper = attendance_mapper
        
    def to_model(self, data: ConferenceData) -> ConferenceModel:
        model = ConferenceModel()
        if data.id is not None:
            model.id = data.id
        model.name = data.name
        model.start = data.start
        model.end = data.end
        if data.speaker is not None:
            model.speaker_id = data.speaker.id
        model.private = False
        return model
    def to_data(self, model:  ConferenceModel) -> ConferenceData :
        data = ConferenceData(
            id =  str(model.id),
            name =  model.name,
            start =  model.start,
            end =  model.end,
            speaker = self.user_mapper.to_data(model.speaker) if model.speaker is not None else None,
            attendees=[self.attendance_mapper.to_data(attendee) for attendee in model.attendees]
        )
        
        return data
        
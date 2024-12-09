from injector import inject

from infrastructure.mappers.language_model_mapper import LanguageModelMapper
from infrastructure.mappers.user_model_mapper import UserModelMapper
from domain.value_objects.attendance_data import AttendanceData
from infrastructure.dtos.sql_alchemy_models.attendance import AttendanceModel


class AttendanceModelMapper:
    @inject
    def __init__(self, language_mapper: LanguageModelMapper, user_mapper: UserModelMapper):
        self.language_mapper = language_mapper   
        self.user_mapper = user_mapper     
        
    def to_model(self, data: AttendanceData) -> AttendanceModel:
        model = AttendanceModel()
        if data.id is not None:
            model.id = data.id
        model.user_id = data.user.id
        model.language_id = data.language.id
        model.start = data.start
        model.end = data.end
        return model
    def to_data(self, model:  AttendanceModel) -> AttendanceData :
        data = AttendanceData(
            id =  str(model.id),
            start =  model.start,
            end =  model.end,
            language=self.language_mapper.to_data(model.language),
            user=self.user_mapper.to_data(model.user)
        )
        
        return data
        
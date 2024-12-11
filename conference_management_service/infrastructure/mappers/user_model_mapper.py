from injector import inject

from infrastructure.mappers.language_model_mapper import LanguageModelMapper
from domain.value_objects.user import UserData
from infrastructure.dtos.sql_alchemy_models.user import UserModel


class UserModelMapper:
    @inject
    def __init__(self, language_mapper: LanguageModelMapper):
        self.language_mapper = language_mapper   
    
    def to_model(self, user: UserData) -> UserModel:
        model = UserModel()
        if user.id is not None:
            model.id = user.id
        model.name = user.name
        model.home_language_id = user.home_language.id
        return model 
        
    def to_data(self, model: UserModel):
        return UserData(
            id=str(model.id),
            name=model.name,
            home_language=self.language_mapper.to_data(model.home_language),
        )
from domain.value_objects.language import LanguageData
from infrastructure.dtos.sql_alchemy_models.language import LanguageModel


class LanguageModelMapper:
    def to_model(self, data: LanguageData) -> LanguageModel:
        model = LanguageModel()
        model.id = data.id
        model.translation_id = data.translation_id
        model.name = data.name
        model.asr = data.asr
        model.t2t = data.t2t
        model.tts = data.tts
        return model
        
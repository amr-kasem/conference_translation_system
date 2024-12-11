from domain.value_objects.language import LanguageData
from infrastructure.dtos.sql_alchemy_models.language import LanguageModel


class LanguageModelMapper:
    def to_model(self, data: LanguageData) -> LanguageModel:
        model = LanguageModel()
        if data.id is not None:
            model.id = data.id
        model.translation_id = data.translation_id
        model.name = data.name
        model.asr = data.asr
        model.t2t = data.t2t
        model.tts = data.tts
        return model
    def to_data(self, model:  LanguageModel) -> LanguageData :
        data = LanguageData(
            id = str(model.id),
            translation_id = str(model.translation_id),
            name = model.name,
            asr = model.asr,
            t2t = model.t2t,
            tts = model.tts,
        )
        return data
        
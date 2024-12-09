from logging import Logger
from injector import inject

from domain.value_objects.translation_result import TranslationResult
from domain.value_objects.translation_request import TranslationRequest
from domain.usecases.conference.get_conference import GetConference
from domain.usecases.usecase import Usecase
class HandleTranslation(Usecase):
    @inject
    def __init__(self, get_conference:GetConference):
        self.get_conference = get_conference 
    def __call__(self,request:TranslationRequest)->list[TranslationResult]:
        conf = self.get_conference(request.conference_id)
        if conf.isInitialized():
            # TODO: translate and return
            print(
                f'''
                    should translate from {conf.data.speaker} to {conf.get_listener_languages()}
                '''
            )
            return []
        else: 
            raise Exception('Conference is not initiailized')
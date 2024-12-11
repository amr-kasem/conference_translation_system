from dataclasses import replace
from logging import Logger
from typing import Callable
from injector import inject

from domain.value_objects.translation_result import TranslationResult
from domain.value_objects.translation_request import TranslationRequest
from domain.usecases.conference.get_conference import GetConference
from domain.repositories.translation_repository import TranslationRepository
from domain.usecases.usecase import Usecase
class HandleTranslation(Usecase):
    @inject
    def __init__(self, get_conference:GetConference, translation_repository:TranslationRepository):
        self.get_conference = get_conference 
        self.translation_callback : Callable[[list[TranslationResult]],None] = None
        self.translation_repository = translation_repository
        
    def init(self, translation_callback: Callable[[list[TranslationResult]],None]):
        self.translation_callback = translation_callback
        
    def __call__(self,request:TranslationRequest)->None:
        conf = self.get_conference(request.conference_id)
        if conf.isInitialized():
            # TODO: translate and return
            print(
                f'''
                    should translate from {conf.data.speaker} to {conf.get_listener_languages()}
                '''
            )
            result =  []
            src = request.voice,conf.data.speaker.language
            for t in conf.get_listener_languages():
                r = self.translation_repository.translate(request.voice,src,t)
                r = replace(r, conference_id=request.conference_id)
            self.translation_callback(result)
            return None
        
        else: 
            raise Exception('Conference is not initiailized')
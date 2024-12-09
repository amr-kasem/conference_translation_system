from domain.usecases.user.end_speech import FinishSpeech
from domain.usecases.user.raise_hand import RaiseHand
from presentation.app import InstantTranslationApp
from presentation.api.controllers.attendance_controller import AttendanceController
from presentation.api.controllers.conference_controller import ConferenceController
from presentation.api.controllers.language_controller import LanguageController
from presentation.api.controllers.user_controller import UserController
from presentation.api.mappers.attendance_mapper import AttendanceDtoMapper
from presentation.api.mappers.conference_mapper import ConferenceDtoMapper
from presentation.api.mappers.language_mapper import LanguageDtoMapper
from presentation.api.rest_api import RestApi
from domain.usecases.attendance.join_conference import JoinConference
from domain.usecases.conference.add_conference import AddConference
from domain.usecases.conference.delete_conference import DeleteConference
from domain.usecases.conference.end_conference import StopConference
from domain.usecases.conference.get_conference import GetConference
from domain.usecases.conference.get_conference_qr import GetConferenceQr
from domain.usecases.conference.get_conferences import GetConferences
from domain.usecases.conference.initialize_conference import InitializeConference
from domain.usecases.conference.start_conference import StartConference
from domain.usecases.language.add_language import AddLanguage
from domain.usecases.language.delete_language import DeleteLanguage
from domain.usecases.language.get_languages import GetLanguages
from domain.usecases.maintanance.migrate import Migrate
from domain.usecases.translation.handle_translation import HandleTranslation
from domain.usecases.user.register_user import RegisterUser
from injector import Module, singleton


from presentation.messaging.messaging import MessagingServices
from infrastructure.data_sources.in_memory.dict_in_memory_datasource import DictInMemoryDataSource
from infrastructure.data_sources.in_memory.in_memory_datasource import InMemoryDataSource

# Create an Injector class to manage dependencies
from infrastructure.mappers.attendance_model_mapper import AttendanceModelMapper
from infrastructure.mappers.conference_model_mapper import ConferenceModelMapper
from infrastructure.mappers.language_model_mapper import LanguageModelMapper
from infrastructure.mappers.user_model_mapper import UserModelMapper
from infrastructure.data_sources.qr_generator.qr_generator import QRcodeGenerator
from infrastructure.data_sources.qr_generator.qr_generator_datasource import QRcodeGeneratorImpl
from domain.repositories.conference_management_repository import ConferenceManagementRepository
from infrastructure.data_sources.data_persistance.persistance_datasource import PersistanceDataSource
from infrastructure.data_sources.data_persistance.postgre_persistance_datasource import SQLAlchemyPersistenceDataSource
from infrastructure.repositories_impl.conference_management_repository_impl import ConferenceManagementRepositoryImpl
from presentation.api.mappers.user_mapper import UserMapper
# from presentation.api import ApiServices


class ConfigModule(Module):
    def configure(self, binder):
        # Bind the Database class to itself, meaning an instance of Database
        ######################################
        # data sources                       #
        ######################################
        binder.bind(PersistanceDataSource, to=SQLAlchemyPersistenceDataSource, scope=singleton)
        binder.bind(QRcodeGenerator, to=QRcodeGeneratorImpl, scope=singleton)
        binder.bind(InMemoryDataSource, to=DictInMemoryDataSource, scope=singleton)
        # Optionally, you could bind other dependencies or configurations here
        
        ######################################
        # data mappers                       #
        ######################################
        binder.bind(AttendanceModelMapper, to=AttendanceModelMapper, scope=singleton)
        binder.bind(ConferenceModelMapper, to=ConferenceModelMapper, scope=singleton)
        binder.bind(LanguageModelMapper, to=LanguageModelMapper, scope=singleton)        
        binder.bind(UserModelMapper, to=UserModelMapper, scope=singleton)        
        
        ######################################
        # Repositories                       #
        ######################################
        # binder.bind(ConferenceHandlingRepository, to=ConferenceHandlingRepositoryImpl)
        binder.bind(ConferenceManagementRepository, to=ConferenceManagementRepositoryImpl, scope=singleton)


        ######################################
        # usecases                           #
        ######################################
        binder.bind(JoinConference, to=JoinConference, scope=singleton)
        binder.bind(AddConference, to=AddConference, scope=singleton)
        binder.bind(DeleteConference, to=DeleteConference, scope=singleton)
        binder.bind(StopConference, to=StopConference, scope=singleton)
        binder.bind(GetConferenceQr, to=GetConferenceQr, scope=singleton)
        binder.bind(GetConference, to=GetConference, scope=singleton)
        binder.bind(GetConferences, to=GetConferences, scope=singleton)
        binder.bind(InitializeConference, to=InitializeConference, scope=singleton)
        binder.bind(StartConference, to=StartConference, scope=singleton)
        binder.bind(AddLanguage, to=AddLanguage, scope=singleton)
        binder.bind(DeleteLanguage, to=DeleteLanguage, scope=singleton)
        binder.bind(GetLanguages, to=GetLanguages, scope=singleton)
        binder.bind(Migrate, to=Migrate, scope=singleton)
        binder.bind(HandleTranslation, to=HandleTranslation, scope=singleton)
        binder.bind(RegisterUser, to=RegisterUser, scope=singleton)
        binder.bind(FinishSpeech, to=FinishSpeech, scope=singleton)
        binder.bind(RaiseHand, to=RaiseHand, scope=singleton)
        
        ######################################
        # presnetaion services               #
        ######################################
        binder.bind(RestApi, to=RestApi, scope=singleton)
        binder.bind(MessagingServices, to=MessagingServices, scope=singleton)
        
        ######################################
        # API Controllers                    #
        ######################################
        binder.bind(AttendanceController, to=AttendanceController, scope=singleton)
        binder.bind(ConferenceController, to=ConferenceController, scope=singleton)
        binder.bind(LanguageController, to=LanguageController, scope=singleton)
        binder.bind(UserController, to=UserController, scope=singleton)

                
        ######################################
        # presnetaion mappers                #
        ######################################
        binder.bind(UserMapper, to=UserMapper, scope=singleton)
        binder.bind(AttendanceDtoMapper, to=AttendanceDtoMapper, scope=singleton)
        binder.bind(ConferenceDtoMapper, to=ConferenceDtoMapper, scope=singleton)
        binder.bind(LanguageDtoMapper, to=LanguageDtoMapper, scope=singleton)
        
        ######################################
        # app                                #
        ######################################
        binder.bind(InstantTranslationApp, to=InstantTranslationApp, scope=singleton)

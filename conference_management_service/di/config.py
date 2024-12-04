# Create an Injector class to manage dependencies
from domain.repositories.conference_management_repository import ConferenceManagementRepository
from infrastructure.data_sources.data_persistance.persistance_datasource import PersistanceDataSource
from infrastructure.data_sources.data_persistance.postgre_persistance_datasource import SQLAlchemyPersistenceDataSource
from infrastructure.repositories_impl.conference_management_repository_impl import ConferenceManagementRepositoryImpl
from injector import Module, singleton
# from presentation.api import ApiServices


class ConfigModule(Module):
    def configure(self, binder):
        # Bind the Database class to itself, meaning an instance of Database
        ######################################
        # Repositories                       #
        ######################################
        # binder.bind(ConferenceHandlingRepository, to=ConferenceHandlingRepositoryImpl)
        binder.bind(ConferenceManagementRepository, to=ConferenceManagementRepositoryImpl)
        ######################################
        # data sources                       #
        ######################################
        binder.bind(PersistanceDataSource, to=SQLAlchemyPersistenceDataSource)
        # binder.bind(StreamingInferenceDatasource, to=StreamingInferenceDatasource)
        # binder.bind(QRcodeGenerator, to=QRcodeGeneratorImpl)
        # Optionally, you could bind other dependencies or configurations here
        
        ######################################
        # presnetaion services               #
        ######################################
        # binder.bind(Api, to=Api, scope=singleton)
        # binder.bind(MessagingInterface, to=MessagingInterface, scope=singleton)
        
        ######################################
        # presnetaion mappers                #
        ######################################
        # binder.bind(RegisterUserMapper, to=RegisterUserMapper, scope=singleton)

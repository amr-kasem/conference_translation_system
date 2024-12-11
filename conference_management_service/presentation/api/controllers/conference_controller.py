from fastapi import  HTTPException
from fastapi.responses import StreamingResponse

from injector import inject

from domain.value_objects.speaker_change_data import SpeakerChangeData
from presentation.rtc_services.rtc_services import RTCServices
from domain.value_objects.intialize_conference_request import InitializeConferenceRequest
from domain.usecases.conference.end_conference import StopConference
from domain.usecases.conference.start_conference import StartConference

from domain.usecases.conference.get_conferences import GetConferences
from domain.usecases.conference.add_conference import AddConference
from domain.usecases.conference.delete_conference import DeleteConference
from domain.usecases.conference.get_conference_qr import GetConferenceQr
from presentation.api.dtos.conference.create_conference import CreateConference
from presentation.messaging.messaging import MessagingServices
from presentation.api.mappers.conference_mapper import ConferenceDtoMapper

class ConferenceController:
    @inject
    def __init__(
                    self,
                    add_conference: AddConference,
                    get_conferences: GetConferences,
                    start:StartConference,
                    stop:StopConference,
                    get_qr: GetConferenceQr,
                    delete_conference: DeleteConference,
                    conference_mapper: ConferenceDtoMapper,
                    messaging: MessagingServices,
                    rtc_services: RTCServices,
                 ) -> None:
        self.add_conference = add_conference
        self.get_conferences = get_conferences
        self.delete_conference = delete_conference
        self.conference_mapper = conference_mapper
        self.get_qr = get_qr
        self.messaging = messaging
        self.rtc_services = rtc_services
        self.start = start
        self.stop = stop


    async def add_conference_handler(self, dto:CreateConference):
        """Endpoint to add new conference."""
        try:
        # For simplicity, let's simulate a user registration
        # This can be replaced with actual logic such as saving to a database
            conference = self.conference_mapper.to_conference(dto=dto)
            self.add_conference(conference=conference)
            # Return success response
            return {"message": 'success'}
        except Exception as e:
            # Handle any exceptions and raise HTTP 503 service unavailable error
            raise HTTPException(status_code=503, detail=f"Error registering user: {str(e)}")
        
        
    async def get_conferences_handler(self):
        """Endpoint to add new conference."""
        try:
            # For simplicity, let's simulate a user registration
            # This can be replaced with actual logic such as saving to a database
            langs = self.get_conferences()
            conferences = [self.conference_mapper.to_dto(conference) for conference in langs] 
            # Return success response
            return conferences
        except Exception as e:
            # Handle any exceptions and raise HTTP 503 service unavailable error
            raise HTTPException(status_code=503, detail=f"Error registering user: {str(e)}")
        
    async def delete_conference_handler(self, conference_id: str):
        """Endpoint to add new conference."""
        try:
        # For simplicity, let's simulate a user registration
        # This can be replaced with actual logic such as saving to a database
            self.delete_conference(conference_id=conference_id)
            # Return success response
            return {"message": 'success'}
        except Exception as e:
            # Handle any exceptions and raise HTTP 503 service unavailable error
            raise HTTPException(status_code=503, detail=f"Error registering user: {str(e)}")
        
    async def get_qr_code(self, conference_id: str):
        """Endpoint to add new conference."""
        try:
        # For simplicity, let's simulate a user registration
        # This can be replaced with actual logic such as saving to a database
            img = self.get_qr(id=conference_id)
            # Return success response
            return StreamingResponse(img, media_type="image/png")
        except Exception as e:
            # Handle any exceptions and raise HTTP 503 service unavailable error
            raise HTTPException(status_code=503, detail=f"Error registering user: {str(e)}")
    
    def speaker_callback(self, speaker:SpeakerChangeData):
        self.messaging.speaker_callback(speaker)
        self.rtc_services.change_speaker(speaker)
    
    async def start_conference(self, conference_id: str):
        """Endpoint to add new conference."""
        try:
        # For simplicity, let's simulate a user registration
        # This can be replaced with actual logic such as saving to a database
            self.start(InitializeConferenceRequest(conference_id=conference_id,on_speaker_change=self.speaker_callback))
            self.rtc_services.add_callee(conference_id=conference_id)
            # Return success response
            return {"message": 'success'}
        

        except Exception as e:
            print(e)
            # Handle any exceptions and raise HTTP 503 service unavailable error
            raise HTTPException(status_code=503, detail=f"Error registering user: {str(e)}")
        
        
    async def end_conference(self, conference_id: str):
        """Endpoint to add new conference."""
        try:
        # For simplicity, let's simulate a user registration
        # This can be replaced with actual logic such as saving to a database
            self.stop(id=conference_id)
            self.rtc_services.remove_callee(conference_id=conference_id)
            # Return success response
            return {"message": 'success'}

        except Exception as e:
            print(e)
            # Handle any exceptions and raise HTTP 503 service unavailable error
            raise HTTPException(status_code=503, detail=f"Error registering user: {str(e)}")
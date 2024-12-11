from fastapi import  HTTPException

from injector import inject

from domain.usecases.attendance.join_conference import JoinConference
from presentation.api.mappers.attendance_mapper import AttendanceDtoMapper
from presentation.api.dtos.attendance.attendance_request import AttendanceRequestDto


class AttendanceController:
    @inject
    def __init__(
                    self,
                    join_conference: JoinConference,
                    # leave_conference: ExitConference,
                    attendance_mapper: AttendanceDtoMapper,
                 ) -> None:
        self.join_conference = join_conference
        self.attendance_mapper = attendance_mapper
    async def join_handler(self, conference_id :str, dto: AttendanceRequestDto):
        """Endpoint to register a new user."""
        try:
            # For simplicity, let's simulate a user registration
            # This can be replaced with actual logic such as saving to a database
            att = self.attendance_mapper.to_attendance(dto=dto)
            req = self.attendance_mapper.to_join_request(attendance=att,conference_id=conference_id)
            self.join_conference(request=req)
            # Return success response
            return {"message": 'success'}
        except Exception as e:
            # Handle any exceptions and raise HTTP 503 service unavailable error
            raise HTTPException(status_code=503, detail=f"Error registering user: {str(e)}")
    
    async def leave_handler(self, conference_id :str, dto: AttendanceRequestDto):
        """Endpoint to register a new user."""
        try:
            # For simplicity, let's simulate a user registration
            # This can be replaced with actual logic such as saving to a database
            # att = self.attendance_mapper.to_attendance(dto=dto)
            # req = self.attendance_mapper.to_join_request(attendance=att,conference_id=conference_id)
            # self.join_conference(request=req)
            # Return success response
            return {"message": 'not impelemented yet'}
        except Exception as e:
            # Handle any exceptions and raise HTTP 503 service unavailable error
            raise HTTPException(status_code=503, detail=f"Error registering user: {str(e)}")
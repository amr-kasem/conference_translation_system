from domain.value_objects.conference import ConferenceData


class Conference:
    def __init__(self, data: ConferenceData):
        self.data: ConferenceData = data

    def add_attendee(self):
        pass

    def get_attendees(self):
        pass
    
    def set_speaker(self):
        pass
    
    def get_listener_languages(self):
        pass

    def get_speaker_language(self):
        pass
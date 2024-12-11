from dataclasses import replace
from datetime import datetime
from typing import Callable, Optional
from domain.value_objects.speaker_change_data import SpeakerChangeData
from domain.value_objects.user import UserData
from domain.value_objects.attendance_data import AttendanceData
from domain.value_objects.translation_meta import TranslationMeta
from domain.value_objects.conference import ConferenceData


class Conference:
    def __init__(self, data: ConferenceData):
        self.data: ConferenceData = data
        self._initialized = False
        self.translation_meta = None
        self.running = False
        self.speaker_callback :Optional[Callable[[SpeakerChangeData],None]] = None
        
    def add_attendee(self,attendee: AttendanceData):
        if not self._initialized:
            raise Exception('conference is not initialized')
        self.data.attendees.append(attendee)
        self.translation_meta.languages.add(f'{self.data.id}/{attendee.language.id}')

    def set_speaker(self):
        if not self._initialized:
            raise Exception('conference is not initialized')
        next_speaker = None
        try:
            next_speaker = self.translation_meta.speaker_queue.pop()
        except:
            pass
        if next_speaker is None:
            self.speaker_callback(
                SpeakerChangeData(
                    conference_id=self.data.id,
                    speaker_id='<NOSPEAKER>',
                )
            )
            raise Exception('No speaker in the queue')
        if self.data.speaker is None:
            self.data = replace(self.data,speaker = next_speaker)
            self.translation_meta = replace(self.translation_meta, speaker = next_speaker.id)
            self.speaker_callback(
                SpeakerChangeData(
                    conference_id=self.data.id,
                    speaker_id=next_speaker.id,
                )
            )
        else :
            raise Exception('Wait until other finish')
        
    def raise_hand(self, speaker: AttendanceData):
        if not self._initialized:
            raise Exception('conference is not initialized')
        if speaker in self.data.attendees:
            if speaker in self.translation_meta.speaker_queue:
                raise Exception('Already in queue')
            if speaker.id == self.translation_meta.speaker:
                raise Exception('Already speaking')
            self.translation_meta.speaker_queue.append(speaker)
            try:
                self.set_speaker()
            except Exception as e:
                print(e)
        else:
            raise Exception('Speaker should be one of attendees.') 
            
    def finish_speach(self, attendance_id:str):
        if not self._initialized:
            raise Exception('conference is not initialized')
        if self.data.speaker is None:
            raise Exception('Already finished')
        if attendance_id == self.translation_meta.speaker:
            self.data = replace(self.data, speaker = None)
            self.translation_meta = replace(self.translation_meta, speaker = None)
            try:
                self.set_speaker()
            except Exception as e:
                print(e)
        else:
            raise Exception('Cannot stop other speaker') 
        
    def get_listener_languages(self)->list[str]:
        if not self._initialized:
            raise Exception('conference is not initialized')
        langs = [l for l in self.translation_meta.languages]
        langs.remove(f'{self.data.id}/{self.data.speaker.language.id}')
        return langs

    
    def init(self, speaker_callback: Callable[[SpeakerChangeData],None]):
        if speaker_callback is None:
            raise Exception('Speaker change callback is not set')
        self.translation_meta = TranslationMeta(
            speaker=self.data.speaker.id if self.data.speaker else None,
            languages={f'{self.data.id}/{att.language.id}' for att in self.data.attendees},
            speaker_queue=[],
        )
        self.speaker_callback = speaker_callback
        self._initialized = True
        
        
    def isInitialized(self)->bool:
        return self._initialized
    
    def start(self)->bool:
        if not self._initialized:
            raise Exception('conference is not initialized')
        self.data = replace(self.data,start=datetime.now())
        self.running = True
        
    def stop(self)->bool:
        if not self._initialized :
            raise Exception('conference is not initialized')
        if not self.data.start:
            raise Exception('conference isn\'t started yet.')
        self.data = replace(self.data,end=datetime.now())
        self.running = False
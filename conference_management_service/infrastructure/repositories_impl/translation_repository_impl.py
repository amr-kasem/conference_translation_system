from io import BytesIO
from domain.value_objects.language import LanguageData
from domain.value_objects.translation_result import TranslationResult
from domain.value_objects.init_translation_request import InitTranslationRequest
from domain.value_objects.translation_request import TranslationRequest
from domain.value_objects.vad_request import VadRequest
from domain.value_objects.init_vad_request import InitVadRequest
from infrastructure.data_sources.translation_datasource.translation_datasource import TranslationDataSource
from infrastructure.data_sources.vad.vad_datasource import VadDataSource
from domain.repositories.translation_repository import TranslationRepository

class TranslationRepositoryImpl(TranslationRepository):
    def __init__(
        self,
        vad_datasource: VadDataSource,
        translate_datasource: TranslationDataSource,
    ) -> None:
        super().__init__()
        self.vad_datasource = vad_datasource
        self.translate_datasource = translate_datasource
        self.on_voice_received = None
    def _on_voice(self, msg) -> TranslationRequest:
        return None

    def init_vad(self, req: InitVadRequest) -> None:
        """
        Initialize Voice Activity Detection (VAD).
        This method prepares the system to detect and process speech-to-text data. 
        It should be called before starting to transcribe or translate audio.
        """
        self.on_voice_received = req.on_voice_recieved

        self.vad_datasource.init(
            voice_callback=self._on_voice,
            host=req.vad_host,
            port=req.vad_port,   
        )

    def stop_vad(self) -> None:
        """
        Stop Voice Activity Detection (VAD).
        This method halts the speech-to-text conversion process and releases any resources used.
        """
        self.vad_datasource.close()
    
    
    def forward_chunk(self, req: VadRequest) -> None:
        
        self.vad_datasource.forward_chunk(req=req)


    def init_translate(self, req: InitTranslationRequest) -> None:
        self.translate_datasource.init(
         host=req.translation_host,
         port=req.translation_port,   
        )

    def translate(self, voice: BytesIO, src: LanguageData, dest: LanguageData) -> TranslationResult:
        """
        Generate and publish translated audio from a given URL.
        This method triggers the conversion of a translated text into speech, which is made available via a URL.
        The generated audio can be used for playback, storage, or further processing.
        """
        
        res = self.translate_datasource.translate(voice=voice, src=src, dest=dest)
        t_text = None
        t_voice = None
        if len(res) > 1:
            t_text = res[1]
            t_voice = res[0]
        else:
            t_text = res[0]
       

        return TranslationResult(
            text=t_text,
            voice=t_voice,
            language_id=dest.id,
        )
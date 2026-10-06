from screens.base_screen import BaseScreen

class ChatScreen(BaseScreen):
    """Mobile AI Assistant Chat Interface Screen."""

    PROMPT_INPUT = {
        "android": "com.LightX.assistant:id/et_prompt_input",
        "ios": "accessibility_id=chat_prompt_input"
    }
    SEND_BUTTON = {
        "android": "com.LightX.assistant:id/btn_send_prompt",
        "ios": "accessibility_id=send_prompt_button"
    }
    MIC_BUTTON = {
        "android": "com.LightX.assistant:id/btn_whisper_mic",
        "ios": "accessibility_id=voice_mic_button"
    }
    CAMERA_RAG_BUTTON = {
        "android": "com.LightX.assistant:id/btn_camera_rag",
        "ios": "accessibility_id=camera_document_button"
    }
    LATEST_AI_BUBBLE = {
        "android": "com.LightX.assistant:id/tv_ai_response",
        "ios": "accessibility_id=ai_response_cell"
    }
    STREAMING_INDICATOR = {
        "android": "com.LightX.assistant:id/lottie_streaming",
        "ios": "accessibility_id=typing_indicator"
    }

    def send_prompt(self, message: str):
        self.type_text(self.PROMPT_INPUT, message)
        self.tap(self.SEND_BUTTON)

    def trigger_voice_recording(self):
        """Simulates tap-and-hold on mic for Whisper voice transcription."""
        self.tap(self.MIC_BUTTON)

    def scan_document_camera(self):
        """Triggers mobile camera OCR scan for RAG context query."""
        self.tap(self.CAMERA_RAG_BUTTON)

    def is_chat_active(self) -> bool:
        return self.is_visible(self.PROMPT_INPUT)


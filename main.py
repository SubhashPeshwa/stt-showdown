from app import dflow
import uuid

if __name__ == "__main__":

    project_id = "pmmd-25-bot"
    session_id = str(uuid.uuid4())
    audio_file_path = "./data/3010.wav"
    language_code = "en-US"

    dflow.transcribe_stream(project_id, session_id, audio_file_path, language_code)
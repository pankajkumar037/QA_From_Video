from faster_whisper import WhisperModel


def get_transcribed_text(video_file_path: str) -> str:
    model = WhisperModel("base")
    segments, info = model.transcribe(video_file_path)

    transcribed_text=""
    for segment in segments:
        transcribed_text+=segment.text
        print(segment.text)
    
    return transcribed_text
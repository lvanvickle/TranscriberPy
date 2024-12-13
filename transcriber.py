import os
import whisper
from moviepy.editor import VideoFileClip

def extract_audio(video_path, audio_path):
    '''
    Extracts audio from a video file and saves it
    as a .wav file.
    Args:
        video_path (str): Path to the input video file
        audio_path (str): Path to save the extracted audio
    '''
    print(f"Extracting audio from {video_path}...")
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)
    print(f"Audio saved to {audio_path}.")

def transcribe_audio(audio_path, model_name="base"):
    '''
    Transcribes audio to text using Whisper.
    Args:
        audio_path (str): Path to the audio file
        model_name (str): Whisper model to use ('tiny',
            'base', 'small', 'medium', 'large')
    Returns:
        str: Transcribed text
    '''
    print(f"Loading Whisper model {model_name}...")
    model = whisper.load_model(model_name)
    print(f"Transcribing audio of {audio_path}...")
    result = model.transcribe(audio_path)
    print(f"Transcription complete.")
    
    return result["text"]

def save_transcription(transcription, output_path):
    '''
    Saves transcription to a text file.
    Args:
        transcription (str): The transcribed text
        output_path (str): Path to save the transcription
    '''
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(transcription)
        print(f"Transcription saved to {output_path}.")

def process_video(video_path, output_path, model_name="base"):
    '''
    Processes the video file: extracts audio, transcribes it,
    and saves the transcription.
    Args:
        video_path (str): Path to the input video file
        output_path (str): Path to save the transcription
        model_name (str): Whisper model to use for transcription
    '''
    audio_path = "temp_audio.wav" # Temporary audio file

    try:
        # Step 1: Extract audio from video
        extract_audio(video_path, audio_path)
        # Step 2: Transcribe audio to text
        transcription = transcribe_audio(audio_path, model_name)
        # Step 3: Save the transcription
        save_transcription(transcription, output_path)
    except error as e:
        print(f"Failed due to {e}")
    finally:
        # Delete temporary audio file
        if os.path.exists(audio_path):
            os.remove(audio_path)

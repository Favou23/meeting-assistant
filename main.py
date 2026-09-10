import os 
from dotenv import load_dotenv
from openai import OpenAI



load_dotenv()
groq_base_url= "https://api.groq.com/openai/v1"
api_key = os.getenv("GROQ_API_KEY")

openai = OpenAI(base_url = groq_base_url, api_key =api_key)
transcription_model = "whisper-large-v3-turbo"
text_model = "openai/gpt-oss-120b"


def transcribe(audio_file):
    audio = open(audio_file, "rb")
    transcript  = openai.audio.transcriptions.create(
        model = transcription_model,  file=audio
    )
    transcribed_audio = transcript.text
    return transcribed_audio

def sumarize (transcribed_audio):
    system_prompt = f"""youre a meeting summarizer, you receive meeting transcript and you summarize"""
    
    user_prompt = f""" below is an extract transcript of a meeting plwase write a minutes in markdown without
    code block, inluding:
    - a summary with atendeees, loaction and dates 
    - discussion points
    - takeaways
    - action items with owners
    
    Transcriptioin:
    {transcribed_audio}"""
    messages= [
        {"role": "system", "content": system_prompt},
        {"role":"user", "content": user_prompt}
    ]

    response = openai.chat.completions.create(
        model = text_model, messages=messages
    )
    results = response.choices[0].message.content
    return results
    
    
    
def create_minutes_file(summary):

    file_path = "meeting_minutes.md"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(summary)

    return file_path
    
def process_meeting(audio_file):
    transcript =transcribe(audio_file)
    summary = sumarize(transcript)
    minutes_file = create_minutes_file(summary)
    
    return  transcript, summary, minutes_file






import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
import tempfile
import os
from fpdf import FPDF

# Functions
def convert_to_wav(uploaded_file):
    """Convert all audio files to WAV"""
    file_type = uploaded_file.name.split('.')[-1].lower()
    with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{file_type}') as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name
    
    audio = AudioSegment.from_file(tmp_path)
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as wav_file:
        audio.export(wav_file.name, format="wav")
        return wav_file.name

def transcribe_audio(file_path, language='en-US'):
    """Speech recognition process"""
    r = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = r.record(source)
        return r.recognize_google(audio_data, language=language)

def create_pdf(text):
    """PDF oluşturma (DÜZELTİLMİŞ)"""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    return bytes(pdf.output())  # Bytearray'ı bytes'a çevir

# Streamlit Interface
st.title("🎤🔊 Audio-Text Converter")

# File Upload Section
uploaded_file = st.file_uploader("Upload MP3/WAV file", type=["wav", "mp3"])
audio_path = None

if uploaded_file:
    audio_path = convert_to_wav(uploaded_file)

if audio_path:
    try:
        text = transcribe_audio(audio_path)
        edited_text = st.text_area("Edit Text", text, height=250)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.download_button(
                "📥 Download TXT",
                edited_text,
                "transcript.txt",
                "text/plain"
            )
        
        with col2:
            pdf_data = create_pdf(edited_text)
            st.download_button(
                "📄 Download PDF",
                pdf_data,  # Direkt byte veriyi kullan
                "transcript.pdf",
                "application/pdf"
            )

    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
    
    finally:
        if os.path.exists(audio_path):
            os.unlink(audio_path)

# 🎤🔊 Audio-Text Converter

This application allows users to convert audio files (MP3 or WAV formats) into text using **Streamlit** and **SpeechRecognition**. Once the audio is transcribed, users can download the generated transcript in either **TXT** or **PDF** format. The app also supports real-time transcription and offers an intuitive interface for easy file uploads and text editing.

## Audio-Text Converter Demo Introduction Video

https://github.com/user-attachments/assets/165a4bc3-d144-46d6-bc36-26c4d038d4bd

---

## 🌐 Demo

You can try out the application and see it in action by visiting the link below:

[**Audio-Text Converter Demo**](https://audio-to-text-t982.onrender.com)

⚠️ **Note**: The app goes to sleep when not actively used or if there is low traffic. 💤
---

## 📌 Project Overview

This project is a **web application** designed to convert audio files (MP3 or WAV) into **text**. After transcription, users can edit the text, and then download it in **TXT** or **PDF** format.

### Features:
- Real-time transcription of audio files
- Support for MP3 and WAV formats
- Edit transcribed text before downloading
- Export results as TXT or PDF files

---

## How It Works

### Streamlit Web App Interface:
1. **Upload Audio File**: The user uploads an MP3 or WAV audio file.
2. **Convert Audio to WAV**: If the uploaded file is not in WAV format, it is converted to WAV for transcription.
3. **Transcription**: The audio is transcribed into text using the **Google Speech API**.
4. **Text Editing**: The transcribed text is displayed in a text box, allowing the user to make changes.
5. **Download Options**: The user can download the transcript as a **TXT** or **PDF** file.

## Streamlit Web Interface
![Alt text](https://github.com/ctntrk/Audio-to-Text/blob/main/web-interface.jpg)

## After Transcript Process
![Alt text](https://github.com/ctntrk/Audio-to-Text/blob/main/transcrip.jpg)

## PDF File Output of Transcript Process
![Alt text](https://github.com/ctntrk/Audio-to-Text/blob/main/transcrip-pdf.jpg)

## TXT File Output of Transcript Process
![Alt text](https://github.com/ctntrk/Audio-to-Text/blob/main/transcrip-txt.jpg)

---

## 🔧 Technologies Used

- **Streamlit**: A Python library for building interactive web applications.
- **SpeechRecognition**: A library for converting speech into text using APIs like Google’s Speech API.
- **PyDub**: A Python library for audio file conversion and manipulation.
- **FPDF**: A library to generate PDF documents.
- **Python**: The primary programming language for this application.

### Required Dependencies:
```bash
pip install streamlit==1.24.0
pip install SpeechRecognition==3.10.0
pip install pydub==0.25.1
pip install fpdf2==2.7.4
pip install python-dotenv==1.0.0
```

---

## 🚀 Usage

1. **To run the application**, use the following command in the terminal:
   ```bash
   streamlit run audio-text.py
   ```

2. **Upload an Audio File**: The user can upload an MP3 or WAV file via the Streamlit interface.

3. **View and Edit Transcript**: After transcription, the text appears in a text box. The user can edit the text as needed.

4. **Download Options**:
   - **Download as TXT**: The user can download the transcript in **TXT** format.
   - **Download as PDF**: The user can download the transcript in **PDF** format.

---

## 🛠️ Technical Details

### Audio Conversion Process:
- **PyDub** is used to convert uploaded audio files (MP3, WAV) to a consistent **WAV** format, which is the most compatible format for speech recognition.

### Transcription:
- The app uses **SpeechRecognition** to transcribe audio into text via **Google’s Speech API**.

### PDF Generation:
- The app uses **FPDF** to convert the transcribed text into a downloadable **PDF** file.

---

## 📖 Help and Information

### Help Section
The app includes a **Help** section that provides explanations on:
- **Confidence Score**: Although not directly exposed in this version, the system's transcription accuracy can vary.
- **Quick Guide**: Basic instructions for uploading files, editing text, and downloading the transcript.
- **Technical Details**: Explanation of the libraries used and how transcription works.

### Cleaning Temporary Files:
Once the transcription process is complete, temporary files are automatically deleted to save space and keep the environment clean.

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

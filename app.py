import streamlit as st
import google.generativeai as genai
import os
import sounddevice as sd
import numpy as np 
import whisper
import scipy.io.wavfile as wav
import tempfile
import torchaudio
import torch
import sys


# ✅ Add path to Chatterbox TTS
sys.path.append("C:/Users/USER/Desktop/speech_llm_chatterbox_project/chatterbox/src")
from chatterbox.tts import ChatterboxTTS


# 🔐 Configure Gemini API
genai.configure(api_key="AIzaSyAC80P7ZxWLxv5s2qdeTc-07-Uyte5BF0E")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# 🧠 App Title & Instructions
st.title("🎤 Speech-to-Speech Chatbot using Gemini + Chatterbox TTS")
st.markdown("Click below to speak. Your voice is sent to Gemini and the response is spoken using Chatterbox TTS.")

# 🎙️ Recording & Processing
if st.button("🎙️ Start Talking"):

    duration = 5  # seconds
    fs = 16000    # Hz

    st.info("🎤 Recording... please speak clearly.")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    st.info("✅ Recording complete!")

    # Save to temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        wav.write(f.name, fs, recording)
        temp_audio_path = f.name

    st.audio(temp_audio_path, format="audio/wav")

    # 🔎 Transcribe with Whisper
    model_whisper = whisper.load_model("base")
    result = model_whisper.transcribe(temp_audio_path)
    query = result["text"]

    st.success(f"🗣 You said: {query}")
    os.remove(temp_audio_path)

    # 🤖 Gemini response
    try:
        response = model.generate_content([{"role": "user", "parts": [query]}])
        reply = response.text
        st.success(f"🤖 Gemini says: {reply}")
        print("Gemini's reply:", reply)
    except Exception:
        st.error("❌ Gemini API error or quota exceeded.")
        st.stop()

    # 🔊 TTS with Chatterbox
    try:
        # Select best device
        device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
        tts = ChatterboxTTS.from_pretrained(device=device)
        wav_tensor = tts.generate(reply)
        torchaudio.save("response.wav", wav_tensor, tts.sr)
        st.audio("response.wav", format="audio/wav")
    except Exception as e:
        st.error(f"❌ Chatterbox TTS error: {e}")

    st.success("✅ Done.")

import sys
sys.path.append("C:/Users/USER/Desktop/speech_llm_chatterbox_project/chatterbox_tts/src")

from chatterbox.tts import ChatterboxTTS
import torchaudio

model = ChatterboxTTS.from_pretrained(device="cpu")
audio = model.generate("Hello! This is a test from Chatterbox TTS.")
torchaudio.save("test_output.wav", audio, model.sr)

print("✅ Done. Check the 'test_output.wav' file in your folder.")
# cd C:\Users\USER\Desktop\speech_llm_chatterbox_project

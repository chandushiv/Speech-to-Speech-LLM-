# 🗣️ Speech-to-Speech LLM Chatbot

This project is an end-to-end **Speech-to-Speech Conversational AI** application that takes your voice input, understands it using an LLM, and responds back in human-like speech.

It combines:
- **Speech-to-Text**: Using OpenAI's `Whisper`
- **Language Understanding**: Using `Gemini` (Google Generative AI)
- **Text-to-Speech**: Using a custom `Chatterbox TTS` module
- **UI**: Built with `Streamlit` for easy interaction

---

## 🚀 Demo Features

- 🎙️ Take voice input via microphone
- 💬 Understand intent using a large language model
- 🗣️ Respond with natural speech output
- 🌐 Run entirely in the browser (via `Streamlit`)

---

## 🛠️ Tech Stack

| Layer                | Tool / Library               |
|---------------------|------------------------------|
| Speech-to-Text      | [`Whisper`](https://github.com/openai/whisper) |
| Language Model (LLM)| [`Gemini`](https://ai.google.dev/) (via `google.generativeai`) |
| Text-to-Speech      | Custom `TTS` module in `chatterbox/` |
| Audio Handling      | `sounddevice`, `torchaudio`, `numpy` |
| UI / Frontend       | `Streamlit` |
| Programming Language| Python 3.11+

---




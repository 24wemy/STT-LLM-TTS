# Voice Assistant with Flask and Hugging Face APIs

Welcome to the Voice Assistant project! This application leverages state-of-the-art machine learning models from Hugging Face to provide a seamless voice assistant experience. The assistant can transcribe speech to text, generate intelligent responses, and convert text responses back to speech, all while running on a Flask web server.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies](#technologies)
- [Setup](#setup)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Introduction

This project aims to create a sophisticated voice assistant that can interact with users through natural language. By using advanced models like Whisper for ASR (Automatic Speech Recognition), Phi-3-mini for natural language understanding and generation, and MMS-TTS for text-to-speech, the assistant can handle complex queries and respond appropriately.

## Features

- **Speech to Text**: Converts user speech into text using Whisper.
- **Intelligent Responses**: Processes the text to generate relevant answers using Phi-3-mini.
- **Text to Speech**: Converts the generated responses back to speech using MMS-TTS.
- **Interactive Web Interface**: Simple and intuitive web interface built with Flask and jQuery.

## Technologies

- **Flask**: A lightweight WSGI web application framework in Python.
- **jQuery**: A fast, small, and feature-rich JavaScript library.
- **Hugging Face API**: Utilized for ASR, LLM, and TTS functionalities.

## Setup

Follow these steps to set up and run the project locally using VSCode.

### Prerequisites

- Python 3.7+
- pip
- VSCode

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/24wemy/STT-LLM-TTS.git
    cd voice-assistant
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install dependencies**:
    ```bash
    pip install flask requests
    ```

5. **Set up environment variables**:
    Create a `.env` file in the project root and add your Hugging Face access token:
    ```env
    HUGGINGFACE_ACCESS_TOKEN=your_huggingface_access_token
    ```

6. **Run the Flask application**:
    ```bash
    python app.py
    ```

### Running the Application

1. Open the project in VSCode.
2. Open a terminal in VSCode.
3. Follow the setup steps to ensure all dependencies are installed and the virtual environment is activated.
4. Run the Flask application:
    ```bash
    python app.py
    ```

5. Access the application in your web browser at `http://127.0.0.1:5000/`.

## Usage

1. **Start Recording**: Click the "Start Recording" button to begin capturing your voice.
2. **Stop Recording**: Click the "Stop Recording" button to stop capturing your voice and send the audio for processing.
3. **View Results**: The transcribed text, response, and audio playback will be displayed on the screen.

## Acknowledgements

This project uses the following APIs from Hugging Face:
- [Whisper](https://huggingface.co/openai/whisper-small) for speech-to-text.
- [Phi-3-mini](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) for language understanding and generation.
- [MMS-TTS](https://huggingface.co/facebook/mms-tts-ind) for text-to-speech.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

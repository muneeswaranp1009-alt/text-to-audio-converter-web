# Text to Audio Converter Web

Create a simple local web application to convert text entered by the user into an MP3 audio with Python, Flask and Google Text to Speech.

This project was initially born as a simple idea to try converting text into audio.

After getting the basic Python working, I decided to take it to the next level and turn it into a local website and created the frontend based on my own project idea.

## Features
- Convert text to audio to MP3
- Simple web interface
- Flask backend
- Google Text-to-Speech conversion
- Normal and slow audio generation
- Fast play option in the frontend
- Audio player for generated audio
- Download generated MP3 files
- Recent conversion history
- Re-convert previous text
- Clear conversion history
- Loading state when generating audio
- Handling of empty input and conversion errors
- Welcome and upcoming updates modals
  
## Technologies used
- Python
- Flask
- gTTS
- HTML
- CSS
- JavaScript
  
## Project structure
text-to-audio-converter-web/
│
├── static/
│  └── voice.mp3
│
├── templates/
│  └── index.html
│
├── main.py
└── README.md

## How it works
The Flask application provides the general web routes and handles the text to audio conversion. The `/convert` endpoint receives the text and selected speed from the frontend. :chatgpt-content-reference{index="0"}
The backend uses gTTS to generate the audio and saves the generated file as `voice.mp3` inside the `static` folder. :chatgpt-content-reference{index="1"}
The frontend provides a text input area, language selection, audio speed selection, and a button to convert the entered text into audio. :chatgpt-content-reference{index="2"}
After successful conversion, the generated audio can be played directly in the browser and downloaded as an MP3 file. :chatgpt-content-reference{index="3"}

## Frontend features

The frontend was created based on my own idea to make the original text to audio concept into a simple local website.
It includes:
- Navigation bar
- Welcome popup
- Upcoming updates popup
- Text input section
- Audio speed selection
- Audio output player
- MP3 download button
- Recent conversion history
- Re-convert option
- Clear history option
- Loading indicator
The frontend also includes a recent history system that allows previously converted text to be loaded again and converted. :chatgpt-content-reference{index="4"}

## Conversion process
1. Enter text in the text area.
2. Select the audio speed.
3. Click `Convert to Audio`.
4. The frontend sends the text and speed to the Flask `/convert` endpoint.
5. Flask processes the request using gTTS.
6. The generated MP3 file is saved in the `static` folder.
7. The audio URL is returned to the frontend.
8. The generated audio is loaded into the audio player.
9. The user can listen to or download the MP3 file.
The frontend sends the conversion request using JavaScript `fetch()` and handles the returned audio URL. :chatgpt-content-reference{index="5"}

## Installation
Install the required Python packages:
pip install flask gtts

## How to run
1. Clone or download this repository.
2. Open the project folder in VS Code or another code editor.
3. Install the required packages.
4. Run the Flask application:
python main.py
5. Open the local Flask URL shown in the terminal.
6. Enter text and click `Convert to Audio`.
   
## Current limitations
- Currently configured for English text-to-speech.

- The application is designed as a local project.
- The generated audio file uses a fixed filename.
- The current history is handled on the frontend.
The frontend currently displays English as the available language and notes that regional language support is planned for future updates. :chatgpt-content-reference{index="6"}

## Future improvements
- Add Tamil, Hindi, Malayalam, and other language support
- Add database integration
- Store conversion history permanently
- Add user accounts
- Improve audio speed controls
- Support additional audio formats
- Add cloud storage
- Deploy the application online
- 
## Learning outcomes
Through this project, I practiced:
- Building a Flask web application
- Connecting a Python backend with a frontend
- Working with APIs and JSON requests
- Using gTTS for text-to-speech conversion
- Handling POST requests
- Serving generated files through Flask
- Writing HTML and CSS for a custom interface
- Using JavaScript `fetch()` for backend communication
- Managing frontend conversion history
- Turning a simple Python idea into a local web application
- 
## Project background
This project was created as a personal learning project.
The original idea was simply to try to convert text into audio using Python. After getting the basic conversion functionality working, I decided to experiment with trying turning it into a local website.
The frontend was created based on my own idea for how the text to audio tool could look and work, with additional frontend functionality added through prompting and experimentation.

## Author
Created as a personal Python and web development learning project.

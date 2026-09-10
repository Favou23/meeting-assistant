# 🎙️ Meeting Assistant

An AI-powered meeting assistant that transforms recorded meeting audio into a transcript and structured meeting minutes.

The application uses **Groq's Whisper model** for speech-to-text transcription and **GPT-OSS** for generating structured meeting summaries. The results are displayed directly in a Gradio interface, with the generated minutes available for download as a Markdown file.

## ✨ Features

* 🎧 Upload meeting audio files
* 📝 Automatic speech-to-text transcription
* 🤖 AI-generated meeting minutes
* 📌 Structured discussion points and takeaways
* ✅ Action items and owners
* 📄 Download generated meeting minutes as a Markdown file
* ⚡ Fast inference using Groq's API
* 🖥️ Simple web interface built with Gradio

## 🏗️ Architecture

```text
User
 │
 │ Upload meeting audio
 ▼
┌─────────────────┐
│   Gradio UI     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Audio Handler   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Groq Whisper    │
│ Speech-to-Text  │
└────────┬────────┘
         │
         ▼
     Transcript
         │
         ▼
┌─────────────────┐
│ Groq GPT-OSS    │
│ Summarization   │
└────────┬────────┘
         │
         ▼
      Summary
      /     \
     ▼       ▼
 Gradio UI  Markdown
             File
```

## 🧰 Tech Stack

* **Python** — Core application logic
* **Gradio** — Web interface
* **Groq API** — AI inference
* **Whisper Large V3 Turbo** — Speech-to-text
* **GPT-OSS 120B** — Meeting summarization
* **OpenAI Python SDK** — API client
* **python-dotenv** — Environment variable management

## 📂 Project Structure

```text
meeting-assistant/
│
├── main.py
├── gradio_ui.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

### `main.py`

Contains the core application logic:

* Audio transcription
* Meeting summarization
* Markdown file generation
* Meeting processing pipeline

### `gradio_ui.py`

Contains the Gradio interface and connects the UI to the meeting-processing pipeline.

This separation keeps the **application logic independent from the user interface**.

## 🔄 Application Flow

The application follows a simple processing pipeline:

```text
Audio File
    ↓
Transcription
    ↓
Meeting Transcript
    ↓
AI Summarization
    ↓
Structured Meeting Minutes
    ↓
Display + Download
```

The main orchestration function connects these stages:

```text
process_meeting()
       │
       ├── transcribe()
       │       ↓
       │   transcript
       │
       ├── summarize()
       │       ↓
       │    summary
       │
       └── create_minutes_file()
               ↓
          Markdown file
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd meeting-assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit your `.env` file to GitHub.

Make sure `.gitignore` contains:

```text
.env
venv/
__pycache__/
```

### 5. Run the application

Start the Gradio application with:

```bash
python gradio_ui.py
```

Gradio will provide a local URL similar to:

```text
http://127.0.0.1:7860
```

Open the URL in your browser.

## 🖥️ Using the Application

1. Upload a meeting recording.
2. Click **Process Meeting**.
3. The application sends the audio to Whisper for transcription.
4. The transcript is passed to the language model.
5. The language model generates structured meeting minutes.
6. The transcript and summary are displayed in the interface.
7. Download the generated Markdown meeting minutes if needed.

## 📝 Output Format

The generated meeting minutes are structured around:

* Meeting summary
* Attendees
* Location
* Date
* Discussion points
* Key takeaways
* Action items
* Action item owners

The output is generated in Markdown format so it can easily be edited, shared, or converted into other document formats.

## 🔐 Environment Variables

| Variable       | Description                                                      |
| -------------- | ---------------------------------------------------------------- |
| `GROQ_API_KEY` | API key used to access Groq's speech-to-text and language models |

## 🚧 Current Limitations

This is currently a **V1 implementation**. Some possible limitations include:

* Transcription and summarization are processed sequentially.
* Very long meetings may require transcript chunking.
* Speaker diarization is not currently implemented.
* Speaker names cannot always be identified automatically.
* Generated minutes depend on the accuracy of the transcription and language model.
* Meeting history is not persisted in a database.
* The current downloadable output is Markdown.

## 🔮 Future Improvements

Potential improvements include:

* [ ] Stream the generated summary to the UI
* [ ] Support longer meeting recordings through transcript chunking
* [ ] Add speaker diarization
* [ ] Add timestamps to transcript segments
* [ ] Extract action items into structured data
* [ ] Generate PDF and DOCX meeting minutes
* [ ] Add meeting history
* [ ] Store meetings and transcripts in a database
* [ ] Add authentication
* [ ] Add meeting title and metadata fields
* [ ] Improve prompt reliability and prevent hallucinated meeting details
* [ ] Deploy the application for public access

## 🎯 What This Project Demonstrates

This project demonstrates practical AI engineering concepts including:

* Integrating hosted AI models through APIs
* Speech-to-text pipelines
* LLM-based text processing
* Prompt engineering
* Function composition and data flow
* Separating UI from core application logic
* File generation
* Environment variable and API-key management
* Building an AI-powered application with Gradio

## 📜 License

This project is available under the MIT License.

---

Built with Python, Gradio, Groq, Whisper, and GPT-OSS.

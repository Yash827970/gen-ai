# Language Tutor (gen-ai)

An interactive language-learning web application built with **Streamlit** and **OpenAI**. Practice speaking, grammar, and translation through AI-powered exercises with instant feedback tailored for beginners.

---

## Summary

**Language Tutor** helps learners improve English (and Hindi-to-English translation) using generative AI. The app provides three guided modules:

| Module | What it does |
|--------|----------------|
| **Image Comprehension** | A random image is shown; you describe it aloud for 30 seconds. Your speech is transcribed with Whisper, compared to a GPT-4o reference description, and you receive supportive feedback on vocabulary and grammar. |
| **Grammar and Fun** | GPT generates fill-in-the-blank or multiple-choice grammar questions. Submit your answer and get AI evaluation with helpful explanations. |
| **Reading and Translation** | A Hindi sentence is generated; you translate it to English and receive feedback on accuracy and improvements. |

The app uses OpenAI models (`gpt-4o`, `gpt-3.5-turbo`, and `whisper-1`) to simulate a patient language teacher that adapts feedback for beginner learners.

---

## Prerequisites

Before you begin, make sure you have:

- **Python 3.9+** installed
- An **OpenAI API key** ([create one here](https://platform.openai.com/api-keys))
- A working **microphone** (required for Image Comprehension)
- **Internet access** (for OpenAI API calls and random images from [Picsum Photos](https://picsum.photos))

---

## Project Structure

```
gen-ai/
├── app.py                      # Main Streamlit entry point and navigation
├── requirements.txt            # Python dependencies
├── pages/
│   ├── home.py                 # Home / welcome page
│   ├── image_comprehension.py  # Image description + speech practice
│   ├── grammar_fun.py          # AI-generated grammar exercises
│   ├── reading_translation.py  # Hindi → English translation practice
│   └── soundcheck.py           # Standalone mic test script (optional)
└── README.md
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/gen-ai.git
cd gen-ai
```

### 2. Create a virtual environment (recommended)

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
pip install python-dotenv sounddevice
```

> **Note:** `python-dotenv` and `sounddevice` are used by the app but are not listed in `requirements.txt`. Install them separately as shown above.

### 4. Configure your OpenAI API key

Create a `.env` file in the project root:

```env
API_KEY=your_openai_api_key_here
```

Alternatively, set the environment variable directly:

**Windows (PowerShell):**

```powershell
$env:API_KEY = "your_openai_api_key_here"
```

**macOS / Linux:**

```bash
export API_KEY="your_openai_api_key_here"
```

> **Important:** Never commit your `.env` file or API key to version control. The `.gitignore` already excludes `.env`.

---

## How to Run the Project

1. Activate your virtual environment (if not already active).
2. Ensure your `API_KEY` is set (via `.env` or environment variable).
3. Start the Streamlit app from the project root:

```bash
streamlit run app.py
```

4. Your browser should open automatically. If not, open the URL shown in the terminal (typically `http://localhost:8501`).

5. Use the **sidebar navigation** to switch between:
   - **Home** — Overview
   - **Image Comprehension** — Describe images aloud
   - **Grammar and Fun** — Grammar exercises
   - **Reading and Translation** — Hindi-to-English translation

---

## Usage Guide

### Image Comprehension

1. Click **Start** to load a random image.
2. Click **Start Talking** when you are ready to speak.
3. Describe the image for **30 seconds** (recording starts automatically).
4. Wait while the app transcribes your speech and generates AI feedback.
5. Review the reference description and personalized improvement tips.

### Grammar and Fun

1. Click **Start / Get New Question** to generate a grammar exercise.
2. Type your answer in the text field.
3. Click **Check Answer** to receive AI feedback.

### Reading and Translation

1. Click **Start** to generate a Hindi sentence.
2. Enter your English translation.
3. Click **Verify Translation** to see what you got right and what to improve.

---

## Optional: Test Your Microphone

To verify audio recording works before using Image Comprehension, run the standalone sound check script:

```bash
python pages/soundcheck.py
```

This records 10 seconds of audio and saves it as `output.wav` in the project root.

---

## Technologies Used

- [Streamlit](https://streamlit.io/) — Web UI framework
- [OpenAI API](https://platform.openai.com/) — GPT-4o, GPT-3.5 Turbo, Whisper
- [sounddevice](https://python-sounddevice.readthedocs.io/) — Audio recording
- [python-dotenv](https://pypi.org/project/python-dotenv/) — Environment variable management
- [Picsum Photos](https://picsum.photos/) — Random practice images

---

## Troubleshooting

| Issue | Possible fix |
|-------|----------------|
| `API_KEY` errors | Confirm `.env` exists in the project root with a valid key, or set the env variable before running. |
| Microphone not working | Run `python pages/soundcheck.py` to test recording. Check OS microphone permissions. |
| `ModuleNotFoundError: sounddevice` | Run `pip install sounddevice`. |
| `ModuleNotFoundError: dotenv` | Run `pip install python-dotenv`. |
| Streamlit port in use | Run `streamlit run app.py --server.port 8502` to use a different port. |

---

## License

This project is for educational and personal language-learning use. Ensure your OpenAI API usage complies with [OpenAI's terms of service](https://openai.com/policies/terms-of-use).

# 📝 AI Text Summarizer - Modular Architecture

A production-ready NLP application that generates concise summaries from long text using Hugging Face's DistilBART model with clean modular architecture.

## 🎯 Project Overview

This application uses a local Hugging Face Transformers pipeline for abstractive text summarization. The project follows clean code principles with complete separation of concerns between UI and business logic.

## 🏗️ Architecture

### Modular Design

```
📦 Project Structure
├── summarizer.py      # Core summarization logic (model loading + inference)
├── app.py            # Gradio UI only (imports from summarizer.py)
├── requirements.txt  # Python dependencies
└── README.md        # Documentation
```

### Key Design Principles

1. **Separation of Concerns**: UI logic (`app.py`) is completely separate from business logic (`summarizer.py`)
2. **Single Responsibility**: Each module has one clear purpose
3. **Global Model Loading**: Model loads once at startup, not per request
4. **Reusability**: `summarizer.py` can be imported by other applications
5. **Maintainability**: Easy to update UI without touching model code

### Module Breakdown

#### `summarizer.py` - Core Logic
- Loads DistilBART model globally using `pipeline()`
- Provides `generate_summary()` function
- Handles input validation and truncation
- Manages model inference
- Returns summary text or error messages

#### `app.py` - UI Layer
- Imports `generate_summary` from `summarizer.py`
- Creates Gradio interface
- Handles user interactions
- Displays statistics and progress
- Manages UI state

## 🚀 Technologies Used

- **Hugging Face Transformers**: Local model inference
- **PyTorch**: Deep learning framework
- **Gradio**: Interactive web UI
- **Python 3.8+**: Programming language

## 🤖 Model Details

### DistilBART (sshleifer/distilbart-cnn-12-6)

- **Architecture**: Distilled BART (smaller, faster)
- **Size**: 1.22GB
- **Training Data**: CNN/DailyMail dataset
- **Task**: Abstractive summarization
- **Device**: CPU-optimized (device=-1)
- **Max Input**: 1500 characters (auto-truncated)

## ✨ Key Features

- ✅ **Modular architecture** - Clean separation of UI and logic
- ✅ **Local inference** - No API calls, runs completely offline
- ✅ **CPU-optimized** - Works without GPU
- ✅ **Global model loading** - Loads once, not per request
- ✅ **Adjustable summary length** - Min/max sliders
- ✅ **Real-time word counter** - Track input length
- ✅ **Summary statistics** - Compression ratio, time, word counts
- ✅ **Input validation** - Handles empty and long inputs
- ✅ **Auto-truncation** - Prevents memory issues
- ✅ **Example inputs** - Quick testing
- ✅ **Beautiful UI** - Modern gradient design
- ✅ **Progress indicators** - Visual feedback
- ✅ **Production-ready** - Error handling and user feedback

## 💻 Local Setup & Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- 2GB free disk space (for model)
- 4GB RAM minimum

### Steps to Run Locally

1. **Clone or download this repository**

```bash
git clone <your-repo-url>
cd <project-folder>
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

This will install:
- `transformers` - Hugging Face library
- `torch` - PyTorch (CPU version)
- `gradio` - Web UI framework

4. **Run the application**

```bash
python app.py
```

5. **First run notes**

- The model (1.22GB) will download automatically on first run
- Download may take 5-30 minutes depending on your internet speed
- Model is cached locally for future runs
- After download, the app will launch automatically

6. **Open your browser**

The app will open at `http://localhost:7860`

## 🌐 Deploy on Hugging Face Spaces

### Method 1: Using the Web Interface

1. **Create a new Space**
   - Go to [huggingface.co/spaces](https://huggingface.co/spaces)
   - Click "Create new Space"
   - Choose a name for your Space
   - Select **Gradio** as the SDK
   - Choose **Public** or **Private**

2. **Upload files**
   - Upload `app.py`
   - Upload `summarizer.py` (IMPORTANT!)
   - Upload `requirements.txt`
   - Upload `README.md` (optional)

3. **Wait for build**
   - Hugging Face will automatically build and deploy
   - Model will download on first build (takes 10-15 minutes)
   - Subsequent builds are faster

4. **Access your app**
   - Live at `https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME`

### Method 2: Using Git

1. **Create a new Space on Hugging Face**

2. **Clone the Space repository**

```bash
git clone https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
cd YOUR_SPACE_NAME
```

3. **Copy project files**

```bash
cp /path/to/app.py .
cp /path/to/summarizer.py .
cp /path/to/requirements.txt .
cp /path/to/README.md .
```

4. **Commit and push**

```bash
git add .
git commit -m "Initial commit: Modular text summarizer"
git push
```

5. **Your app will automatically deploy!**

## 📝 Example Input/Output

### Example 1: Eiffel Tower

**Input:**
```
The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, 
and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on 
each side. During its construction, the Eiffel Tower surpassed the Washington Monument to 
become the tallest man-made structure in the world, a title it held for 41 years until the 
Chrysler Building in New York City was finished in 1930.
```

**Output:**
```
The Eiffel Tower is 324 metres tall and the tallest structure in Paris. It surpassed 
the Washington Monument to become the tallest man-made structure in the world.
```

### Example 2: Artificial Intelligence

**Input:**
```
Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to 
the natural intelligence displayed by humans and animals. Leading AI textbooks define 
the field as the study of intelligent agents: any device that perceives its environment 
and takes actions that maximize its chance of successfully achieving its goals.
```

**Output:**
```
Artificial intelligence (AI) is intelligence demonstrated by machines. Leading AI 
textbooks define the field as the study of intelligent agents.
```

## ⚙️ How It Works

### Workflow

1. **Startup**: `summarizer.py` loads DistilBART model globally
2. **User Input**: User enters text in Gradio UI (`app.py`)
3. **Validation**: Input is validated and truncated if needed
4. **Inference**: `generate_summary()` is called with parameters
5. **Processing**: Model generates summary using transformers pipeline
6. **Response**: Summary and statistics are displayed in UI

### Code Flow

```
app.py (UI)
    ↓
    imports generate_summary()
    ↓
summarizer.py (Logic)
    ↓
    loads model globally
    ↓
    generate_summary() function
    ↓
    returns summary text
    ↓
app.py (UI)
    ↓
    displays result + statistics
```

## 🎨 UI Components

- **Input Textbox**: Multi-line text area for long documents
- **Word Counter**: Real-time character/word count
- **Length Sliders**: Control min/max summary length
- **Generate Button**: Trigger summarization
- **Clear Button**: Reset all fields
- **Output Textbox**: Display generated summary
- **Statistics Dashboard**: Shows compression ratio, time, word counts
- **Examples**: Pre-loaded sample texts for testing
- **Info Sections**: Model details and usage tips

## 🧪 Testing the Modular Structure

### Test 1: Import Test
```python
# Test that summarizer.py can be imported independently
from summarizer import generate_summary

text = "Your long text here..."
summary = generate_summary(text, min_len=30, max_len=120)
print(summary)
```

### Test 2: Empty Input
```python
from summarizer import generate_summary

summary = generate_summary("", 30, 120)
# Expected: "⚠️ Please enter some text to summarize."
```

### Test 3: Long Input
```python
from summarizer import generate_summary

long_text = "word " * 2000  # Very long text
summary = generate_summary(long_text, 30, 120)
# Expected: Truncation warning + summary
```

## 🔧 Configuration Options

### In `summarizer.py`:

```python
# Model selection
model = "sshleifer/distilbart-cnn-12-6"

# Device (CPU/GPU)
device = -1  # -1 for CPU, 0 for GPU

# Input limits
max_input_chars = 1500  # Maximum characters to process

# Summary parameters
min_length = 30  # Default minimum
max_length = 120  # Default maximum
```

### In `app.py`:

```python
# UI defaults
min_length_default = 30
max_length_default = 130

# Slider ranges
min_slider_range = (10, 100)
max_slider_range = (50, 300)
```

## 📊 Performance Notes

- **First Run**: 5-30 minutes (model download)
- **Model Loading**: 10-20 seconds (on app startup)
- **First Summary**: 5-10 seconds (model warm-up)
- **Subsequent Summaries**: 2-5 seconds
- **Memory Usage**: ~2GB RAM (model + inference)
- **Disk Space**: 1.22GB (model cache)
- **CPU Usage**: High during inference, idle otherwise

## 🐛 Troubleshooting

### Issue: Model download is slow
**Solution**: 
- This is normal, model is 1.22GB
- Download happens once, then cached
- Consider deploying to Hugging Face Spaces instead

### Issue: "Loading DistilBART model..." hangs
**Solution**: 
- Check internet connection
- Ensure 2GB free disk space
- Wait patiently, download can take 30+ minutes

### Issue: Out of memory error
**Solution**: 
- Close other applications
- Ensure 4GB+ RAM available
- Input is auto-truncated to 1500 chars

### Issue: Import error "No module named 'summarizer'"
**Solution**: 
- Ensure `summarizer.py` is in the same directory as `app.py`
- Check file names are correct

### Issue: Slow inference on CPU
**Solution**: 
- This is expected, DistilBART is optimized but still compute-intensive
- First inference is slower (model warm-up)
- Consider using GPU if available (change `device=-1` to `device=0`)

## 🎓 Learning Resources

- [Hugging Face Transformers Docs](https://huggingface.co/docs/transformers)
- [BART Paper](https://arxiv.org/abs/1910.13461)
- [Gradio Documentation](https://gradio.app/docs)
- [DistilBART Model Card](https://huggingface.co/sshleifer/distilbart-cnn-12-6)

## 📄 License

This project uses the DistilBART model from Hugging Face, which is licensed under Apache 2.0.

## 🤝 Contributing

Feel free to open issues or submit pull requests for improvements!

## 📧 Contact

For questions or feedback, please open an issue on the repository.

---

**Built with ❤️ using Hugging Face Transformers and Gradio**

**Architecture**: Modular, maintainable, production-ready

# LangChain Chatbot

An interactive AI chatbot powered by Google Gemini AI and LangChain that can answer questions on any topic.

## Features

- 🤖 Interactive conversational interface
- 💬 Powered by Google Gemini 3.5 Flash model
- 🔄 Continuous chat loop with exit commands
- 📝 Clean text-only responses (no metadata)
- ⚙️ Built with LangChain framework

## Requirements

- Python 3.7+
- Google Gemini API key

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ankitsingh9555/LANGCHAIN.git
   cd LANGCHAIN
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv myenv
   ```

3. **Activate the virtual environment:**
   - **Windows:**
     ```bash
     .\myenv\Scripts\Activate.ps1
     ```
   - **macOS/Linux:**
     ```bash
     source myenv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   Create a `.env` file in the project root and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

Run the chatbot:
```bash
python main.py
```

Then simply type your questions. Exit by typing `exit`, `quit`, or `bye`.

### Example:
```
🤖 Chatbot: Hello! Ask me anything. (Type 'exit' to quit)
--------------------------------------------------

📝 You: What is machine learning?
🤖 Chatbot: Machine Learning is a branch of Artificial Intelligence...

📝 You: exit
🤖 Chatbot: Goodbye! Have a great day!
```

## Project Structure

```
LANGCHAIN/
├── main.py              # Main chatbot script
├── requirements.txt     # Python dependencies
├── .env                # Environment variables (API keys)
├── .gitignore          # Git ignore file
├── README.md           # This file
└── myenv/              # Virtual environment
```

## API Keys

Get your free Google Gemini API key from:
https://ai.google.dev/

## Dependencies

- `langchain` - LLM framework
- `langchain-google-genai` - Google Gemini integration
- `google-generativeai` - Google AI SDK
- `python-dotenv` - Environment variable management

## License

MIT License

## Author

Created by [Your Name]

## Contributing

Feel free to fork this project and submit pull requests!

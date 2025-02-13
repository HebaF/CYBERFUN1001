# CYBERFUN 1001 TM TM TM

**CYBERFUN 1001 TM TM TM** is a corporate satire game that blends a Dungeons & Dragons 5e fantasy adventure with tongue-in-cheek, subscription-based corporate humor. In this game, you interact with a "bad" GM—a formal, corporate-minded Dungeon Master who enforces bizarre paywalls and meta-corporate policies. Use destructive commands like `DROP TABLES` to trigger system crashes and break free from oppressive subscriptions!

## Features

- **Corporate Satire Meets Fantasy:** Experience a unique twist on DnD 5e, where fantasy encounters are interlaced with corporate policies and subscription dilemmas.
- **Interactive Chat Interface:** Built with Streamlit, the game provides a simple web-based chat interface for gameplay.
- **AI-Driven GM:** Utilizes the Google Gemini (experimental) API (via the `google-generativeai` library) to generate responses in a formal, corporate tone.
- **Command Triggers:** Special commands (e.g., "hack system", "SQL injection", "DROP TABLES") are intercepted to provide humorous responses and trigger alternate endings.

## Getting Started

Follow these instructions to set up and run **CYBERFUN 1001 TM TM TM** locally.

### Prerequisites

- **Python 3.7+**
- A [Google Cloud API Key](https://cloud.google.com/) with access to the Google Generative AI (Gemini/PaLM) API.
- [pip](https://pip.pypa.io/)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/CYBERFUN1001.git
   cd CYBERFUN1001
   
2. Create a Virtual Environment (Optional but Recommended):
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    Install Dependencies:
      pip install streamlit google-generativeai python-dotenv

3.Set Up Your API Key:
Create a file named .env in the project root with the following content:
GOOGLE_API_KEY=your_actual_api_key_here

## Running the Game
To start the game, run:
  streamlit run app.py
  This command will open a browser window (or provide a URL, e.g., http://localhost:8501) where you can interact with the GM.

### How to Play
Input Your Actions: Type your action or dialogue in the input box to interact with the GM.
Forbidden Commands: Commands such as "hack system", "SQL injection", "unplug computer", or "restart computer" are intercepted. If you attempt one, the GM will respond with a humorous refusal and hint at a system crash ending.
Trigger a System Crash: Enter DROP TABLES to trigger a catastrophic, comedic system crash ending.
Enjoy the Satire: Explore the humorous blend of fantasy adventure and corporate bureaucracy!

## Contributing
Contributions are welcome! If you have ideas to expand or improve the game, feel free to fork the repository and submit pull requests. Please maintain the overall satirical tone of the project.

## License
This project is provided for educational and experimental purposes only. All trademarks and TM references (e.g., "CYBERFUN 1001 TM TM TM") are part of the satire and not intended for commercial use.

## Disclaimer
Use this project responsibly. The game uses experimental APIs and is provided as-is without warranty of any kind. Be sure to secure your API keys and follow best practices when deploying this project.

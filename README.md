OpenAI & Gemini API Lab
A Python project comparing OpenAI (gpt-4o-mini) and Google Gemini (gemini-3.8-flash) API calls side-by-side.

Setup Instructions
Clone the repository:

git clone <YOUR_REPOSITORY_URL>
cd openai-api-lab
Create and activate a virtual environment:

python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install dependencies:

pip install -r requirements.txt
Configure API Keys: Create a .env file in the root folder:

OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
Run the script:

python app.py
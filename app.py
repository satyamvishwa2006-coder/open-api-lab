import os
from dotenv import load_dotenv
from openai import OpenAI
from google import genai

# Load environment variables from .env file
load_dotenv()


# =====================================================================
# SECTION 1: OpenAI API Call
# =====================================================================
def call_openai(prompt: str):
    """
    Section 1: Calls OpenAI's Chat Completion API (e.g., gpt-4o-mini).
    """
    print("\n" + "=" * 55)
    print(" [SECTION 1] Calling OpenAI API...")
    print("=" * 55)

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key or api_key.strip() in ("", "your_openai_api_key_here"):
        print("[!] OpenAI API key not configured!")
        print("    1. Open the '.env' file in this directory.")
        print("    2. Add your key: OPENAI_API_KEY=sk-...")
        return

    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        print("\nResponse from OpenAI:")
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"\nOpenAI API Error: {e}")


# =====================================================================
# SECTION 2: Google Gemini API Call
# =====================================================================
def call_gemini(prompt: str):
    """
    Section 2: Calls Google Gemini's Generate Content API (e.g., gemini-3.8-flash).
    """
    print("\n" + "=" * 55)
    print(" [SECTION 2] Calling Google Gemini API...")
    print("=" * 55)

    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

    if not api_key or api_key.strip() in ("", "your_gemini_api_key_here"):
        print("[!] Gemini API key not configured!")
        print("    1. Get a free key at: https://aistudio.google.com/app/apikey")
        print("    2. Open the '.env' file and set: GEMINI_API_KEY=...")
        return

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )
        print("\nResponse from Gemini:")
        print(response.text)
    except Exception as e:
        print(f"\nGemini API Error: {e}")


# =====================================================================
# Main Runner
# =====================================================================
def main():
    prompt = "Explain in 2 sentences what makes artificial intelligence useful."

    print(f"Test Prompt: \"{prompt}\"")

    # Run Section 1: OpenAI
    call_openai(prompt)

    # Run Section 2: Gemini
    call_gemini(prompt)


if __name__ == "__main__":
    main()
import requests
import json
import sys

MODEL = "gemini-2.5-flash"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"


def build_prompt(info: dict) -> str:
    return f"""You are an expert technical writer. Generate a clean, professional README.md for a software project based on the following details:

Project Name: {info['project_name']}
Description: {info['description']}
Why it was built: {info['why']}
Tech Stack: {info['tech_stack']}
Key Features: {info['features']}
Installation: {info['install']}
Usage Example: {info['usage']}
Project Status: {info['status']}
License: {info['license']}

Requirements:
- Use proper Markdown formatting with headers, code blocks, and badges where appropriate
- Include these sections: title + short description, Features, Tech Stack, Installation, Usage, Contributing, License
- Add a relevant emoji to each section header
- Keep it concise but complete — no fluff
- Use a code block for the usage/install commands
- Make it look great on GitHub

Return ONLY the raw markdown. No explanation, no preamble."""


def generate_readme(info: dict, api_key: str) -> str:
    prompt = build_prompt(info)

    url = f"{API_URL}?key={api_key}"

    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    try:
        response = requests.post(url, json=payload, timeout=30)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"\n❌ API error: {e.response.status_code} — {e.response.text}")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Request failed: {e}")
        sys.exit(1)

    data = response.json()
    return data["candidates"][0]["content"]["parts"][0]["text"]
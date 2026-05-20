questions = [
    ("project_name", "What is your project name? "),
    ("description", "What does it do? (1-2 sentences) "),
    ("why", "Why did you build it / what problem does it solve? "),
    ("tech_stack", "What technologies/languages does it use? "),
    ("features", "List key features (comma-separated): "),
    ("install", "How do you install it? (e.g. pip install / npm install / clone + run) "),
    ("usage", "How do you use it? (basic example or command) "),
    ("status", "Project status? (e.g. WIP, stable, v1.0) "),
    ("license", "License? (e.g. MIT, Apache, none) "),
]

def gather_info() -> dict:
    print("\n🛠️  README Generator — answer a few questions\n")
    answers = {}
    for key, question in questions:
        answer = input(question).strip()
        answers[key] = answer if answer else "N/A"
    return answers
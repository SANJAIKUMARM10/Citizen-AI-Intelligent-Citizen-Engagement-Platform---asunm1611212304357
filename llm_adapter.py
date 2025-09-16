# A small pluggable adapter interface for LLMs.
# Replace the internals with your preferred provider.
import os
import random

def ask(prompt: str) -> str:
    # If an API key exists, you'd call the remote model here.
    # For now, we return a helpful pseudo-response.
    api_key = os.environ.get('LLM_API_KEY')
    if api_key:
        # implement provider call (OpenAI, HF, etc.)
        return 'Connected to LLM (stub).'
    sample = [
        "I can help with next steps. Which municipal department should this go to?",
        "Thanks, I note that. Here are actions you might take...",
        "Understood — I'll summarize this and recommend nearby resources."
    ]
    return random.choice(sample)

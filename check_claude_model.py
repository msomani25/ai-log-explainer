import os
import anthropic

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    print("Claude API key not found. Set ANTHROPIC_API_KEY in your environment.")
    exit()

client = anthropic.Anthropic(api_key=api_key)

models = client.models.list()

print("Available Claude models for your account:\n")
for m in models.data:
    print(m.id)  # <-- use .id instead of .name
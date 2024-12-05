#! /home/zlj09/apps/python3_venv/bin/python3
from openai import OpenAI

with open("./GPT_SECRET_KEY.txt", "r") as fp:
  openrouter_api_key = fp.read().rstrip()
print(f"openrouter_api_key = {openrouter_api_key}")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=openrouter_api_key,
)

completion = client.chat.completions.create(
  # extra_headers={
  #   "HTTP-Referer": $YOUR_SITE_URL, // Optional, for including your app on openrouter.ai rankings.
  #   "X-Title": $YOUR_APP_NAME, // Optional. Shows in rankings on openrouter.ai.
  # },
  model="openai/gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
print(completion.choices[0].message.content)

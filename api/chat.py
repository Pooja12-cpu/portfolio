# api/chat.py
import os
import json
from openai import OpenAI

def handler(request):
    if request.method != "POST":
        return {"statusCode": 405, "body": "Method not allowed"}

    body = json.loads(request.body)
    user_message = body.get("message", "")

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant on Pooja Thakur's portfolio website."},
            {"role": "user", "content": user_message},
        ]
    )

    reply = response.choices[0].message.content.strip()
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"reply": reply})
    }

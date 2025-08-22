import requests
from django.conf import settings
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

OPENROUTER_API_KEY = getattr(settings, "OPENROUTER_API_KEY", "").strip()

def load_summarizer():
    if OPENROUTER_API_KEY:
        # Use OpenRouter mode (dummy summarizer token)
        return ("openrouter", None)
    else:
        model_name = "sshleifer/distilbart-cnn-12-6"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
        return (summarizer, tokenizer)

def chunk_text_by_tokens(text, tokenizer, max_tokens=900):
    tokens = tokenizer.encode(text, truncation=False)
    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i:i + max_tokens]
        yield tokenizer.decode(chunk_tokens, skip_special_tokens=True)

def chunk_text(text, chunk_size=4000):
    for i in range(0, len(text), chunk_size):
        yield text[i:i+chunk_size]

def summarize_with_openrouter(text, max_tokens=250):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant. Summarize the following legal document concisely."
            },
            {
                "role": "user",
                "content": text
            }
        ],
        "max_tokens": max_tokens
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"].strip()

def summarize_text(summarizer, tokenizer, text, max_length=250, min_length=100):
    if OPENROUTER_API_KEY and summarizer == "openrouter":
        summaries = []
        for chunk in chunk_text(text, chunk_size=4000):
            summary_chunk = summarize_with_openrouter(chunk, max_tokens=max_length)
            summaries.append(summary_chunk)
        return " ".join(summaries)
    else:
        summaries = []
        for chunk in chunk_text_by_tokens(text, tokenizer, max_tokens=900):
            result = summarizer(
                chunk,
                max_length=max_length,
                min_length=min_length,
                truncation=True,
                do_sample=False
            )[0]['summary_text']
            summaries.append(result.strip())
        return " ".join(summaries)

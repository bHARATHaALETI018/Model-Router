Run Locally (Smoke Test)
```bash
export OPENAI_API_KEY=xxx
uvicorn app.main:app --reload
```

Test:
```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Say hello like a pirate",
    "model": "gpt-4o"
  }'

```
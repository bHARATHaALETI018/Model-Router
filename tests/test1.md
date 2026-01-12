config.yaml
```bash
mkdir -p config
vi config/config.yaml
```
config contents:
```yaml
default_model: gpt-4o
models:
  gpt-4o:
    provider: openai
```


Run Locally (Smoke Test)
```bash
export OPENAI_API_KEY=xxx
export ROUTER_CONFIG_PATH=$(pwd)/config/config.yaml

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
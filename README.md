# Model-Router

## Overview

**Model-Router** is a lightweight, extensible service that provides a **unified API for routing requests to multiple Large Language Model (LLM) providers at runtime**.

It acts as an abstraction layer between applications or agents and underlying LLM providers such as OpenAI, Anthropic, Gemini, etc., enabling:

* Runtime model switching
* Provider-agnostic interfaces
* Clean separation between **AI orchestration** and **model execution**
* Easy extensibility for new providers

This service is a foundational component in the AI platform architecture and is designed to integrate seamlessly with the **Agent Runtime**.

---

## Key Responsibilities

* Route generation requests to the selected LLM provider
* Normalize request and response formats
* Handle provider configuration and credentials
* Expose a single, stable HTTP API for text generation

---

## Architecture Position

```
[ Agent Runtime / Applications ]
              |
              v
        [ Model-Router ]
              |
    -------------------------
    |        |        |
 [OpenAI] [Claude] [Gemini]
```

Model-Router **does not manage memory, agents, or workflows**.
It strictly focuses on **model invocation**.

---

## Features

* Provider-based routing (`openai`, future: `anthropic`, `gemini`)
* Async-first design
* FastAPI-based HTTP service
* Clean provider registry pattern
* Environment-based secret management
* Easy to extend with new models/providers

---

## API Contract

### `POST /generate`

#### Request

```sh
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Say hello like a pirate",
    "model": "gpt-4o"
  }'
```

#### Response

```json
{
  "text": "............",
  "model": "gpt-5-nano",
  "usage": {
    ....
  }
}
```

---

## Environment Variables

| Variable         | Description                 |
| ---------------- | --------------------------- |
| `OPENAI_API_KEY` | API key for OpenAI provider |
| `ROUTER_CONFIG_PATH` | /app/config/config.yaml |

Set before running:

```bash
export OPENAI_API_KEY="your_api_key_here"
export ROUTER_CONFIG_PATH=$(pwd)/app/config/config.yaml
```

---

## Running Locally

### 1. Create virtual environment

```bash
python -m venv venv
# Activate venv
source venv/Scripts/activate # For Linux
# For Windows
.\venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the server

```bash
uvicorn app.main:app --reload --port 8000
```

Server will be available at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Provider Registry Pattern

All providers must implement the base interface:

```python
class BaseProvider(ABC):

    @abstractmethod
    async def generate(self, prompt: str, model: str, parameters: dict):
        pass

```

Providers are registered centrally:

```python
class OpenAIProvider(BaseProvider):
  ....

def get_provider(name: str):
    if name == "openai":
        return OpenAIProvider()
    raise ValueError(f"Unknown provider: {name}")
```

This allows new providers to be added without changing API logic.

---

## Non-Goals

Model-Router intentionally does **not** handle:

* Conversation state
* Memory or persistence
* Tool execution
* Agent logic or workflows

These concerns belong to the **Agent Runtime**.

---

## Future Enhancements

* Add Anthropic / Gemini providers
* Streaming responses
* Rate limiting
* Observability (metrics, tracing)
* Model capability metadata

---
# Model Router

## Getting-Started

### Step-1 
Create a virtual environment

```bash
python -m venv venv
# Activate venv
source venv/Scripts/activate # For Linux
# For Windows
.\venv\Scripts\activate
```
### Step-2
Install the dependencies

```bash
pip install -r requirements.txt
```
### Step-3
Run the FastAPI application

```bash
uvicorn app.main:app --reload
```
### Step-4
Test the server from the terminal

```
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Explain Terraform like I am 15",
    "model": "gpt-5-nano"
  }'

```
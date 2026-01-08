from pydantic import BaseModel

class GenerateRequest(BaseModel):
    prompt: str
    model: str

class GenerateResponse(BaseModel):
    provider: str
    model: str
    output: str

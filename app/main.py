from fastapi import FastAPI, HTTPException
from app.schemas import GenerateRequest, GenerateResponse
from app.config import DEFAULT_PROVIDER

from app.providers import openai as openai_provider
# from app.providers import azure_openai as azure_provider

app = FastAPI(title="Model Router")

@app.post("/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    try:
        output = openai_provider.generate(req.prompt, req.model)
        provider = "openai"
        # if DEFAULT_PROVIDER == "azure":
        #     output = azure_provider.generate(req.prompt, req.model)
        #     provider = "azure-openai"
        # else:
        #     output = openai_provider.generate(req.prompt, req.model)
        #     provider = "openai"
    
        return GenerateResponse(
            provider=provider,
            model=req.model,
            output=output
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

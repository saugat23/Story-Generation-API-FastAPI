from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import setting
from routers import story,job

app = FastAPI(
    title="Adventure/Story game API",
    description="API to create stories using OpenAI LLM",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=setting.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(story.router, prefix=setting.API_PREFIX)
app.include_router(job.router, prefix=setting.API_PREFIX)

if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
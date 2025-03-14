from fastapi import FastAPI
from app.routes import person, project, ticket
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include user-related routes
app.include_router(person.router)
app.include_router(project.router)
app.include_router(ticket.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the API"}

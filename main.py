from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import random
from insults import insults
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

app = FastAPI()

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET"],
	allow_headers=[""],
    max_age=3600,
)


class DetailedInsult(BaseModel):
    season: int
    episode: int
    character: str
    insult: str

@app.get("/")
def read_root():
    return FileResponse("static/index.html")

@app.get("/api/insults", response_model=DetailedInsult)
@limiter.limit("100/hour")
async def get_random_insult(request: Request):
    all_insults = insults["insults"]
    if not all_insults:
        raise HTTPException(status_code=404, detail="No insults available")
    random_insult = random.choice(all_insults)
    return DetailedInsult(
        season=random_insult["season"],
        episode=random_insult["episode"],
        character=random_insult["character"],
        insult=random_insult["insult"]
    )

@app.get("/api/insults/season/{season}", response_model=DetailedInsult)
@limiter.limit("100/hour")
async def get_insult_by_season(request: Request, season: int):
    season_insults = [insult for insult in insults["insults"] if insult["season"] == season]
    if not season_insults:
        raise HTTPException(status_code=404, detail=f"No insults available for season {season}")
    random_insult = random.choice(season_insults)
    return DetailedInsult(
        season=random_insult["season"],
        episode=random_insult["episode"],
        character=random_insult["character"],
        insult=random_insult["insult"]
    )

@app.get("/api/insults/season/{season}/episode/{episode}", response_model=DetailedInsult)
@limiter.limit("100/hour")
async def get_insult_by_season_and_episode(request: Request, season: int, episode: int):
    episode_insults = [
        insult for insult in insults["insults"]
        if insult["season"] == season and insult["episode"] == episode
    ]
    if not episode_insults:
        raise HTTPException(
            status_code=404,
            detail=f"No insults available for season {season}, episode {episode}"
        )
    random_insult = random.choice(episode_insults)
    return DetailedInsult(
        season=random_insult["season"],
        episode=random_insult["episode"],
        character=random_insult["character"],
        insult=random_insult["insult"]
    )

@app.get("/api/insults/character/{character}", response_model=DetailedInsult)
@limiter.limit("100/hour")
async def get_insult_by_character(request: Request, character: str):
    character_insults = [insult for insult in insults["insults"] if (insult["character"]).lower() == character]
    if not character_insults:
        raise HTTPException(status_code=404, detail=f"No insults available for character {(character).title()}")
    random_insult = random.choice(character_insults)
    return DetailedInsult(
        season=random_insult["season"],
        episode=random_insult["episode"],
        character=random_insult["character"],
        insult=random_insult["insult"]
    )

@app.get("/api/insults/season/{season}/character/{character}", response_model=DetailedInsult)
@limiter.limit("100/hour")
async def get_insult_by_season_and_character(request: Request, season: int, character: str):
    season_character_insults = [
        insult for insult in insults["insults"]
        if insult["season"] == season and (insult["character"]).lower() == character
    ]
    if not season_character_insults:
        raise HTTPException(
            status_code=404,
            detail=f"No insults available for season {season} and character {(character).title()}"
        )
    random_insult = random.choice(season_character_insults)
    return DetailedInsult(
        season=random_insult["season"],
        episode=random_insult["episode"],
        character=random_insult["character"],
        insult=random_insult["insult"]
    )

@app.get("/api/insults/season/{season}/episode/{episode}/character/{character}", response_model=DetailedInsult)
@limiter.limit("100/hour")
async def get_insult_by_season_episode_and_character(request: Request, season: int, episode: int, character: str):
    episode_character_insults = [
        insult for insult in insults["insults"]
        if insult["season"] == season and insult["episode"] == episode and (insult["character"]).lower() == character
    ]
    if not episode_character_insults:
        raise HTTPException(
            status_code=404,
            detail=f"No insults available for season {season}, episode {episode}, and character {(character).title()}"
        )
    random_insult = random.choice(episode_character_insults)
    return DetailedInsult(
        season=random_insult["season"],
        episode=random_insult["episode"],
        character=random_insult["character"],
        insult=random_insult["insult"]
    )

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import random
from insults import insults


silicon_valley_insults = FastAPI()
silicon_valley_insults.mount("/static", StaticFiles(directory="static"), name="static")


class DetailedInsult(BaseModel):
    season: int
    episode: int
    character: str
    insult: str

@silicon_valley_insults.get("/")
def read_root():
    return FileResponse("static/index.html")

@silicon_valley_insults.get("/api/insults", response_model=DetailedInsult)
async def get_random_insult():
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

@silicon_valley_insults.get("/api/insults/season/{season}", response_model=DetailedInsult)
async def get_insult_by_season(season: int):
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

@silicon_valley_insults.get("/api/insults/season/{season}/episode/{episode}", response_model=DetailedInsult)
async def get_insult_by_season_and_episode(season: int, episode: int):
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

@silicon_valley_insults.get("/api/insults/character/{character}", response_model=DetailedInsult)
async def get_insult_by_character(character: str):
    character_insults = [insult for insult in insults["insults"] if insult["character"] == character]
    if not character_insults:
        raise HTTPException(status_code=404, detail=f"No insults available for character {character}")
    random_insult = random.choice(character_insults)
    return DetailedInsult(
        season=random_insult["season"],
        episode=random_insult["episode"],
        character=random_insult["character"],
        insult=random_insult["insult"]
    )

@silicon_valley_insults.get("/api/insults/season/{season}/character/{character}", response_model=DetailedInsult)
async def get_insult_by_season_and_character(season: int, character: str):
    season_character_insults = [
        insult for insult in insults["insults"]
        if insult["season"] == season and insult["character"] == character
    ]
    if not season_character_insults:
        raise HTTPException(
            status_code=404,
            detail=f"No insults available for season {season} and character {character}"
        )
    random_insult = random.choice(season_character_insults)
    return DetailedInsult(
        season=random_insult["season"],
        episode=random_insult["episode"],
        character=random_insult["character"],
        insult=random_insult["insult"]
    )

@silicon_valley_insults.get("/api/insults/season/{season}/episode/{episode}/character/{character}", response_model=DetailedInsult)
async def get_insult_by_season_episode_and_character(season: int, episode: int, character: str):
    episode_character_insults = [
        insult for insult in insults["insults"]
        if insult["season"] == season and insult["episode"] == episode and insult["character"] == character
    ]
    if not episode_character_insults:
        raise HTTPException(
            status_code=404,
            detail=f"No insults available for season {season}, episode {episode}, and character {character}"
        )
    random_insult = random.choice(episode_character_insults)
    return DetailedInsult(
        season=random_insult["season"],
        episode=random_insult["episode"],
        character=random_insult["character"],
        insult=random_insult["insult"]
    )

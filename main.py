from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import random


bachmanity_api = FastAPI()

class Insult(BaseModel):
    insult: str

insults = {
    "s1": [
        "s1 insult 1",
        "s1 insult 2",
        "s1 insult 3",
    ],
    "s2": [
        "s2 insult 1",
        "s2 insult 2",
        "s2 insult 3",
    ],
}

@bachmanity_api.get("/")
def read_root():
    return FileResponse("static/index.html")

@bachmanity_api.get('/insult', response_model=Insult)
async def get_random_insult():
    all_insults = []
    for season in insults:
        insult_list = insults[season]
        for insult in insult_list:
            all_insults.append(insult)
    if not all_insults:
        raise HTTPException(status_code=404, detail="No insults available")
    random_insult = random.choice(all_insults)
    return {"insult": random_insult}

@bachmanity_api.get('/insult/{season}', response_model=Insult)
async def get_season_insult(season: str):
    season_insults = insults.get(season, [])
    if not season_insults:
         raise HTTPException(status_code=404, detail=f"No {season} insults available")
    random_insult = random.choice(season_insults)
    return {"insult": random_insult}

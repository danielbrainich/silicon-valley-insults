from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import random
from insults import insults


silicon_valley_insults = FastAPI()

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
        season=random_insult["Season"],
        episode=random_insult["Episode"],
        character=random_insult["Character"],
        insult=random_insult["Insult"]
    )

# @silicon_valley_insults.get("/api/insults", response_model=Insult)
# async def get_random_insult():
#     all_insults = []
#     for season in insults:
#         insult_list = insults[season]
#         for insult in insult_list:
#             all_insults.append(insult)
#     if not all_insults:
#         raise HTTPException(status_code=404, detail="No insults available")
#     random_insult = random.choice(all_insults)
#     return {"insult": random_insult}

# @silicon_valley_insults.get('/insult/{season}', response_model=Insult)
# async def get_season_insult(season: str):
#     season_insults = insults.get(season, [])
#     if not season_insults:
#          raise HTTPException(status_code=404, detail=f"No {season} insults available")
#     random_insult = random.choice(season_insults)
#     return {"insult": random_insult}

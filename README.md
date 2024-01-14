# Silicon Valley Insults API

## Introduction
Silicon Valley Insults API is a RESTful service that provides a collection of insults from the HBO series "Silicon Valley". It offers multiple endpoints to retrieve insults based on character, season, and specific episodes.

## Quick Start
To use the API, send HTTP GET requests to the available endpoints. The responses are in JSON format.

## Sample Request

fetch("https://www.siliconvalleyinsults.com/api/insults")

## Sample Response

{
    "season": 1,
    "episode": 2,
    "character": "Gavin",
    "insult": "I hate Richard Hendricks, that little Pied Piper prick."
}

## API Endpoints

### Get a Random Insult

Method: GET
Path: /api/insults

### Get a Random Insult by Character

Method: GET

Path: /api/insults/character/{character}

Parameters: {character} is a string representing the first name of the character you want an insult from.

### Get a Random Insult by Season

Method: GET

Path: /api/insults/season/{season}

Parameters: {season} is an integer representing the season you want an insult from.

### Get a Random Insult by Season and Character

Method: GET

Path: /api/insults/season/{season}/character/{character}

Parameters:

{season} is an integer representing the season.

{character} is a string representing the character.

### Get a Random Insult by Season and Episode

Method: GET

Path: /api/insults/season/{season}/episode/{episode}

Parameters:

{season} is an integer representing the season.

{episode} is an integer representing the episode.

### Get a Random Insult by Season, Episode, and Character

Method: GET

Path: /api/insults/season/{season}/episode/{episode}/character/{character}

Parameters:

{season} is an integer representing the season.

{episode} is an integer representing the episode.

{character} is a string representing the character.

## Errors and Exceptions

### Insult Does Not Exist

The insult you request may not exist. For example, you may request an insult from Jared from Season 1 Episode 3 when no such insult exists in the database. In this case, you will receive the following exception:

{
    "detail": "No insults available for season 1, episode 3, and character Jared"
}

## Development
I built this API using FastAPI, a framework for building APIs with Python.

## Credits
Designed and coded by me, Daniel Brainich.

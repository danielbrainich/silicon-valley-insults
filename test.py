import requests

response = requests.get("http://127.0.0.1:8000/api/insults")
print(response.json)
print(response.content)
print(response.status_code)
print(response.headers)

# terminal command below runs my API on a local server
# uvicorn main:silicon_valley_insults --reload


# build my docker image
# docker build -t silicon_valley_insults .

# run my image as a docker container
# docker run -p 8000:8000 silicon_valley_insults

# to stop my running container
# docker stop bachmanity_api

# to start back up from it's stopped state without needing to rebuild image
# docker start bachmanity_api

# you will need to rebuild the container each time you make changes and then run that image like this
# docker build -t bachmanity_api .
# docker run -p 8000:8000 bachmanity_api

# you can run your app in a development environment with the --reload option so that the code reloads whenever changes are detected like this
# uvicorn fastapi:silicon_valley_insults --host 0.0.0.0 --port 8000 --reload


# heroku command line steps

# gut push origin main
# git push heroku main

                # <header>
                #     <nav class="navbar navbar-expand-lg pt-4 pb-4 sticky-top">
                #         <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                #             <span class="navbar-toggler-icon"></span>
                #         </button>
                #         <div class="collapse navbar-collapse" id="navbarSupportedContent">
                #             <ul class="navbar-nav mx-auto mb-2 mb-lg-0">
                #                 <li class="nav-item"><a class="nav-link px-4" href="#endpoints">Endpoints</a></li>
                #                 <li class="nav-item"><a class="nav-link px-4" href="#about">About</a></li>
                #                 <li class="nav-item"><a class="nav-link px-4" href="#info">Info</a></li>
                #             </ul>
                #         </div>
                #     </nav>
                # </header>
                    # <!-- <div>
                    #     <h3>Endpoints</h3>
                    #     <ul class="no-bullet">
                    #         <li><a href="#one">Get a random insult</a></li>
                    #         <li><a href="#two">Get a random insult by season</a></li>
                    #         <li><a href="#three">Get a random insult by character</a></li>
                    #         <li><a href="#four">Get a random insult by season and by character</a></li>
                    #         <li><a href="#five">Get a random insult by season and by episode</a></li>
                    #         <li><a href="#six">Get a random insult by season and by episode and by character</a></li>
                    #     </ul>
                    # </div> -->

from connection.secrets import refresh_token, base_64
import requests

def refresh():
    query = "https://accounts.spotify.com/api/token"

    response = requests.post(query,
                             data={"grant_type": "refresh_token", "refresh_token": refresh_token},
                             headers={"Authorization": "Basic " + base_64})

    response_json = response.json()

    return response_json["access_token"]

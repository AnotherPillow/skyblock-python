from typing_extensions import Literal
import requests
from .types.ServerInfo import *

_server_id_dictionary = {
    'skywars': 7,
    'economy': 6,
    'survival': 4,
}

def getPlayers(server: Literal["skywars", "economy", "survival"]) -> ServerInfo:
    id = _server_id_dictionary[server]
    data = requests.post(f'https://skyblock.net/index.php?server-status/{id}/query',
        headers={
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept": "application/json, text/javascript, */*; q=0.01",
        },
        data="_xfRequestUri=%2F&_xfNoRedirect=1&_xfResponseType=json"
    ).json()
    
    status = data['serverStatus']
    return ServerInfo(status['online'], status['players_online'], status['max_players'], status['player_list'])
    

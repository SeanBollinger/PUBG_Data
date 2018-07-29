import requests, sys, json

match_ids, players, telemetry, key = [], 'ItsSharkey', [], #your pubg api key here as string
url = "https://api.pubg.com/shards/pc-na/players?filter[playerNames]=%s" %players
headers = {
    'accept': 'application/vnd.api+json',
    'Authorization': 'Bearer %s' %key
}

def main():
    """Main entry point for the script. First we're just going to get the telemetry objects. further develepment todos will be to check the DB for existing matches, and ship new matches up to cloudant"""
    matches = get_match_ids_by_playername(players)
    get_telemetry(matches)
    print(telemetry)
    pass

def get_match_ids_by_playername(players):
    '''Get match ID's for recently played games by playername or multiple player names in a list'''
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    lis = json_data['data'][0]['relationships']['matches']['data']
    for i in lis:
        match_ids.append(i['id'])
    return match_ids

'''
def check_existing(match_ids):
    return match_ids
'''

def get_telemetry(match_ids):
    '''get telemetry data object'''
    h = {'accept': 'application/vnd.api+json'}
    telem = []
    for i in match_ids:
        url_2 = "https://api.pubg.com/shards/pc-na/matches/%s" %i
        response = requests.get(url_2, headers = h)
        json_data = json.loads(response.text)
        telemetry.append(json_data)
    return telemetry

if __name__ == '__main__':
    sys.exit(main())


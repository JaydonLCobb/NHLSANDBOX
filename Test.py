import requests
import json
# import pandas as pd 
#url = "https://api.nhle.com/stats/rest/en/shiftcharts?cayenneExp=gameId=2023020007"
url  = "https://api-web.nhle.com/v1/gamecenter/2024010030/play-by-play"
# url = "https://api-web.nhle.com/v1/schedule/now"

response = requests.get(url)


if response.status_code == 200:
    data = response.json()  
    pretty_data = json.dumps(data, indent=4) 
   # print(pretty_data)

   # for key in data:
     #   print(key)


   # key_to_print = "plays"  

    # print plays (based on key_to_print - for now it's plays)
    # if key_to_print in data:
    #    print(json.dumps(data[key_to_print], indent=4))  
        

    # goals by id
    # for play in data['plays']:
    #     if 'details' in play and 'assist1PlayerId' in play['details'] and play['details']['assist1PlayerId'] == 8483429:
    #         print(json.dumps(play, indent=4))

    casey = 8483429
    counter = 0
    for play in data['plays']:
        if 'details' in play:
         if casey in play['details'].values():
           counter+=1
        #   print(json.dumps(play, indent=4))
        #   print(counter)




    # get jack hughes id
    # last_name_to_search = "Hughes"  
    # search_id = 0
    # njUrl = "https://api-web.nhle.com/v1/roster/NJD/current"
    # response = requests.get(njUrl)
    # data = response.json()  
    # pretty_data = json.dumps(data, indent=4)
    # print(pretty_data)
    # for rosterSpot in data['forwards']: #change here based on position
    #     if 'lastName' in rosterSpot and 'default' in rosterSpot['lastName'] and rosterSpot['lastName']['default'] == last_name_to_search:
    #         id = rosterSpot['id']
    #     ##   print(json.dumps(rosterSpot, indent=4))  
    #         print(id)


def get_player_id(last_name_to_search, position, team):
    url = "https://api-web.nhle.com/v1/roster/{team}/current" 
    url = url.format(team=team)                        
    response = requests.get(url)
    data = response.json()  
    pretty_data = json.dumps(data, indent=4)
    #print(pretty_data)
    for rosterSpot in data[position]: #change here based on position
        if 'lastName' in rosterSpot and 'default' in rosterSpot['lastName'] and rosterSpot['lastName']['default'] == last_name_to_search:
            id = rosterSpot['id']
        #   print(json.dumps(rosterSpot, indent=4))  
        #    print(rosterSpot['firstName'], rosterSpot['lastName'], id)
            # return id

def get_player_id2(last_name_to_search, team):
    url = "https://api-web.nhle.com/v1/roster/{team}/current" 
    url = url.format(team=team)                        
    response = requests.get(url)
    data = response.json()  

    positions = ['forwards', 'defensemen', 'goalies'] 

    for pos in positions:
        for rosterSpot in data[pos]:
            if 'lastName' in rosterSpot and 'default' in rosterSpot['lastName'] and rosterSpot['lastName']['default'] == last_name_to_search:
                id = rosterSpot['id']
                # print(rosterSpot['firstName'], rosterSpot['lastName'], id)
                return id
            

def get_team_schedule(team):
    url = "https://api-web.nhle.com/v1/club-schedule-season/{team}/now" 
    url = url.format(team=team)                        
    response = requests.get(url)
    data = response.json()  
    pretty_data = json.dumps(data, indent=4)
    print(pretty_data)

 
def get_top_players():
    url = "https://api.nhle.com/stats/rest/en/leaders/skaters/points?cayenneExp=season=20232024"
    response = requests.get(url)
    data = response.json()
    pretty_data = json.dumps(data, indent=4)
    print(pretty_data)


def get_shift_charts():
    url = "https://api.nhle.com/stats/rest/en/shiftcharts?cayenneExp=gameId=2021020001"
    response = requests.get(url)
    data = response.json()
    pretty_data = json.dumps(data, indent=4)
    print(pretty_data)
   

def main():
    # get_player_id("Hughes", "forwards", "NJD")
    # get_player_id("Hughes", "defensemen", "VAN")
    # get_player_id("Brennan", "goalies", "NJD")

    # print(get_player_id2("Hughes", "NJD"))
    # print(get_player_id2("Hughes", "VAN"))
    # print(get_player_id2("Brennan", "NJD"))
    # get_team_schedule("NJD")
   # get_top_players()
    get_shift_charts()
    
if __name__ == "__main__":
    main()
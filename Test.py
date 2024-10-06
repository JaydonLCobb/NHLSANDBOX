import requests
import json
from datetime import date, datetime, timedelta
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
def get_api_response(url):
    """
    Fetches data from the given API URL and returns the response as a dictionary.
    
    Args:
        url (str): The URL of the API endpoint.
    
    Returns:
        dict: The JSON response from the API, or an error message if the request fails.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Error: Received status code {response.status_code}"}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}


def get_all_keys(data):
    """
    Recursively fetches all keys from the API response, including nested keys.
    
    Args:
        data (dict or list): The API response data, either as a dictionary or list.
    
    Returns:
        set: A set of all keys in the API response, including nested keys.
    """
    keys = set()
    
    if isinstance(data, dict):
        for key in data:
            keys.add(key)
            keys.update(get_all_keys(data[key]))  # Recursively get keys from nested structures
    elif isinstance(data, list):
        for item in data:
            keys.update(get_all_keys(item))  # Recursively get keys from each item in the list

    return keys


def get_weekly_games():
    url = "https://api-web.nhle.com/v1/schedule/now"
    response=requests.get(url)
    data = response.json()

   # print(get_api_sections(url))
   # print(get_api_sections2(url))
    keys = get_all_keys(url)
    

    # for game in data:
    #     if datetime.strptime(game['nextStartDate'], '%Y-%m-%d').date() >= date.today() and datetime.strptime(game['nextStartDate'], '%Y-%m-%d').date() <= date.today()+7:
    #         return data
    
    #pretty_data = json.dumps(data, indent=4)
    #return pretty_data

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

def get_api_sections(url):
    """
    Fetches data from the given API URL and returns the top-level keys (sections) in the response.
    
    Args:
        url (str): The URL of the API endpoint.
    
    Returns:
        list: A list of top-level keys in the API response, or an error message if the request fails.
    """
    try:
        # Step 1: Make the API Request
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Step 2: Parse the Response
            data = response.json()
            
            # Step 3: List all the sections (keys) in the top-level dictionary
            sections = list(data.keys())
            return sections
        else:
            return f"Error: Received status code {response.status_code}"

    except Exception as e:
        return f"An error occurred: {e}"


def get_api_sections2(url):
    """
    Fetches data from the given API URL and returns the top-level keys (sections) in the response.
    
    Args:
        url (str): The URL of the API endpoint.
    
    Returns:
        dict: A dictionary containing the top-level keys and their corresponding values.
    """
    try:
        # Step 1: Make the API Request
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Step 2: Parse the Response
            data = response.json()
            
            # Step 3: Return the keys and their values
            return {key: data[key] for key in data.keys()}
        else:
            return {"error": f"Error: Received status code {response.status_code}"}

    except Exception as e:
        return {"error": f"An error occurred: {e}"}

def get_weekly_games2():
    url = "https://api-web.nhle.com/v1/schedule/now"
    data = get_api_response(url)

    if isinstance(data, dict):
        # Set the start to today and end to 7 days from today
        today = datetime.now()
        start_of_week = today  # Today
        end_of_week = today + timedelta(days=7)  # 7 days from today

        # List to store games scheduled for the next week
        games_this_week = []

        # Check for the nextStartDate
        if 'nextStartDate' in data:
            next_start_date_str = data['nextStartDate']
            next_start_date = datetime.strptime(next_start_date_str, '%Y-%m-%d')
            hometeam = data['homeTeam']
            # Check if the game falls within the next week
            if start_of_week <= next_start_date <= end_of_week:
                games_this_week.append({'nextStartDate': next_start_date_str})
                games_this_week.append({'homeTeam': hometeam})

        # Print out the games scheduled for the next week
        if games_this_week:
            print("Games scheduled for the next week:")
            print(json.dumps(games_this_week, indent=4))
        else:
            print("No games scheduled for the next week.")
    else:
        print(data)  # Print the error message if applicable

def main():
    print(get_weekly_games2())
    # get_player_id("Hughes", "forwards", "NJD")
    # get_player_id("Hughes", "defensemen", "VAN")
    # get_player_id("Brennan", "goalies", "NJD")

    # print(get_player_id2("Hughes", "NJD"))
    # print(get_player_id2("Hughes", "VAN"))
    # print(get_player_id2("Brennan", "NJD"))
    # get_team_schedule("NJD")
    # get_top_players()
    # get_shift_charts()
    
if __name__ == "__main__":
    main()
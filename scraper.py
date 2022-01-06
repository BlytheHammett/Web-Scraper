from bs4 import BeautifulSoup
import requests
import csv

with open('stats.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    fieldnames = ['Name', 'Goals', 'Shots', 'Shooting accuracy %', 'Assists', 'Passes per match', 'Big Chances Created', 'Through balls', 'Accurate long balls', 'Tackle success %', 'Duels won']
    thewriter.writerow(fieldnames)

    url = "https://www.premierleague.com/players/3920/Paul-Pogba/stats?co=1&se=-1"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    first_player = [] # stores all of the player's info

    # gets the player's name
    name_element = doc.find_all('div', class_ = "name t-colour")
    player_name = ""
    for element in name_element:
        player_name = element.text

    first_player.append(player_name)

    stats_elements = doc.find_all('div', class_ = "normalStat")
    for elements in stats_elements:
        stats_str = elements.text
        stats_str = stats_str.strip()
        stats_list = stats_str.split("\n") # stat description and actual stat are on separate lines
        stats_list[0] = stats_list[0].strip()
        stats_list[1] = stats_list[1].strip()
        
        if (stats_list[0] in fieldnames):
            first_player.append(stats_list[1])
        
    thewriter.writerow(first_player)

    url = "https://www.premierleague.com/players/5101/Ilkay-G%C3%BCndogan/stats?co=1&se=-1"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    second_player = []
    name_element = doc.find_all('div', class_ = "name t-colour")
    player_name = ""
    for element in name_element:
        player_name = element.text

    second_player.append(player_name)

    stats_elements = doc.find_all('div', class_ = "normalStat")
    for elements in stats_elements:
        stats_str = elements.text
        stats_str = stats_str.strip()
        stats_list = stats_str.split("\n")
        stats_list[0] = stats_list[0].strip()
        stats_list[1] = stats_list[1].strip()
        
        if (stats_list[0] in fieldnames):
            second_player.append(stats_list[1])
    
    thewriter.writerow(second_player)
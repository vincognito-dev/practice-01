player = {
    "name": "Ahmed Musa",
    "position": "forward",
    "date_of_birth": "1992-10-14",
    "seasons": [{"season": "2024/2025", "club": "kano pillars", "apps": 23, "goals": 10},
    {"season": "2025/2026", "club": "kano pillars", "apps": 26, "goals": 6}]
}

def get_career_totals(player):
    total_apps = 0
    total_goals = 0
    seasons_list = player["seasons"]
    for season in seasons_list:
        total_apps += season["apps"]
        total_goals += season["goals"]
    return {"total_apps": total_apps, "total_goals": total_goals}

def display_player(player):
    name = player.get("name")
    position = player.get("position")
    date_of_birth = player.get("date_of_birth")
    print(f"player_name: {name}, | position: {position}, | date_of_birth: {date_of_birth}")


    seasons = player.get("seasons")
    for items in seasons:
        season = items.get("season")
        club = items.get("club")
        apps = items.get("apps")
        goals = items.get("goals")
        print(f'season: {season}, | club: {club}, | apps: {apps}, | goals: {goals}')
    totals = get_career_totals(player)
    total_apps = totals.get("total_apps")
    total_goals = totals.get("total_goals")
    print(f'Total_apps: {total_apps} | Total_goals: {total_goals}')
display_player(player)

def main_menu():
    print("Player Career Tracker")
    print("____________________\n")
    print("1. Add a player")
    print("2. Add a season")
    print("3. View a player")
    print("4. List all players")
    print("5. Quit")
    choice = input("Select an option 1-5: ")
    return choice
players = []
def get_player_info():
     name = input("Enter player name: ")
     dob = input("Enter player date of birth (e.g., YYYY-MM-DD): ")
     position = input("Enter player position: ")

     player_data = {"name": name, "date_of_birth": dob, "position": position, "seasons": []}
     return player_data
def find_player():
    
while True:
    choice = main_menu()
    if choice == "1":
        new_player = get_player_info()
        players.append(new_player)
    elif choice == "2":
        print("Add a season")
    elif  choice == "3":
        print("View a player")
    elif choice == "4":
        print("List all players")
    elif choice == "5":
        print("Quit")
        break
    else:
        print("invalid input, Try again")

import json
import os
import math
import time
import requests
os.system('')

try:
    with open('API_KEY') as inf:
        API_KEY = inf.read()
except FileNotFoundError:
    API_KEY = input("Please enter your API key: ")
    with open('API_KEY', 'w') as outf:
        outf.write(API_KEY)

NONRANK = "\u001b[30;1m"
VIP = "\u001b[32;1m[VIP\u001b[32;1m]"
VIP_PLUS = "\u001b[32;1m[VIP\033[38;5;208m+\u001b[32;1m]"
MVP = "\033[38;5;51m[MVP"
MVP_PLUS = "\033[38;5;208m[MVP"
YOUTUBER = "\033[38;5;196m[\033[38;5;255mYOUTUBE\033[38;5;196m]"
GAME_MASTER = "\033[38;5;22m[GM]"
ADMIN = "\033[38;5;196m[ADMIN]"
reset = "\u001b[0m"

while True:
    name = input("Input name: ")
    try:
        def get_info(ign):
            return requests.get(ign).json()

        ign = f"https://api.mojang.com/users/profiles/minecraft/{name}"

        data = get_info(ign)

        uuid = data["id"]
    except Exception:
        print(f"\033[38;5;196mProvided invalid username. Try again{reset}")
        continue

    def get_info(url):
        return requests.get(url).json()

    url = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"
    data = get_info(url)

    x = requests.get("https://playerdb.co/api/player/minecraft/" + uuid)
    x = x.json()
    display = x['data']['player']['username']


    try:
        bw_final_deaths = data["player"]["stats"]["Bedwars"]["final_deaths_bedwars"]
    except KeyError:
        bw_final_deaths = 0
    try:
        bw_final_kills = data["player"]["stats"]["Bedwars"]["final_kills_bedwars"]
    except KeyError:
        bw_final_kills = 0
    try:
        bw_level = data["player"]["achievements"]["bedwars_level"]
    except KeyError:
        bw_level = 1
    try:
        network_exp = data["player"]["networkExp"]
    except KeyError:
        network_exp = 0
    try:
        sw_level = data["player"]["achievements"]["skywars_you_re_a_star"]
    except KeyError:
        sw_level = 1
    try:
        sw_kills = data["player"]["stats"]["SkyWars"]["kills"]
    except KeyError:
        sw_kills = 0
    try:
        sw_deaths = data["player"]["stats"]["SkyWars"]["deaths"]
    except KeyError:
        sw_deaths = 0
    try:
        d_wins = data["player"]["stats"]["Duels"]["wins"]
    except KeyError:
        d_wins = 0
    try:
        d_losses = data["player"]["stats"]["Duels"]["losses"]
    except KeyError:
        d_losses = 0
    try:
        uhc_score = data["player"]["stats"]["UHC"]["score"]
    except KeyError:
        uhc_score = 0
    try:
        rank_color = data["player"]["rankPlusColor"]
    except KeyError:
        rank_color = "RED"
    try:
        discord = data["player"]["socialMedia"]["links"]["DISCORD"]
    except KeyError:
        discord = ""

    if "rankPlusColor" in data["player"]:
        rank_color = data["player"]["rankPlusColor"]
    else:
        rank_color = "RED"

    if "rank" in data["player"] and not data["player"]["rank"] == "NORMAL":
        rank = data["player"]["rank"]
    elif "monthlyPackageRank" in data["player"] and not data["player"]["monthlyPackageRank"] == "NONE":
        rank = data["player"]["monthlyPackageRank"]
    elif "newPackageRank" in data["player"]:
        rank = data["player"]["newPackageRank"]
    elif "packageRank" in data["player"]:
        rank = data["player"]["packageRank"]
    else:
        rank = None

    if rank == None:
        col = NONRANK
    elif rank == "VIP":
        col = VIP
    elif rank == "VIP_PLUS":
        col = VIP_PLUS
    elif rank == "MVP" or rank == "MVP_PLUS":
        col = MVP
    elif rank == "SUPERSTAR":
        col = MVP_PLUS
    elif rank == "YOUTUBER":
        col = YOUTUBER
    elif rank == "GAME_MASTER":
        col = GAME_MASTER
    elif rank == "ADMIN":
        col = ADMIN
    else: print("\033[38;5;196mError\u001b[0m")

    if rank == "MVP_PLUS" or "SUPERSTAR":
        if rank_color == "RED":
            PLUS = "\u001b[31;1m"
        if rank_color == "GOLD":
            PLUS = "\033[38;5;208m"
        if rank_color == "GREEN":
            PLUS = "\u001b[32;1m"
        if rank_color == "YELLOW":
            PLUS = "\u001b[33;1m"
        if rank_color == "LIGHT_PURPLE":
            PLUS = "\033[38;5;219m"
        if rank_color == "WHITE":
            PLUS = "\033[38;5;255m"
        if rank_color == "BLUE":
            PLUS = "\033[38;5;27m"
        if rank_color == "DARK_GREEN":
            PLUS = "\033[38;5;34m"
        if rank_color == "DARK_RED":
            PLUS = "\033[38;5;124m"
        if rank_color == "DARK_AQUA":
            PLUS = "\033[38;5;45m"
        if rank_color == "DARK_PURPLE":
            PLUS = "\033[38;5;171m"
        if rank_color == "DARK_GRAY":
            PLUS = "\u001b[30;1m"
        if rank_color == "BLACK":
            PLUS = "\u001b[30m"
        if rank_color == "DARK_BLUE":
            PLUS = "\033[38;5;17m"

    if rank == "MVP_PLUS": 
        r = f"{col}{PLUS}+\033[38;5;51m] {display}{reset}"
    elif rank == "SUPERSTAR":
        r = f"{col}{PLUS}++\033[38;5;208m] {display}{reset}"
    elif rank == "MVP":
        r = f"{col}\033[38;5;51m] {display}{reset}"
    else: r = f"{col} {display}{reset}"

    def get_info(g_info):
        return requests.get(g_info).json()

    g_info = f"https://api.hypixel.net/findGuild?key={API_KEY}&byUuid={uuid}"

    data = get_info(g_info)

    g_id = data["guild"]

    def get_info(g_info):
        return requests.get(g_info).json()

    g_info = f"https://api.hypixel.net/guild?key={API_KEY}&id={g_id}"

    data = get_info(g_info)

    try:
        guild_name = data["guild"]["name"]
    except (KeyError, TypeError):
        guild_name = ""
    try:
        guild_color = data["guild"]["tagColor"]
    except (KeyError, TypeError):
        guild_color = "GRAY"

    if guild_color == "GRAY":
        guild_color = "\033[38;5;245m"
    elif guild_color == "YELLOW":
        guild_color = "\033[38;5;226m"
    elif guild_color == "GOLD":
        guild_color = "\033[38;5;208m"
    elif guild_color == "DARK_GREEN":
        guild_color = "\033[38;5;28m"
    elif guild_color == "DARK_AQUA":
        guild_color = "\033[38;5;30m"
    
    try:
        gexp = 0
        mem = data["guild"]["members"]
        for i in mem:
            if i["uuid"] == uuid:
                for n in i["expHistory"].values():
                    gexp += n
        if (int(gexp)) < 100000:
            print(f"{r} gained \033[38;5;196m{gexp}{reset} GEXP in the last 7 days while being in {guild_color}{guild_name}{reset}")
        elif gexp in range (100000, 200000):
            print(f"{r} gained \u001b[33;1m{gexp}{reset} GEXP in the last 7 days while being in {guild_color}{guild_name}{reset}")
        elif gexp in range (200000, 300000):
            print(f"{r} gained \u001b[32;1m{gexp}{reset} GEXP in the last 7 days while being in {guild_color}{guild_name}{reset}")
        else: print(f"{r} gained \u001b[35;1m{gexp}{reset} GEXP in the last 7 days while being in {guild_color}{guild_name}{reset}")
    except KeyError:
        print(f"{r} is currently not in the guild")
    
    if bw_final_deaths == 0:
        bw_fkdr = bw_final_kills
    else:  
        bw_fkdr = bw_final_kills / bw_final_deaths
    if sw_deaths == 0:
        sw_kdr = sw_kills
    else:
        sw_kdr = sw_kills / sw_deaths
    if d_losses == 0:
        d_wlr = d_wins
    else:
        d_wlr = d_wins / d_losses

    network_level = (math.sqrt((2 * network_exp) + 30625) / 50) - 2.5
    network_level = round(network_level, 2)
    bw_fkdr = round(bw_fkdr, 2)
    sw_kdr = round(sw_kdr, 2)
    d_wlr = round(d_wlr, 2)

    if uhc_score < 10:
        uhc_star = 1
    if uhc_score in range (10, 60):
        uhc_star = 2
    if uhc_score in range (60, 210):
        uhc_star = 3
    if uhc_score in range (210, 460):
        uhc_star = 4
    if uhc_score in range (460, 960):
        uhc_star = 5
    if uhc_score in range (960, 1710):
        uhc_star = 6
    if uhc_score in range (1710, 2710):
        uhc_star = 7
    if uhc_score in range (2710, 5210):
        uhc_star = 8
    if uhc_score in range (5210, 10210):
        uhc_star = 9
    if uhc_score in range (10210, 13210):
        uhc_star = 10
    if uhc_score in range (13210, 16210):
        uhc_star = 11
    if uhc_score in range (16210, 19210):
        uhc_star = 12
    if uhc_score in range (19210, 22210):
        uhc_star = 13
    if uhc_score in range (22210, 25210):
        uhc_star = 14
    if uhc_score >= 25210:
        uhc_star = 15

    if (float(network_level)) < 100:
        print(f"Network Level: \u001b[31;1m{network_level}\u001b[0m")
    else: print(f"Network Level: \u001b[32;1m{network_level}\u001b[0m")

    if (int(bw_level)) < 150:
        print(f"Bedwars Star: \u001b[31;1m{bw_level}\u001b[0m")
    else: print(f"Bedwars Star: \u001b[32;1m{bw_level}\u001b[0m")

    if (float(bw_fkdr) < 2.5):
        print(f"Bedwars FKDR: \u001b[31;1m{bw_fkdr}\u001b[0m")
    else: print(f"Bedwars FKDR: \u001b[32;1m{bw_fkdr}\u001b[0m")
    if (int(sw_level)) < 15:
        print(f"Skywars Star: \u001b[31;1m{sw_level}\u001b[0m")
    else: print(f"Skywars Star: \u001b[32;1m{sw_level}\u001b[0m")

    if (float(sw_kdr)) < 1:
        print(f"Skywars KDR: \u001b[31;1m{sw_kdr}\u001b[0m")
    else: print(f"Skywars KDR: \u001b[32;1m{sw_kdr}\u001b[0m")

    if (int(d_wins)) < 2000:
        print(f"Duels wins: \u001b[31;1m{d_wins}\u001b[0m")
    else: print(f"Duels wins: \u001b[32;1m{d_wins}\u001b[0m")

    if (float(d_wlr)) < 2.5:
        print(f"Duels WLR: \u001b[31;1m{d_wlr}\u001b[0m")
    else: print(f"Duels WLR: \u001b[32;1m{d_wlr}\u001b[0m")

    if (int(uhc_star)) < 5:
        print(f"UHC Star: \u001b[31;1m{uhc_star}\u001b[0m")
    else: print(f"UHC Star: \u001b[32;1m{uhc_star}\u001b[0m")

    print(f"Discord: \033[38;5;33m{discord}")

    if (float(network_level)) >= 100 and (float(bw_fkdr) >= 2.5) and (int(bw_level)) >= 150:
        print(f"{r} \u001b[32;1mmeets requirements\u001b[0m\n")
    elif (float(network_level)) >= 100 and (int(sw_level)) >= 15 and (float(sw_kdr)) >= 1:
        print(f"{r} \u001b[32;1mmeets requirements\u001b[0m\n")
    elif (float(network_level)) >= 100 and (int(d_wins)) >= 2000 and (float(d_wlr)) >= 2.5:
        print(f"{r} \u001b[32;1mmeets requirements\u001b[0m\n")
    elif (float(network_level)) >= 100 and (int(uhc_score)) >= 460:
        print(f"{r} \u001b[32;1mmeets requirements\u001b[0m\n")
    elif (int(gexp)) > 300000:
        print(f"{r} \u001b[35;1mmeets GEXP requirements\u001b[0m\n")
    else: print(f"{r} \u001b[31;1mdoesn't meets requirements\u001b[0m\n")
    time.sleep(0.5)
from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
import schedule
import time

def scheduled():
    #connect to yahoo api
    sc = OAuth2(None, None, from_file='oauth2.json')

    # get game object
    gm = yfa.Game(sc, 'nfl')

    leagues = gm.league_ids()

    print(leagues)

    # get the league object
    lg = gm.to_league('YOURLEAGUE')

    # get the team key
    teamkey = lg.team_key()

    #get the team object
    team = lg.to_team(teamkey)
    #get team roster
    roster = team.roster()

    # print(roster)

    # waivers = lg.waivers()
    # print(waivers)

    print("=== MY TEAM ===")

    for r in roster:
        print(r)

    # fa = lg.free_agents('QB')
    #
    # print('=== FREE AGENTS ===')
    #
    # for p in fa:
    #     print(p)

    # # # Drop Lamelo
    # # team.drop_player(6395)
    # #
    # Add Deshaun Watson
    team.add_player(30125)
    #
    # Drop Harden add Conley
    # team.add_and_drop_players(4246, 4563)

    newroster = team.roster()

    print("=== MY NEW ROSTER ===")

    for r in newroster:
        print(r)

schedule.every().day.at("04:00").do(scheduled)

while True:
    schedule.run_pending()
    time.sleep(1)

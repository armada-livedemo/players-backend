import pymysql
import hermes

db_config = hermes.get_config('database.json')


def create_player(player_name):
    with pymysql.connect(**db_config) as cur:
        cur.execute("INSERT INTO players(player_name) VALUES (%s)", player_name)


def get_players():
    with pymysql.connect(**db_config) as cur:
        cur.execute("SELECT * FROM players")
        result = cur.fetchall()
    return result


def get_player(player_name):
    with pymysql.connect(**db_config) as cur:
        cur.execute("SELECT * FROM players WHERE player_name = %s", player_name)
        result = cur.fetchall()
    return result


def update_score(player_name, score):
    with pymysql.connect(**db_config) as cur:
        cur.execute("UPDATE players SET best_score = %s WHERE player_name = %s AND best_score < %s",
                    (score, player_name, score))

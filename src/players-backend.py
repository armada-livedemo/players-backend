import web
import players

web.config.debug = False

class Index(object):
    def GET(self):
        return 'Service works!'


class Players(object):
    def GET(self):
        return str(players.get_players())+"\n"


class Player(object):
    def POST(self, player_name):
        players.create_player(player_name)
        return str(players.get_player(player_name))+"\n"

    def GET(self, player_name):
        return str(players.get_player(player_name))+"\n"


class Score(object):
    def POST(self, player_name, score):
        players.update_score(player_name, score)
        return "Ok\n"


def main():
    urls = (
        '/', Index.__name__,
        '/players', Players.__name__,
        '/player/(.*)/([0-9]+)', Score.__name__,
        '/player/(.*)', Player.__name__,
    )
    app = web.application(urls, globals())
    app.run()


if __name__ == '__main__':
    main()

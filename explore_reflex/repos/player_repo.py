import sqlite3

from icecream import ic

from explore_reflex.entities.player import Player


class PlayerRepository:
    def __init__(self, db_file: str):
        self.db_file = db_file
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()
        ic(f"connected to {self.db_file}")
        # self.cursor.execute(
        #     """CREATE TABLE IF NOT EXISTS players
        #                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        #                         code TEXT,
        #                         surname TEXT,
        #                         initial TEXT,
        #                         firstname TEXT,
        #                         active BOOLEAN)"""
        # )
        # self.connection.commit()

    def add_player(self, player: Player):
        self.cursor.execute(
            """INSERT INTO players (code, surname, initial, firstname, active)
                               VALUES (?, ?, ?, ?, ?)""",
            (
                player.code,
                player.surname,
                player.initial,
                player.firstname,
                player.active,
            ),
        )
        self.connection.commit()

    def get_player_by_id(self, player_id: int) -> Player | None:
        self.cursor.execute("""SELECT * FROM players WHERE id = ?""", (player_id,))
        player_data = self.cursor.fetchone()
        if player_data:
            return Player(
                id=player_data[0],
                code=player_data[1],
                surname=player_data[2],
                initial=player_data[3],
                firstname=player_data[4],
                active=bool(player_data[5]),
            )
        return None

    def get_all_players(self) -> list[Player]:
        ic("get_all_players()")
        self.cursor.execute("""SELECT * FROM players""")
        players_data = self.cursor.fetchall()
        res = [
            Player(
                id=player[0],
                code=player[1],
                surname=player[2],
                initial=player[3],
                firstname=player[4],
                active=bool(player[5]),
            )
            for player in players_data
        ]
        ic(f"{len(res)=}")
        return res

    def update_player(self, player: Player):
        self.cursor.execute(
            """UPDATE players SET code=?, surname=?, initial=?, firstname=?, active=?
                               WHERE id=?""",
            (
                player.code,
                player.surname,
                player.initial,
                player.firstname,
                player.active,
                player.id,
            ),
        )
        self.connection.commit()

    def delete_player(self, player_id: int):
        self.cursor.execute("""DELETE FROM players WHERE id=?""", (player_id,))
        self.connection.commit()

    def __del__(self):
        self.connection.close()

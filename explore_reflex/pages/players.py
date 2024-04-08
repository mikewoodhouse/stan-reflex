"""The dashboard page."""

from pathlib import Path

import reflex as rx
from icecream import ic

from explore_reflex.entities import Player
from explore_reflex.repos import PlayerRepository
from explore_reflex.templates import template


class PlayerNameSearch(rx.State):
    text: str = ""


@template(route="/players", title="Players")
def players() -> rx.Component:
    """
    The players page.
    """

    db_path = Path(__file__).parent.parent / "stan.sqlite"
    ic(db_path)

    players: list[Player] = PlayerRepository(str(db_path)).get_all_players()

    table_rows = [
        rx.table.row(rx.table.row_header_cell(player.name)) for player in players[:10]
    ]

    ic(f"{len(table_rows)=}")

    return rx.vstack(
        rx.heading("Players", size="8"),
        rx.input(
            name="player_name",
            placeholder="Player name",
            on_change=PlayerNameSearch.set_text,
        ),
        rx.button(
            "Search",
            type="submit",
        ),
        rx.text(PlayerNameSearch.text),
        rx.table.root(
            rx.table.header(rx.table.column_header_cell("Name")),
            rx.table.body(*table_rows),
        ),
    )

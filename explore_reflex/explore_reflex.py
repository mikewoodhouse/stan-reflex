"""Welcome to Reflex!."""

import reflex as rx

from explore_reflex import styles

# Import all the pages.
from explore_reflex.pages import *


class State(rx.State):
    """Define empty state to allow access to rx.State.router."""


# Create the app.
app = rx.App(style=styles.base_style)

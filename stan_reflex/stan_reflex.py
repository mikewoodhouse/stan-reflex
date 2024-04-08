"""Welcome to Reflex!."""

import reflex as rx

from stan_reflex import styles

# Import all the pages.
from stan_reflex.pages import *


class State(rx.State):
    """Define empty state to allow access to rx.State.router."""


# Create the app.
app = rx.App(style=styles.base_style)

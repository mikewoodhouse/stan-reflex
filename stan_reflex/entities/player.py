from dataclasses import dataclass


@dataclass(kw_only=True)
class Player:
    id: int = -1
    code: str = ""
    surname: str = ""
    initial: str = ""
    firstname: str = ""
    active: bool = False

    @property
    def name(self) -> str:
        if forename := self.firstname or self.initial:
            return f"{self.surname}, {forename}"
        return self.surname

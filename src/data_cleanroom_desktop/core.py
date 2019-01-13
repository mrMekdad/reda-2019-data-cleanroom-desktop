"""Core workflow for Data Cleanroom Desktop by Red@."""

PROJECT_NAME = "Data Cleanroom Desktop"
DOMAIN_THEME = "software engineering"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}

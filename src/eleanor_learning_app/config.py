from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Language:
    id: str
    display_name: str
    number_sound_path: Path


def load_languages(config_path: Path | None = None) -> list[Language]:
    path = config_path or PROJECT_ROOT / "config" / "languages.json"
    with path.open("r", encoding="utf-8") as config_file:
        data = json.load(config_file)

    languages = []
    for item in data.get("languages", []):
        languages.append(
            Language(
                id=str(item["id"]),
                display_name=str(item["display_name"]),
                number_sound_path=PROJECT_ROOT / str(item["number_sound_path"]),
            )
        )
    return languages

from pathlib import Path
import json
import re
import pandas as pd


def clean_episode(name: str) -> str:
    match = re.search(r"S\d+E\d+", name)
    return match.group(0) if match else name


def load_subtitles(path: str = "../data/raw/season1.json") -> pd.DataFrame:
    p = Path(path)
    data = json.loads(p.read_text(encoding="utf-8"))
    rows = []
    for episode_name, subtitles in data.items():
        episode = clean_episode(episode_name)
        for subtitle_id, text in subtitles.items():
            rows.append(
                {
                    "episode": episode,
                    "subtitle_id": int(subtitle_id),
                    "text": text,
                }
            )
    df = (
        pd.DataFrame(rows)
        .sort_values(["episode", "subtitle_id"])
        .reset_index(drop=True)
    )
    return df

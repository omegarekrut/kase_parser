import time
from datetime import timedelta
from typing import Tuple, Dict

def calculate_timestamps(interval: str) -> Tuple[int, int]:
    end_timestamp: int = int(time.time()) 
    intervals: Dict[str, timedelta] = {
        "1m": timedelta(minutes=1),
        "5m": timedelta(minutes=5),
        "15m": timedelta(minutes=15),
        "30m": timedelta(minutes=30),
        "1h": timedelta(hours=1),
        "4h": timedelta(hours=4),
        "1d": timedelta(days=1),
        "1w": timedelta(weeks=1),
        "1m": timedelta(weeks=4),
        "3m": timedelta(weeks=13),
        "6m": timedelta(weeks=26)
    }

    if interval not in intervals:
        raise ValueError(f"Unsupported interval: {interval}")

    start_timestamp: int = end_timestamp - int(intervals[interval].total_seconds())
    return start_timestamp, end_timestamp

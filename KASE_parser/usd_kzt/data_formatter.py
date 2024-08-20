from typing import List, Dict, Any

class DataFormatter:
    @staticmethod
    def format_data(raw_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        formatted_data: List[Dict[str, Any]] = []
        timestamps: List[int] = raw_data.get("t", [])
        opens: List[float] = raw_data.get("o", [])
        highs: List[float] = raw_data.get("h", [])
        lows: List[float] = raw_data.get("l", [])
        closes: List[float] = raw_data.get("c", [])
        volumes: List[float] = raw_data.get("v", [])

        for i in range(len(timestamps)):
            formatted_data.append({
                "timestamp": timestamps[i] * 1000, 
                "open": opens[i],
                "high": highs[i],
                "low": lows[i],
                "close": closes[i],
                "volume": volumes[i],
            })

        return formatted_data

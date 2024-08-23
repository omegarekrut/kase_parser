import json
import os
import time
from typing import Any, Dict, List


def save_json_to_file(data: List[Dict[str, Any]], directory: str) -> None:
    # Get the current timestamp for the filename
    current_timestamp = int(time.time())
    filename = f"{current_timestamp}.json"
    filepath = os.path.join(directory, filename)

    # Create the directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)

    # Save the JSON data to the file
    with open(filepath, "w") as json_file:
        json.dump(data, json_file, indent=2)

    print(f"Data saved to {filepath}")
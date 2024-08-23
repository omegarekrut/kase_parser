from save_json_to_file import save_json_to_file
from kase_client import KaseClient
from data_formatter import DataFormatter
from timestamp_utils import calculate_timestamps
import json

def main() -> None:
    client: KaseClient = KaseClient()
    symbol: str = "USDKZT_TOM"
    resolution: str = "D" 
    interval: str = "3m"  

    start_timestamp, end_timestamp = calculate_timestamps(interval)

    raw_data = client.fetch_currency_data(
        symbol=symbol, 
        resolution=resolution, 
        start_timestamp=start_timestamp, 
        end_timestamp=end_timestamp
    )
    formatted_data = DataFormatter.format_data(raw_data)
    
    directory = "output"
    save_json_to_file(formatted_data, directory)

    print(json.dumps(formatted_data, indent=2))
    

if __name__ == "__main__":
    main()

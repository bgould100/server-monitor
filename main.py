import json
import os
from monitor import online_servers, highest_cpu, server_count
from pathlib import Path
filename = os.environ.get("SERVER_FILE")
file_path = Path(filename)
with file_path.open("r") as file:
    data = json.load(file)

onl_serv = online_servers(data)
print(onl_serv)

highest = highest_cpu(data)
print("Highest CPU server is:", highest)

count = server_count(data)
print(f"Total servers: {count}")

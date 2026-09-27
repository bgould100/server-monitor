def online_servers(data):
    onl_serv = []
    for item in data:
        if item["status"] == "online":
            onl_serv.append(item)
    return onl_serv


def highest_cpu(data):
    high = 0
    highest = {}
    for item in data:
        if item["cpu"] > high:
            high = item["cpu"]
            highest = item
    return highest


def server_count(data):
    cou = len(data)
    return cou

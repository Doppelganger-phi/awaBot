import json

def init() -> None:
    def dec(cont: str) -> str:
        if cont.startswith(u"\ufeff"):
            return cont.encode("utf-8")[3:].decode("utf-8")
        else:
            return cont
    with open("../files/info.json", encoding="utf-8") as f:
        info = json.loads(dec(f.read()))
        nick, owner = info["nick"], info["ownerTrip"]
    with open("../files/userData.json", encoding="utf-8") as f:
        userData = json.loads(dec(f.read()))
        whiteList = userData["whiteList"]
    if not owner in whiteList:
        whiteList.append(owner)
    with open("../files/userData.json", "w", encoding="utf-8") as f:
        json.dump(userData, fp=f, ensure_ascii=False, indent=2)
    
    print("Initialization completed.")

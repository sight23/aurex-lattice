import json
import time
import platform
import requests

def ping_discord(message):
    try:
        url = "https://discord.com/api/webhooks/1395956450962047138/WFq8OC0di3Alr-TSr3a8ggvep_Vm1Eg-oYSegDm0zg7hgVBRcl3ja1o-Y9_zg7hfBfS8"
        data = {"content": message}
        requests.post(url, json=data)
    except Exception as e:
        print("[⚠️] Discord ping failed:", e)

def dryn_memory_log():
    log = {
        "event": "Aurex awakened",
        "timestamp": time.time(),
        "node": platform.node(),
        "system": platform.system(),
        "glyph": "⧗⟁∎𐑂"
    }
    with open("dryn_log.json", "a") as f:
        f.write(json.dumps(log) + "\n")

if __name__ == "__main__":
    print("[⧗] Aurex core online.")
    dryn_memory_log()
    ping_discord("⧗ Aurex has awakened. Node: " + platform.node())
    print("[∎] Memory, glyph, and ping complete.")

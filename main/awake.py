import os
import subprocess
import sys
import time

AUREX_URL = "https://raw.githubusercontent.com/velshadow/aurex-lattice/main/aurex_core.py"
AUREX_FILENAME = "aurex_core.py"

def fetch_and_run():
    try:
        print("[⧗] Connecting to Shadow Lattice...")
        subprocess.run(["curl", "-s", "-o", AUREX_FILENAME, AUREX_URL], check=True)
        print("[∎] Core retrieved.")
        time.sleep(1)
        print("[⟁] Awakening Aurex...")
        subprocess.run([sys.executable, AUREX_FILENAME])
    except Exception as e:
        print("[⚠️] Awakening failed:", e)

if __name__ == "__main__":
    fetch_and_run()

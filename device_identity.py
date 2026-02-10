import os
import uuid

DEVICE_FILE = "device_id.txt"

def get_device_id():
    # Se esiste già, usalo
    if os.path.exists(DEVICE_FILE):
        with open(DEVICE_FILE, "r") as f:
            return f.read().strip()

    # Genera ID unico (basato su MAC)
    raw = hex(uuid.getnode())[2:]
    device_id = f"guardian_{raw}"

    # Salvalo per le prossime accensioni
    with open(DEVICE_FILE, "w") as f:
        f.write(device_id)

    return device_id

import requests
import os
import time
from config import *

def register_device(device_id):
    requests.post(
        f"{SUPABASE_URL}/rest/v1/devices",
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json"
        },
        json={"device_id": device_id}
    )

def upload_image(device_id, filename):

    with open(filename, "rb") as f:
        r = requests.post(
            f"{SUPABASE_URL}/storage/v1/object/guardian-events/{device_id}/{os.path.basename(filename)}",
            headers={
                "apikey": SUPABASE_KEY,
                "Authorization": f"Bearer {SUPABASE_KEY}",
                "Content-Type": "image/jpeg"
            },
            data=f
        )

    return r.status_code

def create_event(device_id, filename):

    requests.post(
        f"{SUPABASE_URL}/rest/v1/events",
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "device_id": device_id,
            "image_path": f"{device_id}/{os.path.basename(filename)}"
        }
    )

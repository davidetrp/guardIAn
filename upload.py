import requests
from config import SUPABASE_URL, SUPABASE_KEY, DEVICE_ID 

#with open("../snapshots/test.jpg", "rb") as f:
 #   r = requests.post(
  #      f"{SUPABASE_URL}/storage/v1/object/guardian-events/guardian_home/test.jpg",


def upload(filename):
    with open(filename, "rb") as f:
        r = requests.post(
            f"{SUPABASE_URL}/storage/v1/object/guardian-events/{DEVICE_ID}/{filename}",
            headers={
                "apikey": SUPABASE_KEY,
                "Authorization": f"Bearer {SUPABASE_KEY}",
                "Content-Type": "image/jpeg"
            },
            data=f
        )
    return r.status_code

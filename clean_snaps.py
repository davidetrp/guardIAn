import glob
import os
import requests

from config import (
    MAX_LOCAL_SNAPSHOTS,
    LOCAL_FOLDER,
    SUPABASE_URL,
    SUPABASE_KEY,
    DEVICE_ID
)

# ⚠️ nome bucket (obbligatorio)
SUPABASE_BUCKET = 'guardian_', DEVICE_ID 


def delete_from_supabase(filename: str):
    url = f"{SUPABASE_URL}/storage/v1/object/{SUPABASE_BUCKET}/{filename}"

    headers = {
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "apikey": SUPABASE_KEY,
    }

    r = requests.delete(url, headers=headers)

    if r.status_code not in (200, 204):
        print(f"⚠️ Supabase delete failed {filename}: {r.status_code} {r.text}")
    else:
        print(f"☁️ Cloud deleted: {filename}")


def cleanup_old_files():

    files = sorted(
        glob.glob(os.path.join(LOCAL_FOLDER, "*.jpg")),
        key=os.path.getmtime
    )

    if len(files) <= MAX_LOCAL_SNAPSHOTS:
        return

    for file_path in files[:-MAX_LOCAL_SNAPSHOTS]:
        filename = os.path.basename(file_path)

        # 1️⃣ delete local
        try:
            os.remove(file_path)
            print(f"🗑️ Local deleted: {filename}")
        except Exception as e:
            print(f"⚠️ Local delete failed {filename}: {e}")

        # 2️⃣ delete cloud
        delete_from_supabase(filename)

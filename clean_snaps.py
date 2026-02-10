import glob
import os
from config import MAX_LOCAL_SNAPSHOTS, LOCAL_FOLDER

def cleanup_old_files():

    files = sorted(
        glob.glob(os.path.join(LOCAL_FOLDER, "*.jpg")),
        key=os.path.getmtime
    )

    if len(files) > MAX_LOCAL_SNAPSHOTS:
        for f in files[:-MAX_LOCAL_SNAPSHOTS]:
            os.remove(f)

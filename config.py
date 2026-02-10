from device_identity import get_device_id
from supabase_client import *
# Zona di interesse (percentuale del frame)
ROI_Y_START = 0.5     # metà inferiore: soglia/porta
ROI_Y_END   = 1.0

# Motion detection
MIN_AREA = 5000        # area minima (da tarare)
FRAMES_REQUIRED = 3    # frame consecutivi
COOLDOWN_SEC = 20      # evita raffiche

#CLEAN SNAPSHOTS
MAX_LOCAL_SNAPSHOTS = 5
LOCAL_FOLDER = '../snapshots/'
# Camera
LOW_RES = (320, 240)
HIGH_RES = (1280, 720)

# UPLOAD LINKS SUPABASE
SUPABASE_URL = 'https://rpfdtiayciclzswsuflo.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJwZmR0aWF5Y2ljbHpzd3N1ZmxvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzA3MzAzMjMsImV4cCI6MjA4NjMwNjMyM30.V8Ank3r9PWdUGpJRKQ15KHbbxH4gA6nQ81qhtUzH3JU'
DEVICE_ID = get_device_id()

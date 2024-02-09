import xmltodict
import dict2xml
import calendar
import datetime
from dateutil.parser import parse
import sqlite3

with open('2024-02-05_11_42_31.895_2024-02-05T11_42+0530.gpx') as file:
  activity = xmltodict.parse(file.read())
  
db = sqlite3.connect('gadgetbridge')
cursor = db.cursor()

for track_point in activity['gpx']['trk']['trkseg']['trkpt']:
  activity_time = parse(track_point['time'])
  seconds = calendar.timegm(activity_time.timetuple())
  seconds = seconds - (seconds%60)
  row = cursor.execute("select HEART_RATE from hybrid_hractivity_sample where TIMESTAMP = ?", (seconds,)).fetchone()
  track_point['extensions']['gpxtpx:TrackPointExtension']['gpxtpx:HR'] = row[0]
  
print(dict2xml.dict2xml(activity['gpx']['trk']['trkseg']))
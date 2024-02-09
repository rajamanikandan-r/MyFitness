import gpxpy
import gpxpy.gpx
from xml.etree.ElementTree import Element, SubElement, tostring
import sqlite3
import calendar

gpx_file = open("2024-02-05_11_42_31.895_2024-02-05T11_42+0530.gpx", "r")
gpx = gpxpy.parse(gpx_file)

db = sqlite3.connect('gadgetbridge')
cursor = db.cursor()

for track in gpx.tracks:
  for segment in track.segments:
    for track_point in segment.points:
      seconds = calendar.timegm(track_point.time.timetuple())
      seconds = seconds - (seconds%60)
      print(track_point.time)
      print(seconds)
      row = cursor.execute("select HEART_RATE from hybrid_hractivity_sample where TIMESTAMP = ?", (seconds,)).fetchone()
		  # Create extension (hr)
      hr = row[0]
      extension = Element("gpxtpx:TrackPointExtension", attrib={"xmlns:gpxtpx": "http://www.garmin.com/xmlschemas/TrackPointExtension/v1"})
      hr_element = SubElement(extension, "gpxtpx:hr")
      hr_element.text = str(hr)
      track_point.extensions.append(extension)

# Save the modified GPX file
with open("modified_workout.gpx", "w") as output_file:
    output_file.write(gpx.to_xml())
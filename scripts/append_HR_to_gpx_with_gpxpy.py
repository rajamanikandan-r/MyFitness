import gpxpy
import gpxpy.gpx
from xml.etree.ElementTree import Element, SubElement, tostring
import sqlite3
import calendar
import glob

files = glob.glob("*.gpx")
db = sqlite3.connect('gadgetbridge')
cursor = db.cursor()

for file in files:
	gpx_file = open(file, "r")
	gpx = gpxpy.parse(gpx_file)

	for track in gpx.tracks:
	  for segment in track.segments:
	    for track_point in segment.points:
	      seconds = calendar.timegm(track_point.time.timetuple()) - 19800
	      seconds = seconds - (seconds%60)
	      row = cursor.execute("select HEART_RATE from hybrid_hractivity_sample where TIMESTAMP = ?", (seconds,)).fetchone()
	      hr = row[0]
	      extension = Element("gpxtpx:TrackPointExtension", attrib={"xmlns:gpxtpx": "http://www.garmin.com/xmlschemas/TrackPointExtension/v1"})
	      hr_element = SubElement(extension, "gpxtpx:hr")
	      hr_element.text = str(hr)
	      track_point.extensions.append(extension)

	with open("mod_" + file, "w") as output_file:
	    output_file.write(gpx.to_xml())
import sqlite3
import datetime
import numpy as np

conn = sqlite3.connect('gadgetbridge')
c = conn.cursor()
min_steps_per_minute=00

d=c.execute("select strftime('%Y.%m.%d', datetime(timestamp, 'unixepoch')) as d,sum(STEPS) from HYBRID_HRACTIVITY_SAMPLE where STEPS > ? group by d",(min_steps_per_minute,)).fetchall()
w=c.execute("select strftime('%Y.%W', datetime(timestamp, 'unixepoch')) as d,sum(STEPS) from HYBRID_HRACTIVITY_SAMPLE where STEPS > ? group by d",(min_steps_per_minute,)).fetchall()
m=c.execute("select strftime('%Y.%m', datetime(timestamp, 'unixepoch')) as d,sum(STEPS) from HYBRID_HRACTIVITY_SAMPLE where STEPS > ? group by d",(min_steps_per_minute,)).fetchall()
y=c.execute("select strftime('%Y', datetime(timestamp, 'unixepoch')) as d,sum(STEPS) from HYBRID_HRACTIVITY_SAMPLE where STEPS > ? group by d",(min_steps_per_minute,)).fetchall()
print("all avg:",c.execute("select avg(STEPS) from HYBRID_HRACTIVITY_SAMPLE where STEPS > ? ",(min_steps_per_minute,)).fetchall())

db={x[0]:x[1] for x in d}
wb={x[0]:x[1] for x in w}
mb={x[0]:x[1] for x in m}
yb={x[0]:x[1] for x in y}

print(d)
print(w)
print(m)
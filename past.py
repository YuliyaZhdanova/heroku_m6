from datetime import datetime as dt
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from collections import Counter

Base = declarative_base()


class LogEntry(Base):
    __tablename__ = "logs"

    uid = Column(Integer, primary_key=True)
    ip_addr = Column(String(16))
    timestamp = Column(DateTime)

    def __init__(self, ip_addr, timestamp):
        self.ip_addr = ip_addr
        self.timestamp = timestamp

    def __str__(self):
        return "'%s' on %s" % (self.ip_addr, self.timestamp)

 
engine = create_engine("sqlite:///access_log.db")
Session = sessionmaker(bind=engine)
s = Session()

val = s.query(LogEntry).count()
print(val)

c = []

q = s.query(LogEntry)
q = q.filter(LogEntry.timestamp < dt(2019, 3, 2))
for log in q.all():
    c.append(log.ip_addr)
 
count = Counter(c)
d = count.most_common(3)

f = d[0][1] + d[1][1] + d[2][1]
print(f/val * 100)
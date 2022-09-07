import haversine as hs
from haversine import Unit

loc1=(28.426846,77.088834)
loc2=(28.394231,77.050308)
print(type(loc1))
distance = hs.haversine(loc1,loc2)
m_distance = hs.haversine(loc1,loc2,unit=Unit.METERS)
miles = hs.haversine(loc1,loc2,unit=Unit.MILES)
print(distance,m_distance,miles)

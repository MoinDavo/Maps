import datetime as dt

class GeoDataPoint:
	def __init__(self, datetime:dt, latitude:float, longitude:float):
		self.datetime = datetime
		self.latitude = latitude
		self.longitude = longitude
		self.coordinate = (latitude, longitude)
	
	
class OlympusGeoDataPoint(GeoDataPoint):
	def __init__(self, datetime:dt, latitude:float, longitude:float, time, compass, pressure, temperature, acceleration):
		super().__init__(datetime, latitude, longitude)
		self.time = time
		self.compass = compass
		self.pressure = pressure
		self.temperature = temperature
		self.acceleration = acceleration

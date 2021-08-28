class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.timestayed = {}
        self.timesvisited = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        stationIn, timeIn = self.customers[id]
        if (stationIn, stationName) in self.timestayed:
            self.timestayed[(stationIn, stationName)] += t - timeIn
        else:
            self.timestayed[(stationIn, stationName)] = t - timeIn
        if (stationIn, stationName) in self.timesvisited:
            self.timesvisited[(stationIn, stationName)] += 1
        else:
            self.timesvisited[(stationIn, stationName)] = 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.timestayed[(startStation, endStation)]/self.timesvisited[(startStation, endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
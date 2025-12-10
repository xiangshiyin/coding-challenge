class UndergroundSystem:
    def __init__(self):
        from collections import defaultdict

        self.stationLog = defaultdict(list)
        self.routeStats = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.stationLog[id].append([stationName, t])

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, t1 = self.stationLog[id].pop()
        endStation = stationName
        if (startStation, endStation) not in self.routeStats:
            self.routeStats[(startStation, endStation)] = [t - t1, 1]
        else:
            self.routeStats[(startStation, endStation)][0] += t - t1
            self.routeStats[(startStation, endStation)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) not in self.routeStats:
            return None
        else:
            return (
                self.routeStats[(startStation, endStation)][0]
                / self.routeStats[(startStation, endStation)][1]
            )


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

finalPaths = []

def findPath(stations, firstStation, lastStation, paths=[]):
	paths.append(firstStation)
	for fromStation, toStation in stations:
		if fromStation == firstStation and toStation == lastStation:
			paths.append(lastStation)
			return paths
		elif fromStation == firstStation and toStation != lastStation:
			copyStations = list(stations)
 			copyStations.remove((fromStation, toStation))
 			return findPath(copyStations, toStation, lastStation, paths)
 			
 	return None

def parseInput(stations, firstStation, lastStation):
	for fromStation, toStation in stations:
		if fromStation == firstStation:
			copyStations = list(stations)
			copyStations.remove((fromStation, toStation))
			copyStations.insert(0, (fromStation, toStation))
			path = findPath(copyStations, fromStation, lastStation, [])

			if path != None:
				finalPaths.append(path)
				
				path = []

def readInput():
	stationsTuples = []
	print "Input:"
	while True:
		stations = raw_input()

		if stations == "":
			break

		singleStationTuple = (stations.split(" ")[0], stations.split(" ")[1])
		stationsTuples.append(singleStationTuple)

	return stationsTuples

parseInput(readInput(), "H", "L")
finalPaths.sort(lambda x,y: cmp(len(x), len(y)))

print "Output:"
print ' '.join(finalPaths[0])
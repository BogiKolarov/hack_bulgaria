finalPaths = []

def parseInput(stations, firstStation, lastStation, paths=[]):
	paths.append(firstStation)
	
	for fromStation, toStation in stations:
		print "trying: " + fromStation + " " + toStation
		if fromStation == firstStation and toStation == lastStation:
			paths.append(lastStation)
			finalPaths.append(paths)
			print str(paths)
		elif fromStation == firstStation and toStation != lastStation:
			print fromStation + " " + toStation
			stations.remove((fromStation, toStation))
			parseInput(stations, toStation, lastStation)
			

def readInput():
	stationsTuples = []

	while True:
		stations = raw_input()

		if stations == "":
			break

		singleStationTuple = (stations.split(" ")[0], stations.split(" ")[1])
		stationsTuples.append(singleStationTuple)

	return stationsTuples

parseInput(readInput(), "H", "L")
print
print finalPaths
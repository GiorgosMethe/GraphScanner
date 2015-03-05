import csv
import copy

graph = dict()

def scanner(node, path):
	if node not in graph:
		path.append(node)
		with open('paths.csv', 'a') as csvfile:
			csvwriter = csv.writer(csvfile, delimiter=',')
			csvwriter.writerow(path)
	else:
		for link in graph[node]:
			a = copy.copy(path)
			a.append(node)
			scanner(link,a)

with open('nodes.csv', 'rb') as csvfile:
	graphCSV = csv.reader(csvfile, delimiter=',')
	for row in graphCSV:
		if row[0] not in graph:
			graph[row[0]] = list()
		for i in xrange(1, len(row)):
			graph[row[0]].append(row[i])

# print graph
# for key, value in graph.iteritems():
# 	print key, value

scanner('1',[])



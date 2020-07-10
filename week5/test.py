query = ['palm.cpu', 23.1, 1235]
METRIC = ['palm.cpu', 23.1, 23123]
data = list(filter(lambda info: info == query, METRIC))
if len(data) == 0:
    METRIC.append(query)
print(METRIC)


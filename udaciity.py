import numpy
from scipy import stats
data = [1, 1, 2, 2, 3, 3, 4, 4]

mean = numpy.mean(data)
median = numpy.median(data)
mode = stats.mode(data)
std = numpy.std(data)
var = numpy.var(data)

print('mean',mean)
print('median',median)
print('mode',mode)
print('std',std)
print('var',var)
print('max', max(data))
print('min', min(data))
print('range', max(data) - min(data))
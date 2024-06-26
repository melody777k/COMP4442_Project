import os
import sys
from pyspark import SparkContext

args = sys.argv
inp = args[1] # all input data in one file
out = args[2] # output directory

# global outputA
# outputA = out
print("aaa")

def f(line):
    new_line = [None if item == '' else item for item in line]
    while len(new_line)<19:
        new_line.append(None)
    return new_line

def g(x):
    if x is None:
        return 0
    try:
        ans = int(x)
    except ValueError:
        ans = 0
    return ans

def add_tuples(tuple1, tuple2):
    result = tuple()
    
    for num1, num2 in zip(tuple1, tuple2):
        if type(num1)==str and num1==num2:
            sum_result = num1
        else:
            sum_result = num1 + num2
        result += (sum_result,)

    return result

sc = SparkContext()

inp = sc.textFile(inp)
inp = inp.flatMap(lambda line: line.split("\n"))
inp = inp.map(lambda line: line.split(",")).map(lambda l: f(l))

overspeed_num_times_info = inp.map(lambda line: (line[0],(line[1], g(line[14]),g(line[16]),g(line[15]),g(line[12])))).reduceByKey(lambda a, b: add_tuples(a, b)).coalesce(1)
overspeed_num_times_info.saveAsTextFile(out)


sc.stop()






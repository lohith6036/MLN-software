
# import xlrd
#
# # sample to work with excel
#
# workbook = xlrd.open_workbook('metaInfo100Recordsxls.xlsx')
# worksheet = workbook.sheet_by_name('metaInfo100Records')
# # give corresponding columns and rows starting from 0 .....n
# value = worksheet.cell(1, 1)
# print(value)

# import csv
# #
# # sample to work with csv
#
# with open('metaInfo100Records.csv') as csvDataFile:
#     data = [row for row in csv.reader(csvDataFile)]
#     print(data[1][1])

# with open('config_file_1.txt', mode='r') as config_file:
#     lines = config_file.readlines()
#     number_of_layers = lines[7]
#     for layer in range(int(number_of_layers)):
#         n=int(layer)+8
#         feature_row = lines[n]
#         x=feature_row.split(',')
#         file_name = "layer_file_{}".format(layer + 1)
#         print(file_name)


# switch case sample

# def zero():
#     print("You typed zero.\n")

# def sqr():
#     print ("n is a perfect square\n")


# # map the inputs to the function blocks
# options = {0 : zero,
#            1 : sqr,
#            4 : sqr,
#            9 : sqr,
# }


# options[1]()
# options[0]()
# options[4]()


# from haversine import haversine, Unit

# lyon = (45.7597, 4.8422) # (lat, lon)
# paris = (48.8567, 2.3508)

# print(haversine(lyon, paris))
# # >> 392.2172595594006  # in kilometers

# print(haversine(lyon, paris, unit=Unit.MILES))
# # >> 243.71201856934454  # in miles




# import math
# # Example points in 3-dimensional space...
# x = (5,6,7)
# y = (8,9,9)
# distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
# print("Euclidean distance from x to y: ",distance)


# jaccard score
# import numpy as np
# from sklearn.metrics import jaccard_score

# y_pred = [20, 12, 21,10,1 ,3]
# y_true = [20, 11, 12, 1, 2,45]
# result = jaccard_score(y_true, y_pred, average = None)
# # (None, 'micro', 'macro', 'weighted', 'samples')
# print(result.tolist())
# print(type(result))
# print(result)


# def jaccard(a, b):
#     c = a.intersection(b)
#     return float(len(c)) / (len(a) + len(b) - len(c))


# # list1=[20.1, 30.2, 10.1]
# # list2=[20.1, 30.2, 60.566, 10.2,10.1]

# list1 = [3, 7, 5,4,3,7]
# list2 = [2, 54, 13, 15]
# words1 = set(list1)
# words2 = set(list2)
# print(words1)
# print(jaccard(words1, words2))


# cosine
# from scipy import spatial

# def cosine_similarity(list1, list2):
#     similarity = 1 - spatial.distance.cosine(list1, list2)
#     return  similarity


# list1 = [3, 7, 5,4]
# list2 = [2, 54, 13, 15]
# print(cosine_similarity(list1, list2))


# Cosine similarity need two lists of similar shape which is not a case with any dataset
# Question # it gives a range between 0 and 1 but we need to know how to compare using the threshold for the cosine similarity
# we are getting some where around 0.98 or something with in 0.9 - 0.8



# pearson

# import math

# def average(x):
#     assert len(x) > 0
#     return float(sum(x)) / len(x)

# def pearson_def(x, y):
#     assert len(x) == len(y)
#     n = len(x)
#     assert n > 0
#     avg_x = average(x)
#     avg_y = average(y)
#     diffprod = 0
#     xdiff2 = 0
#     ydiff2 = 0
#     for idx in range(n):
#         xdiff = x[idx] - avg_x
#         ydiff = y[idx] - avg_y
#         diffprod += xdiff * ydiff
#         xdiff2 += xdiff * xdiff
#         ydiff2 += ydiff * ydiff

#     return diffprod / math.sqrt(xdiff2 * ydiff2)

# list1=[1,2,3]
# list2=[1,5,7]
# print (pearson_def(list1, list2))

# community detection


# import louvain
# import igraph as ig
# G = ig.Graph.Erdos_Renyi(100, 0.1)
# part = louvain.find_partition(G, louvain.ModularityVertexPartition)


# code to read all files in a folder in python
# path = '/some/path/to/file'

# for filename in os.listdir(path):

# path='C:/Users/Admin/OneDrive/RA/multi layer/Multilayer for Git/datasets'
# import os
# for filename in os.listdir():


import collections
a = ['Comedy','Musical','Romance','Comedy']

counter=collections.Counter(a)
print(counter)

    







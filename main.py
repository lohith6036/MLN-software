import csv
from itertools import combinations

from similarityMetric import SimilarityObject
from layer import *
import datetime
from inputValidation import *
import time

path='.\datasets'
import os
for filename in os.listdir(path):
    File_Path=filename
    # ActualPath='C:/Users/Admin/OneDrive/RA/multi layer/Multilayer for Git/datasets/{}'.format(File_Path)

    class Main:
        nodeList = []
        edgeList = []
        similarityObj = SimilarityObject()
        inputValidationObj = InputValidationObj()
        layerObj = LayerObject()
        # inputTypeObj = InputType()
        line_count = 0
        line_dummy_count=1
        userInputObj = UserInput(None,None,None,None,None,None,None,None,None,None,None,None)

    #Opening config file to fetch the details provided by the user
        with open('config_file_1.txt', mode='r') as config_file:
            lines = config_file.readlines()
            number_of_layers = lines[7]
            for layer in range(int(number_of_layers)):
                n = int(layer) + 8
                # index out of range  and rstrip to remove \n at the end
                feature_row = lines[n].rstrip("\n")
                #Node number currently taken as first column by default ( also can be considered as Unique Id or Primary Key)
                node_column = 0
                # check if the provided input is valid (according to the metric format and sequence) and assign the format which the user has opeted for
                result = inputValidationObj.layer_specification_validation(feature_row)
                # Assigning input from user file to the code flow
                feature_column = result.feature_column
                # if available
                feature_column_latitude=result.feature_column_lat
                feature_column_longitude=result.feature_column_long
                # number_of_ranges=result.number_of_range
                list_of_ranges=result.range_input
                user_distance_measurement=result.distance_measurement
                threshold = result.threshold_input
                user_input_type = result.metric_type
                similarity_measure_input=result.similarity_measure_formulae
                # if available
                distance_formulae=result.distance_formulae

                from itertools import combinations
                # with open(File_Path, mode='r',encoding="utf8") as data_file:
                with open(r'C:/Users/Admin/OneDrive/RA/multi layer/Multilayer for Git/datasets/{}'.format(File_Path), mode='r',encoding="utf8") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=',')
                    # a = csv_reader
                    # next(csv_reader)  # This is for excluding the header from the data list
                    combi = combinations(list(csv_reader), 2)
                    # Using If elseif else statement here as artificial switch case is not feasible 
                    if(user_input_type==2):
                        for i in list(combi):
                            #  converting the data in csv to int is not correct. need to change
                            if similarityObj.numeric_metric(int(i[0][int(feature_column)]), int(i[1][int(feature_column)]), int(threshold)):
                                edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))
                    elif(user_input_type==1):
                        for i in list(combi):
                            if similarityObj.nominal_metric(i[0][int(feature_column)],i[1][int(feature_column)]):
                                edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)])) # adds the nodes pass similarity metric has an edge
                    elif(user_input_type==3):
                        if(distance_formulae==Metric_Distance_Measure_enum.EUCLIDEAN.name):
                            for i in list(combi):
                                # need to implement lon1, lat1, lon2, lat2,user_unit,threshold
                                if similarityObj.haversine(i[0][feature_column_longitude],i[0][feature_column_latitude],i[1][feature_column_longitude],i[1][feature_column_latitude],user_distance_measurement,threshold):
                                    edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))
                            # yet to be implemented .....logic for calculating distance and add a edge list
                        # else:
                        #     for i in list(combi):
                        #         if similarityObj.euclidean
                        
                    elif(user_input_type==4):
                        # code for SET type input
                        if(similarity_measure_input==Similarity_Measure_Formulae_enum.JACCARD.name):
                            for i in list(combi):
                                if similarityObj.jaccard_similarity(i[0][int(feature_column)], i[1][int(feature_column)],threshold ):
                                    edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))

                        elif(similarity_measure_input==Similarity_Measure_Formulae_enum.COSINE.name):
                            # code for cosine in set
                            for i in list(combi):
                                if similarityObj.jaccard_similarity(int(i[0][int(feature_column)]), int(i[1][int(feature_column)]),threshold ):
                                    edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))
                        else:
                            # code for pearson
                            for i in list(combi):
                                if similarityObj.jaccard_similarity(int(i[0][int(feature_column)]), int(i[1][int(feature_column)]),threshold ):
                                    edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))
                    elif(user_input_type==5):
                        # code for TEXT type input
                        # for jaccard
                        if(similarity_measure_input==Similarity_Measure_Formulae_enum.JACCARD.name):
                            for i in list(combi):
                                if similarityObj.jaccard_similarity(int(i[0][int(feature_column)]), int(i[1][int(feature_column)]),threshold ):
                                    edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))

                        elif(similarity_measure_input==Similarity_Measure_Formulae_enum.COSINE.name):
                            # code for cosine 
                            for i in list(combi):
                                if similarityObj.jaccard_similarity(int(i[0][int(feature_column)]), int(i[1][int(feature_column)]),threshold ):
                                    edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))
                        else:
                            # code for pearson
                            for i in list(combi):
                                if similarityObj.jaccard_similarity(int(i[0][int(feature_column)]), int(i[1][int(feature_column)]),threshold ):
                                    edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))
                    elif(user_input_type==7):
                        # Code for numeric fixed range
                        for i in list(combi):
                            if similarityObj.numeric_metric_range(int(i[0][int(feature_column)]), int(i[1][int(feature_column)]),list_of_ranges ):
                                edgeList.append(str(i[0][int(node_column)]) + "," + str(i[1][int(node_column)]))
                    else:
                        print("Invalid input provided. Terminating the program. Please check your input format")

                if len(edgeList)!=0:
                    with open(r'C:/Users/Admin/OneDrive/RA/multi layer/Multilayer for Git/datasets/{}'.format(File_Path), mode='r',encoding="utf8") as data_file:
                        csv_reader = csv.reader(data_file, delimiter=',')
                        next(csv_reader)
                        for row in csv_reader:
                            nodeList.append(str(row[0]))
                            line_count += 1

                    # file_name = "layer_file_{}_{}_{}".format(layer+1,feature_column,time.strftime("%Y%m%d-%H%M%S"))
                    file_name_array=File_Path.split('.')
                    file_name="C:/Users/Admin/OneDrive/RA/multi layer/Multilayer for Git/layer_files/layer_file_{}.csv".format(file_name_array[0])
                    # calling layer class to write layer data to a file
                    layerObj.write_layer_file(line_count, edgeList, nodeList, file_name)
                    line_count=0
                    nodeList=[]
                    edgeList=[]
            


            

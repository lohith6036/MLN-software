from math import radians, cos, sin, asin, sqrt

class SimilarityObject:
    def __init__(self):
        print('similarity class initialized')

    # This is for any numeric similarity comparision. Pass the values which need to be compared in obj1 and obj2
    # and the threshold for which the difference can be estimated.

    def numeric_metric(self, obj1, obj2, threshold):
        if (abs(obj1 - obj2)) < threshold:
            return True
        else:
            return False

    def numeric_metric_self(self,obj,threshold):
        if obj<threshold:
            return True
        else:
            return False

    def nominal_metric(self, object1, object2):
        if object1==object2:
            return True
        else:
            return False
            
    def haversine(self, lon1, lat1, lon2, lat2,user_unit,threshold):
        distance = 0
        from haversine import haversine, Unit
        # Calculate distance based on the provided units from user
        if user_unit==Unit.KILOMETERS.name:
            distance = haversine((lon1,lat1),(lon2,lat2),unit=Unit.KILOMETERS)
        elif user_unit==Unit.METERS.name:
            distance = haversine((lon1,lat1),(lon2,lat2),unit=Unit.METERS)
        elif user_unit==Unit.MILES.name:
            distance = haversine((float(lon1),float(lat1)),(float(lon2),float(lat2)),unit=Unit.MILES)
        elif user_unit == Unit.NAUTICAL_MILES.name:
            distance = haversine((lon1,lat1),(lon2,lat2),unit=Unit.NAUTICAL_MILES)
        else:
            return False
    
        # verify if the distance is in threshold or not
        if(distance<threshold):
            return True
        else:
            return False
        
    
    def euclidean(self,list1,list2,threshold ):
            # this method has limitation. It should atlease have a 2 dimentional array or more but not less(1 or 0)
            import math
            # this calculates for n- dimentional arrays .... can give directly array with 2 or 3 dimentional elements
            distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(list1, list2)]))

            if(distance<threshold):
                return True
            else:
                return False

    def numeric_metric_range(self,input1,input2,list):
        # Code for checking if the provided input1 and input2 are in any range available in the list(have multiple ranges)
        # If both input1 and input2 are in same range, then we have a edge and return true from this method else false
        isSimilar=False
        for element in list:
            if (element[0] <= input1 <= element[1]):
                if (element[0] <= input2 <= element[1]):
                    isSimilar = True
                else:
                    isSimilar = False
            else:
                isSimilar = False
        return isSimilar
        
    def cosine_similarity(self,input):
        return False
    
    # list accepts integer, float and string types and similarity ranges from 0.0 - 1.0
    def jaccard_similarity(self,list_1,list_2,threshold):
        # remove , from the array and convert it into a list
        list1=set(list_1.split(','))
        list2=set(list_2.split(','))
        common = list1.intersection(list2)
        similarity=float(len(common)) / (len(list1) + len(list2) - len(common))
        if (similarity>=threshold):
            return True
        else:
            return False

        # """
        # https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
        # Calculate the great circle distance between two points
        # on the earth (specified in decimal degrees)
        # """
        # # convert decimal degrees to radians
        # lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # # haversine formula
        # dlon = lon2 - lon1
        # dlat = lat2 - lat1
        # a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        # c = 2 * asin(sqrt(a))
        # r = 3956  # Radius of earth in kilometers. Use 3956 for miles and 6371 for kms
        # return c * r

    # def geometric(self,lon1,lat1,lon2,lat2,threshold):
    #     distance = SimilarityObject.haversine(lon1,lat1,lon2,lat2)
    #     return SimilarityObject.numeric_metric_self(distance, threshold)

import requests
import math
from columnar import columnar

URL_PATH = "https://nominatim.openstreetmap.org/search.php"
# ORIGIN = ["New Mexico Museum of Natural History & Science", "New Mexico Museum of Natural History & Science",
#           "New Mexico Museum of Natural History & Science", "New Mexico Museum of Natural History & Science",
#           "New Mexico Museum of Natural History & Science"]

# Had to truncate these values 
ORIGIN = ["New Mexico Museum of Natural Hist", "New Mexico Museum of Natural Hist",
          "New Mexico Museum of Natural Hist", "New Mexico Museum of Natural Hist",
          "New Mexico Museum of Natural Hist"]


def get_lat_lon(location):
    PARAMS = {'q': location, 'format': 'jsonv2'}

    # send a GET request and save response object to variable
    r = requests.get(url=URL_PATH, params=PARAMS)

    # extract data from response object in and parse json data
    data = r.json()

    # print data for investigative purposes
    # print(data)

    latitude = float(data[0]['lat'])
    longitude = float(data[0]['lon'])
    return [latitude, longitude]


# end def get_lat_lon(location):


def selection_sort(array):
    # taken from:
    # https://big-o.io/algorithms/comparison/selection-sort/
    print("in selectionsort: ", array)
    # step 1: loop from the beginning of the array to the second to last item
    currentIndex = 0
    while (currentIndex < len(array) - 1):
        # step 2: save a copy of the currentIndex
        minIndex = currentIndex
        # step 3: loop through all indexes that proceed the currentIndex
        i = currentIndex + 1
        while (i < len(array)):
            # step 4:   if the value of the index of the current loop is less
            #           than the value of the item at minIndex, update minIndex
            #           with the new lowest value index
            if (array[i] < array[minIndex]):
                # update minIndex with the new lowest value index
                minIndex = i
            i += 1
        # step 5: if minIndex has been updated, swap the values at minIndex and currentIndex
        if (minIndex != currentIndex):
            temp = array[currentIndex]
            array[currentIndex] = array[minIndex]
            array[minIndex] = temp
        currentIndex += 1

    return array


def calculate_distance(orig, dest):
    # dlon = lon2 -lon1
    dlon = dest[1] - orig[1]
    # dlat = lat2 - lat1
    dlat = dest[0] - orig[0]
    # a = (sin(dlat/2))^2 + cos(lat2) * cos(lat2) * (sin(dlon/2))^2
    a = (math.sin(math.radians(dlat / 2))) ** 2 + \
        math.cos(math.radians(orig[0])) * \
        math.cos(math.radians(dest[0])) * \
        (math.sin(math.radians(dlon / 2))) ** 2
    # c = 2 * atan( sqrt(a), sqrt(1-a) )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    R = 3961
    d = R * c

    return d


# end def calculate_distance(orig, dest)


def calc(dest):
    # calculate distance
    loc1 = get_lat_lon("New Mexico Museum of Natural History & Science")
    loc2 = get_lat_lon(dest)
    return calculate_distance(loc1, loc2)

    # Python program to get transpose
    # elements of two dimension list


# end of def capture(dest):

# Python program to get transpose
# elements of two dimension list
# taken from : https://www.geeksforgeeks.org/python-transpose-elements-of-two-dimensional-list/
def transpose(l1, l2):
    # iterate over list l1 to the length of an item
    for i in range(len(l1[0])):
        # print(i)
        row = []
        for item in l1:
            # appending to new list with values and index positions
            # i contains index position and item contains values
            row.append(item[i])
        l2.append(row)
    return l2


# end of def transpose(l1, l2):


def main():
    # Strings below can be replaced with full street addresses too.

    # array of destinations
    dest = ["New Mexico Highlands University", "Carlsbad Caverns National Park", "Grand Canyon National Park",
            "Mesa Verde National Park", "White Sands National Park"]

    # get the calculated distnaces and convert from map to list
    dist = list(map(calc, dest))
    # print(dist)

    # coordinated sort
    # taken from:
    # https://stackoverflow.com/questions/9764298/how-to-sort-two-lists-which-reference-each-other-in-the-exact-same-way
    dist, dest = zip(*selection_sort(list(zip(dist, dest))))
    # print("Destination: ", dest)
    # print("Distance: ", dist)
    # print("dist: ", dist)

    # round each element
    # taken from:
    # https://stackoverflow.com/questions/36982858/object-of-type-map-has-no-len-in-python-3
    rdist = list(map(lambda dist: round(dist), dist))
    # print(rdist)

    # taken from:
    # https://stackoverflow.com/questions/9989334/create-nice-column-output-in-python
    headers = ['From',
               'To',
               'Distance'
               ]

    data = [ORIGIN, dest, rdist]

    # provide an empty array
    pivot = []

    # transpose rows and columns
    tbl = transpose(data, pivot)
    #print("tbl: ", tbl)

    table = columnar(tbl, headers, no_borders=True)
    print(table)

    print("Distance is given in units of miles...\n")
    # provide an empty array
    pivot = []
    #print("transpose: ", transpose(data, pivot))


# end def main():

if __name__ == "__main__":
    main()

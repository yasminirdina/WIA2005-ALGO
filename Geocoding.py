from typing import List, Any
import time
start_time = time.time()

from geopy.geocoders import Nominatim
from gmplot import gmplot
from geopy.distance import geodesic

def find_coordinate(loc):
    geolocator = Nominatim(user_agent="A-GoGo", timeout = 60)
    location = geolocator.geocode(loc)
    coord = location.latitude, location.longitude

    return coord

def plotPoints(coord_arr, color_arr, shortest_lat_arr, shortest_long_arr, gmap, line, color_line_arr):
    for i in range(len(coord_arr)):
        #get the latitude and longitude
        lat = (coord_arr[i])[0]
        long = (coord_arr[i])[1]
        loc_lats, loc_longs = zip(*[(lat, long)])
        #save the point on map
        gmap.scatter(loc_lats, loc_longs, color=color_arr[i], size=300, marker=False)

    #the "line" parameter in this function acts as an indicator to identify whether-
    #-we are trying to plot POINTS or LINES
    #0 = points, else = lines
    #if want to draw lines as well, call plotLine function
    if(line != 0):
        plotLine(shortest_lat_arr, shortest_long_arr, color_line_arr, line, gmap)
    #if want to plot points only (Question 1), draw it immediately on the map
    else:
        gmap.draw("A-GoGo_map.html")

    return gmap

def plotLine(shortest_lat_arr, shortest_long_arr, color_line_arr, line,  gmap):
    #will only draw lines on map + the previously saved POINTS if this function is called.
    for i in range(0, line):
        gmap.plot(shortest_lat_arr[i], shortest_long_arr[i], color=color_line_arr[i], edge_width=3)

    gmap.draw("A-GoGo_map.html")

#calculate distance between 2 points
def calc_distance(coordinate_points_start_i, coordinate_points_dest_i, points_i):
    point_split = points_i.split(", ")
    start_point = coordinate_points_start_i.split(", ")
    dest_point = coordinate_points_dest_i.split(", ")
    start = (start_point[0], start_point[1])
    destination = (dest_point[0], dest_point[1])
    point_distance = round(((geodesic(start, destination).miles)*1.609), 2)
    print("Distance between {0} - {1}: {2}km". format(point_split[0], point_split[1], point_distance))

    return point_distance

"""
#find shortest path randomly by checking each time through 27 points a.k.a AFTER ALGORITHM IS CHOSEN
def find_shortest(points, initial, min, transport, point_distance):
    total_distance = 0
    shortest_path = initial
    start_loc = initial
    min_index = 0
    pathDist = []
    while(start_loc != "Georgetown Pulau Pinang"):
        for k in range(len(points)):
            point_split = points[k].split(", ")
            if(point_split[0] == start_loc):
                if(point_distance[k] < min):
                    min = point_distance[k]
                    min_index = k
        total_distance += min
        point_split = points[min_index].split(", ")
        shortest_path += "(" + transport[min_index] + ") - " + point_split[1]
        start_loc = point_split[1]
        min = 500

    pathDist.append(shortest_path)
    pathDist.append(total_distance)
    return pathDist
"""

#find shortest path from 10 paths a.k.a BEFORE ALGORITHM IS CHOSEN
def find_shortest1(paths, points, min_init, transport, point_distance):
    min_index = 0
    min_dist = min_init
    minPathDist = []
    allPathDist = [] #store distances of all 10 paths

    #iterate through each path and split each path at each iteration
    for i in range(len(paths)):
        total_distance = 0
        paths_split = paths[i].split(" - ")

        #for the i-th iteration of paths, iterate through each splitted i-th path
        for j in range(len(paths_split) - 1):
            #extract start location/point by finding the '(' which indicates the start letter of transport used
            #by finding the index/position of '(', so later we only extract until before the index je
            #same goes to destination location and trans used (we use the start trans)
            divide_start = paths_split[j].find("(")
            start_loc = (paths_split[j])[0: divide_start: 1]
            start_trans = (paths_split[j])[divide_start + 1: len(paths_split[j]) - 1: 1]
            divide_dest = paths_split[j+1].find("(")

            #this one for the lasssst point in every path (sebab "Georgetown Pulau Pinang" takda "(" so when we use "find("(")", akan return -1 instead of any index
            if (divide_dest != -1):
                dest_loc = (paths_split[j+1])[0: divide_dest: 1]
                #print("[CHECK] Dest loc: ", dest_loc)
            else:
                dest_loc = paths_split[j+1]
                #print("[CHECK] Dest loc: ", dest_loc)

            #after we indicate start, dest and trans used for a particular point from a path, iterate through the "points" array, untuk get the distance
            for k in range(len(points)):
                point_split = points[k].split(", ")
                #print("current k: ", k)
                #print("point split: ", point_split)
                #print("\n[CHECK] trans at {0}: {1}".format(k, transport[k]))
                if(start_loc == point_split[0] and dest_loc == point_split[1] and start_trans == transport[k]):
                    #print("\n[CHECK] !!! yeay masuk sini !!!")
                    #once found, just accumulate dekat total_distance
                    total_distance += point_distance[k]
                    #break because we don't want to waste processing time lepas dah dpt distance
                    break

        #store distance of current path
        allPathDist.append(round(total_distance, 2))

        #print("\n[CHECK] total distance path {0}= {1}".format(i, total_distance))
        #check minimum distance here, and get the min index
        if(total_distance < min_dist):
            min_dist = round(total_distance, 2)
            min_index = i
            #print("[CHECK] min: ", total_distance)
            #print("[CHECK] min_index: ", min_index)
        #print("\n--------------------------")

    #once dah habis, append the shortest path and the distance
    minPathDist.append(paths[min_index])
    minPathDist.append(min_dist)
    return minPathDist, allPathDist, min_index

#method to get coord for drawing polyline
def getCoordPolyline(pathDistx):
    shortest_split = pathDistx.split(" - ")
    shortest_point_coord = []
    #shortest_point_lat = []
    #shortest_point_long = []
    for j in range(len(shortest_split) - 1):
        divide_start = shortest_split[j].find("(")
        start_loc = (shortest_split[j])[0: divide_start: 1]
        shortest_point_coord.append(find_coordinate(start_loc))
        #shortest_point_lat = (shortest_point_coord[j])[0]
        #shortest_point_long = (shortest_point_coord[j])[1]
        #print("Shortest point latitude at j = {0} - {1}".format(j, shortest_point_lat))
        #print("Shortest point longitude at j = {0} - {1}\n".format(j, shortest_point_long))
        divide_dest = shortest_split[j+1].find("(")
        if (divide_dest == -1):
            start_loc = (shortest_split[j+1])
            shortest_point_coord.append(find_coordinate(start_loc))
            #shortest_point_lat = (shortest_point_coord[j])[0]
            #shortest_point_long = (shortest_point_coord[j])[1]
            #print("Shortest point latitude at j = {0} - {1}".format(j+1, shortest_point_lat))
            #print("Shortest point longitude at j = {0} - {1}".format(j+1, shortest_point_long))
            break

    return shortest_point_coord

def calc_distance_weightage(allPathDist):
    dist_wt = []
    min_dist = min(allPathDist)
    max_dist = max(allPathDist)

    for i in range(len(allPathDist)):
        if (allPathDist[i] >= min_dist) and (allPathDist[i] < (min_dist + 50)):
            dist_wt.append(50)
        elif (allPathDist[i] >= (min_dist + 50)) and (allPathDist[i] < (min_dist + (50 * 2))):
            dist_wt.append(40)
        elif allPathDist[i] >= (min_dist + (50 * 2)) and (allPathDist[i] < (min_dist + (50 * 3))):
            dist_wt.append(30)
        elif allPathDist[i] >= (min_dist + (50 * 3)) and (allPathDist[i] < (min_dist + (50 * 4))):
            dist_wt.append(20)
        elif allPathDist[i] >= (min_dist + (50 * 4)) and (allPathDist[i] <= max_dist):
            dist_wt.append(10)

    return dist_wt

#Calculate total weightage for all paths
def calc_total_weightage(dist_wt, trans_wt, paths, allPathDist):
    total_wt = []
    total_trans_wt_i = 0
    start = 0
    cnt_trans = 0
    print("<--- QUESTION 10: Post-sentiment analysis summary --->\n")
    for i in range(len(paths)):
        paths_split = paths[i].split(" - ")
        total_trans_wt_i = 0
        cnt_trans = 0
        for j in range(len(paths_split) - 1):
            divide_start = paths_split[j].find("(")
            start_trans = (paths_split[j])[divide_start + 1: len(paths_split[j]) - 1: 1]

            if start_trans == "MRT Bus" or start_trans == "Rapid KL Bus" or start_trans == "Bus":
                total_trans_wt_i += (trans_wt[0])[1]
                cnt_trans += 1
                continue

            if start_trans == "KTM Train" or start_trans == "ETS Train" or start_trans == "KLIA Transit":
                total_trans_wt_i += (trans_wt[1])[1]
                cnt_trans += 1
                continue

            if start_trans == "LRT Train" or start_trans == "MRT Train":
                total_trans_wt_i += (trans_wt[2])[1]
                cnt_trans += 1
                continue

            if start_trans == "Grab":
                total_trans_wt_i += (trans_wt[3])[1]
                cnt_trans += 1
                continue

            if start_trans == "Ferry":
                total_trans_wt_i += (trans_wt[4])[1]
                cnt_trans += 1
                continue

            if start_trans == "Flight":
                total_trans_wt_i += (trans_wt[5])[1]
                cnt_trans += 1
                continue

            if start_trans == "Walk":
                total_trans_wt_i += (trans_wt[6])[1]
                cnt_trans += 1
                continue

        print("[Path {0}]".format(i+1))
        total_trans_wt_i = round(((total_trans_wt_i/cnt_trans) * 0.5), 2) #max weightage for sentiment is 50% only for one path
        total_wt.append(total_trans_wt_i + dist_wt[i])
        print("Total distance: ", allPathDist[i])
        print("Total distance weightage: ", dist_wt[i])
        print("Total transportation weightage: ", total_trans_wt_i)
        print("Total weightage: {0}\n".format(total_wt[i]))

    return total_wt

#MAIN
if __name__ == "__main__":
    coord_georgetown = find_coordinate("Georgetown, Pulau Pinang")

    points = [("University of Malaya, Phileo Damansara"),
              ("Phileo Damansara, KL Sentral"),
              ("KL Sentral, Kuala Lumpur International Airport"),
              ("Kuala Lumpur International Airport, Penang International Airport"),
              ("Penang International Airport, Georgetown Pulau Pinang"),
              ("University of Malaya, KL Sentral"),
              ("KL Sentral, Kuala Lumpur International Airport"),
              ("KL Sentral, KTM Butterworth"),
              ("KTM Butterworth, Sultan Abdul Halim Ferry Terminal"),
              ("Sultan Abdul Halim Ferry Terminal, Penang Ferry"),
              ("Penang Ferry, Georgetown Pulau Pinang"),
              ("Kuala Lumpur International Airport, Sultan Abdul Halim Airport"),
              ("Sultan Abdul Halim Airport, KTM Alor Setar"),
              ("KTM Alor Setar, KTM Butterworth"),
              ("University of Malaya, LRT Universiti"),
              ("LRT Universiti, KL Sentral"),
              ("KL Sentral, KTM Butterworth"),
              ("KTM Butterworth, Sultan Abdul Halim Ferry Terminal"),
              ("KL Sentral, Terminal Bersepadu Selatan"),
              ("Terminal Bersepadu Selatan, KOMTAR Bus Terminal"),
              ("KOMTAR Bus Terminal, Georgetown Pulau Pinang"),
              ("University of Malaya, LRT Universiti"),
              ("LRT Universiti, KLCC"),
              ("KLCC, Persiaran Hampshire"),
              ("Persiaran Hampshire, Queensbay Mall"),
              ("Queensbay Mall, Georgetown Pulau Pinang"),
              ("Penang International Airport, Georgetown Pulau Pinang")]

    transport = ["MRT Bus", "MRT Train", "KLIA Transit", "Flight",
                 "Bus", "Grab", "Bus", "KTM Train",
                 "Grab", "Ferry", "Walk", "Flight",
                 "Grab", "KTM Train", "Rapid KL Bus", "LRT Train",
                 "ETS Train", "Walk", "KLIA Transit", "Bus",
                 "Bus", "Walk", "LRT Train", "Walk",
                 "Bus", "Bus", "Grab"]

    paths = ["University of Malaya(MRT Bus) - Phileo Damansara(MRT Train) - KL Sentral(KLIA Transit) - Kuala Lumpur International Airport(Flight) - Penang International Airport(Bus) - Georgetown Pulau Pinang",
             "University of Malaya(Grab) - KL Sentral(Bus) - Kuala Lumpur International Airport(Flight) - Penang International Airport(Grab) - Georgetown Pulau Pinang",
             "University of Malaya(MRT Bus) - Phileo Damansara(MRT Train) - KL Sentral(KTM Train) - KTM Butterworth(Grab) - Sultan Abdul Halim Ferry Terminal(Ferry) - Penang Ferry(Walk) - Georgetown Pulau Pinang",
             "University of Malaya(Grab) - KL Sentral(Bus) - Kuala Lumpur International Airport(Flight) - Sultan Abdul Halim Airport(Grab) - KTM Alor Setar(KTM Train) - KTM Butterworth(Grab) - Sultan Abdul Halim Ferry Terminal(Ferry) - Penang Ferry(Walk) - Georgetown Pulau Pinang",
             "University of Malaya(Rapid KL Bus) - LRT Universiti(LRT Train) - KL Sentral(ETS Train) - KTM Butterworth(Grab) - Sultan Abdul Halim Ferry Terminal(Ferry) - Penang Ferry(Walk) - Georgetown Pulau Pinang",
             "University of Malaya(Grab) - KL Sentral(ETS Train) - KTM Butterworth(Walk) - Sultan Abdul Halim Ferry Terminal(Ferry) - Penang Ferry(Walk) - Georgetown Pulau Pinang",
             "University of Malaya(Grab) - KL Sentral(KLIA Transit) - Terminal Bersepadu Selatan(Bus) - KOMTAR Bus Terminal(Bus) - Georgetown Pulau Pinang",
             "University of Malaya(Walk) - LRT Universiti(LRT Train) - KLCC(Walk) - Persiaran Hampshire(Bus) - Queensbay Mall(Bus) - Georgetown Pulau Pinang",
             "University of Malaya(Walk) - LRT Universiti(LRT Train) - KL Sentral(ETS Train) - KTM Butterworth(Walk) - Sultan Abdul Halim Ferry Terminal(Ferry) - Penang Ferry(Walk) - Georgetown Pulau Pinang",
             "University of Malaya(Walk) - LRT Universiti(LRT Train) - KL Sentral(KLIA Transit) - Kuala Lumpur International Airport(Flight) - Penang International Airport(Grab) - Georgetown Pulau Pinang"]

    #Initialize map
    apikey = 'AIzaSyDcWlSerV4kKJELxEimH0ZNkGNqeavi2Tc'
    center = find_coordinate("Seri Iskandar, Perak")
    gmap = gmplot.GoogleMapPlotter(center[0], center[1], 8, apikey=apikey)
    coord_arr = []
    color_arr = []
    shortest_lat_arr = []
    shortest_long_arr = []
    color_line_arr = []

    #store coordinates and point colors of ALL possible points (read: vertices) to get to the destination
    #in two separate arrays, without redundant points
    for i in range(len(points)):
        loc = points[i].split(", ")

        #if reach the last points,  take the second part of it (Georgetown a.k.a the destination)
        if(i == len(points) - 1):
            #print("[CHECK] last point\n")

            coord_i = find_coordinate(loc[1])
            if(loc[1] == "University of Malaya"):
                color_i = "blue"
            elif(loc[1] == "Georgetown, Pulau Pinang"):
                color_i = "red"
            else:
                color_i = "purple"
        #before reaching the last point, take the first part of points (the starting)
        #and take note the color
        else:
            coord_i = find_coordinate(loc[0])
            if(loc[0] == "University of Malaya"):
                color_i = "blue"
            elif(loc[0] == "Georgetown, Pulau Pinang"):
                color_i = "red"
            else:
                color_i = "purple"

        #check if the same coordinate & color have been inserted in the array, to avoid redundancy
        if(coord_i not in coord_arr):
            coord_arr.append(coord_i)
            color_arr.append(color_i)

    #call plotPoints function to draw the scattered points on map
    #will return gmap object to save the previous plots
    print("<--- QUESTION 1: Plotting all points on the map. --->\n")
    print("10 paths options: ")
    for i in range(len(paths)):
        print("[Path {0}]: {1}".format(i+1, paths[i]))
    print("")
    gmap = plotPoints(coord_arr, color_arr, shortest_lat_arr, shortest_long_arr, gmap, 0, color_line_arr)

    print("All points are plotted! Check A-GoGo_map.html to view the map.\n")

    #create 2 array to store start and detination points' coordinates separately
    coordinate_points_start = []
    coordinate_points_dest = []

    #store coordinates of the 27 start-destination points in array coordinate_points_start and xxx_dest in term "lats, long"
    for i in range(len(points)):
        #print("current i = ", i)
        point_split = points[i].split(", ")
        start_i_coord = find_coordinate(point_split[0])
        dest_i_coord = find_coordinate(point_split[1])
        coordinate_points_start.append(str(start_i_coord[0]) + ", " + str(start_i_coord[1]))
        coordinate_points_dest.append(str(dest_i_coord[0]) + ", " + str(dest_i_coord[1]))

    #create array to store distance between start-dest points (for further comparison to find shortest path from UM - Georgetown)
    point_distance = []

    #store distance between start-dest points
    print("<--- QUESTION 2: Calculating distances between the stops. --->\n")
    for j in range(len(coordinate_points_start)):
        point_distance.append(calc_distance(coordinate_points_start[j], coordinate_points_dest[j], points[j]))

    print("")

    #algorithm for finding shortest path
    # 1: find shortest from 10 chosen routes
    allPathDist = []
    min_init = 500
    min_index = 0
    pathDist1, allPathDist, min_index = find_shortest1(paths, points, min_init, transport, point_distance)
    print("<--- QUESTION 3: Generating the shortest path (distance-based). --->\n")
    print("List of distances for all paths: \n", allPathDist)
    print("\nShortest path is path {0}: \n{1}".format(min_index + 1, pathDist1[0]))
    print("\nShortest path's distance: {0} km\n".format(pathDist1[1]))

    """
    # 2: random combination after checking between all 27 points
    min = 500
    initial = "University of Malaya"
    pathDist = find_shortest(points, initial, min, transport, point_distance)
    print("-----AFTER ALGORITHM IS CHOSEN-----")
    print("Shortest path: ", pathDist[0])
    print("Shortest distance: {0} km\n".format(pathDist[1]))
    """

    #Getting coordinates for shortest path to draw polyline
    #print("-----GETTING COORDS FOR POLYLINE BEFORE ALGORITHM IS CHOSEN----")
    b_shortest_points_coords = getCoordPolyline(pathDist1[0])

    """
    print("\n-----GETTING COORDS FOR POLYLINE AFTER ALGORITHM IS CHOSEN----")
    a_shortest_points_coords = getCoordPolyline(pathDist)
    """

    #draw line for shortest path (before)
    shortest_lat_arr = []
    shortest_long_arr = []
    lat_arr = []
    long_arr = []
    for i in range(len(b_shortest_points_coords)):
        lat_arr.append((b_shortest_points_coords[i])[0])
        long_arr.append((b_shortest_points_coords[i])[1])

    shortest_lat_arr.append(lat_arr)
    shortest_long_arr.append(long_arr)
    color_line_arr.append("Green")

    #plot the shortest path's line on map by passing the arguments: shortest latitude & longitude array,
    #points coordinates array, points color array, gmap object, line = 1 indicating we want to draw first line + points
    #color_line = "green" indicating this line we are trying to draw at the moment is green in color.
    print("<--- QUESTION 4: Plotting line to illustrate the origin location, stops and the destination based on shortest path in QUESTION 3. --->\n")
    plotPoints(coord_arr, color_arr, shortest_lat_arr, shortest_long_arr, gmap, 1, color_line_arr)

    print("Line 1 [Green]: Shortest path (pre-sentiment analysis) has been drawn successfully! Check the A-GoGo_map.html file to view the map.\n")

    """
    #line 2
    lat_arr = []
    long_arr = []
    for i in range(len(a_shortest_points_coords)):
        lat_arr.append((a_shortest_points_coords[i])[0])
        long_arr.append((a_shortest_points_coords[i])[1])

    shortest_lat_arr.append(lat_arr)
    shortest_long_arr.append(long_arr)
    color_line_arr.append("Black")

    #plot the shortest path's line on map by passing the arguments: shortest latitude & longitude array,
    #points coordinates array, points color array, gmap object, line = 2 indicating we want to draw the second line + points
    #color_line = "green" indicating this line we are trying to draw at the moment is green in color.
    plotPoints(coord_arr, color_arr, shortest_lat_arr, shortest_long_arr, gmap, 2, color_line_arr)

    print("\nShortest path's line 2 drawn successfully!")
    """

    print("List of distances of all 10 paths: \n", allPathDist)

    #giving weightage for all paths' distances
    dist_wt = calc_distance_weightage(allPathDist)

    print("\nList of the distance weightage for all 10 paths: \n",dist_wt)
    print("")

    #Question 10
    import trygraph
    trygraph.calc_sentiment_weightage()
    sent_wt = []
    sent_wt = trygraph.trans_wt

    #print("\nsent_wt: ", sent_wt)

    total_wt = []
    total_wt = calc_total_weightage(dist_wt, sent_wt, paths, allPathDist)

    print("List of total weightage for all 10 paths: \n", total_wt)

    opt_total_wt = max(total_wt)
    opt_path_index = total_wt.index(opt_total_wt)

    print("\nThe most optimum path (based on both distance and sentiment is path {0}:".format(opt_path_index + 1))
    print(paths[opt_path_index])

    #Get coordinates for drawing line 2
    opt_shortest_coords = getCoordPolyline(paths[opt_path_index])

    #drawing line 2
    lat_arr = []
    long_arr = []
    for i in range(len(opt_shortest_coords)):
        lat_arr.append((opt_shortest_coords[i])[0])
        long_arr.append((opt_shortest_coords[i])[1])

    shortest_lat_arr.append(lat_arr)
    shortest_long_arr.append(long_arr)
    color_line_arr.append("Black")

    #plot the shortest path's line on map by passing the arguments: shortest latitude & longitude array,
    #points coordinates array, points color array, gmap object, line = 2 indicating we want to draw the second line + points
    #color_line = "green" indicating this line we are trying to draw at the moment is green in color.
    plotPoints(coord_arr, color_arr, shortest_lat_arr, shortest_long_arr, gmap, 2, color_line_arr)

    print("\nLine 2 [Black]: Shortest path (post-sentiment analysis) has been drawn successfully! Check the A-GoGo_map.html file to view the map.")

    print("\n------------------------------------------------------------------------------------------------------------------------------------\n")

    print("Time elapsed: {:.2f}s\n".format(time.time() - start_time))

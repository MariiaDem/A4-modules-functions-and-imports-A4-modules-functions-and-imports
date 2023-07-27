"""Getting input from user and communication with special API to get the route

This file can also be imported as a module and contains the following
functions:

    * starting_coord_by_user - allows user to enter starting point coordinates
    * finishing_coord_by_user - allows user to choose destination point coordinates
    * get_directions_response - sending request to the Route and directions API and getting response 

"""
def starting_coord_by_user():
    """Allows user to input their own coordinates for the starting point of a route

    Returns: list
    User-defined coordinates as a list.
    """
    print("Please enter your starting coordinates here:")
    lat = float(input("Enter latitude: "))
    long = float(input("Enter longitude: "))
    coordinates = [lat,long]
    print("Your starting coordinates: " + str(coordinates))
    
    return coordinates

def finishing_coord_by_user(df):
    """Allows user to choose destination point coordinates in list from pandas data frame
    Parameters:
    ------------------
    df: pandas.DataFrame

    Returns: list
    User-defined coordinates as a list.
    """
        
    print("Please choose your destination point:\n")
    for row in range(0,len(df)):
        print(row, df['name'][row])
    number = int(input("Enter number "))
    coord = df['coordinates'][number]
    lat = coord[0]
    long = coord[1]
    coordinates = [lat,long]
    print("Your destination point coordinates: " + str(coordinates))
    
    return coordinates

import requests

def get_directions_response(lat1, long1, lat2, long2, mode='drive'):
    """Sending request to the Route and directions API and getting response with array of coordinates of route
    
    Parameters:
    ------------------
    lat1:  latitude of the starting point
    long1: longitude of the starting point
    lat2: latitude of the finish point
    long2: longitude of the finith point
    mode: mode of the route, it may be "drive", "truck", "bicycle", "walk" or "transit"

    Returns: GeoJSON.Features
    Information about the route
    """
    
    
    url = "https://route-and-directions.p.rapidapi.com/v1/routing"
    key = "9ac082c230msh06a9665fe45fb1ap1d6299jsn9101a5141ae9"
    host = "route-and-directions.p.rapidapi.com"
    headers = {"X-RapidAPI-Key": key, "X-RapidAPI-Host": host}
    querystring = {"waypoints":f"{str(lat1)},{str(long1)}|{str(lat2)},{str(long2)}","mode":mode}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

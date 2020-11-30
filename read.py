import csv  

def readJoints(filename):
    point = []
    points = []
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=';')

        for row in reader:
            point.append(row[1])
            point.append(row[2])
            point.append(row[3])
            points.append(point)
            point = []
    
    return points

def readFile(source):
    i = 1
    s = open(source, "r")

    lines = s.readlines()
    length = len(lines)
    point = []
    point.append(lines[0])
    points = []

    while i<length:
        if i%20 == 0:
            points.append(point)
            point = []
            point.append(lines[i])
        else:
            point.append(lines[i])
        
        i = i+1;
            
    points.append(point)
    return points

def retrieveCoordinates(frame):
    coordinates = []

    for bodyPart in frame:
        string = bodyPart.split(';')

        x = float(string[1])
        z = float(string[2])
        y = -float((string[3].split())[0])

        coordinates.append([x, y, z])

    return coordinates

def retrieveLine(node1, node2, data):
    return [[data[node1][0], data[node2][0]], [data[node1][1], data[node2][1]], [data[node1][2], data[node2][2]]]
    

def retrieveFrame(data):
    frame = [retrieveLine(0, 1, data),
         retrieveLine(1, 2, data),
         retrieveLine(1, 3, data),
         retrieveLine(2, 4, data),
         retrieveLine(3, 5, data),
         retrieveLine(4, 6, data),
         retrieveLine(5, 7, data),
         retrieveLine(6, 8, data),
         retrieveLine(7, 9, data),
         retrieveLine(1, 10, data),
         retrieveLine(10, 11, data),
         retrieveLine(11, 12, data),
         retrieveLine(11, 13, data),
         retrieveLine(12, 14, data),
         retrieveLine(13, 15, data),
         retrieveLine(14, 16, data),
         retrieveLine(15, 17, data),
         retrieveLine(16, 18, data),
         retrieveLine(17, 19, data)]

    return frame    

def getVerticalAnkleLeft(data):
    ankleLeftData = []

    for frame in data:
        string = frame[17].split(';')

        ankleLeftData.append(float(string[2]))
    return ankleLeftData

def getVerticalAnkleRight(data):
    ankleRightData = []

    for frame in data:
        string = frame[16].split(';')

        ankleRightData.append(float(string[2]))
    return ankleRightData

text = readFile("3.txt")

def readRightSS(filename):
    s = open(filename, "r")

    RightSS = []
    lines = s.readlines()
    
    string=lines[0].split()
    RightSS = [[int(num) for num in string]]

    string =lines[1].split()
    RightSS.append([int(num) for num in string])  

    return RightSS

def readLeftSS(filename):
    i = 1
    s = open(filename, "r")

    LeftSS = []
    lines = s.readlines()
    
    string=lines[2].split()
    LeftSS = [int(num) for num in string]

    return LeftSS
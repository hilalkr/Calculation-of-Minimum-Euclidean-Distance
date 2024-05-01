import math

points = [(2, 3), (5, 6), (8, 9), (10, 12)]


def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance


distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
        
min_distance = min(distances)
print("Minimum Distance", min_distance)
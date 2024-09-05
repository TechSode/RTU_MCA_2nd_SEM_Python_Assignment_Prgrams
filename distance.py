import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

if __name__ == "__main__":
    # Take input from the user
    x1 = float(input("Enter the x-coordinate of the first point: "))
    y1 = float(input("Enter the y-coordinate of the first point: "))
    x2 = float(input("Enter the x-coordinate of the second point: "))
    y2 = float(input("Enter the y-coordinate of the second point: "))

    # Calculate the distance
    dist = calculate_distance(x1, y1, x2, y2)

    # Display the result
    print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is {dist:.2f}")
import math


def main():
    x1 = float(input("First coord x: "))
    y1 = float(input("First coord y: "))
    x2 = float(input("Second coord x: "))
    y2 = float(input("Second coord y: "))
    difference_x = x2-x1
    difference_y = y2-y1
    dist = math.sqrt(difference_x**2 + difference_y**2)
    print("The distance between those points is", dist)


if __name__ == "__main__":
    main()

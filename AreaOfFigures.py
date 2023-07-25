from math import pi

figure = input()

if figure == "square":
    a_square = float(input())
    area_square = a_square * a_square
    print(f"{area_square:.3f}")

if figure == "rectangle":
    a_rectangle = float(input())
    b_rectangle = float(input())
    area_rectangle = a_rectangle * b_rectangle
    print(f"{area_rectangle:.3f}")

if figure == "circle":
    r_circle = float(input())
    area_circle = pi * r_circle * r_circle
    print(f"{area_circle:.3f}")

if figure == "triangle":
    a_triangle = float(input())
    h_triangle = float(input())
    area_triangle = (a_triangle * h_triangle) / 2
    print(f"{area_triangle:.3f}")
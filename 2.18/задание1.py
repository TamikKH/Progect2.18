#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse
import json
import os


def circle(rad):
    """
    Функция для вычисления площади круга.
    """
    return 3.14 * rad ** 2


def cylinder(radius, height, full_area=False):
    """
    Функция для вычисления площади цилиндра.
    """
    side_area = 2 * 3.14 * radius * height
    if full_area:
        return side_area + 2 * circle(radius)
    else:
        return side_area


def save_to_json(data, file_name):
    """
    Функция для сохранения данных в файл JSON.
    """
    with open(file_name, 'w') as file:
        json.dump(data, file)


def load_from_json(file_name):
    """
    Функция для чтения данных из файла JSON.
    """
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data
    else:
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Calculate the surface area of a cylinder and save data to JSON file")
    parser.add_argument("radius", type=float, help="Radius of the cylinder")
    parser.add_argument("height", type=float, help="Height of the cylinder")
    parser.add_argument("--full-area", action="store_true", help="Calculate full surface area of the cylinder")
    parser.add_argument("--data", help="Name of the data file")

    args = parser.parse_args()

    radius = args.radius
    height = args.height
    full_area = args.full_area

    # Получение имени файла данных из переменной окружения, если параметр --data не указан
    if args.data:
        file_name = args.data
    elif os.environ.get('CYLINDER_DATA'):
        file_name = os.environ.get('CYLINDER_DATA')
    else:
        file_name = "cylinder_data.json"

    area = cylinder(radius, height, full_area)
    print("Surface area of the cylinder:", area)

    data = {"radius": radius, "height": height, "full_area": full_area, "area": area}
    save_to_json(data, file_name)

    loaded_data = load_from_json(file_name)
    if loaded_data:
        print("Data from file:", loaded_data)
    else:
        print("File not found or empty.")
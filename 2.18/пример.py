#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse
import json
import os


def input_data():
    n = int(input("Введите количество сотрудников: "))
    employees = []
    for _ in range(n):
        surname = input("Введите фамилию и инициалы работника: ")
        position = input("Введите название занимаемой должности: ")
        year = int(input("Введите год поступления на работу: "))
        employees.append({"фамилия и инициалы": surname, "должность": position, "год поступления": year})
    employees.sort(key=lambda x: x["фамилия и инициалы"])
    return employees


def save_to_json(employees, filename):
    with open(filename, "w") as file:
        json.dump(employees, file)


def load_from_json(filename):
    with open(filename, "r") as file:
        employees = json.load(file)
    return employees


def print_employees_with_experience(employees, years):
    found = False
    for employee in employees:
        experience = 2024 - employee["год поступления"]
        if experience > years:
            print(employee["фамилия и инициалы"])
            found = True
    if not found:
        print("Нет работников с таким стажем работы в организации.")


def main():
    parser = argparse.ArgumentParser(description="Program for managing employee records")
    parser.add_argument("--load", help="Load employee data from JSON file")
    parser.add_argument("--save", help="Save employee data to JSON file")
    parser.add_argument("--experience", type=int, help="Minimum years of experience")
    parser.add_argument("--data", help="Name of the data file")
    args = parser.parse_args()

    if args.data:
        data_file = args.data
    elif os.environ.get('WORKERS_DATA'):
        data_file = os.environ.get('WORKERS_DATA')
    else:
        data_file = "workers.json"

    if args.load:
        employees = load_from_json(args.load)
    else:
        employees = input_data()

    if args.experience is not None:
        print("Работники с стажем работы более {} лет:".format(args.experience))
        print_employees_with_experience(employees, args.experience)
    else:
        print("Не указан минимальный стаж работы. Используйте опцию --experience для этого.")

    if args.save:
        save_to_json(employees, args.save)
        print("Список сотрудников сохранен в файл", args.save)


if __name__ == "__main__":
    main()
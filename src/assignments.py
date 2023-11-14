# define your methods here.
# ex1() - ex10()
from pprint import pprint

from src.Invoice import Invoice
from src.Dwarf import Dwarf
from src.Fighter import Fighter
from src.CarCollector import CarCollector
from src.Calculator import Calculator
from src.TaxMan import TaxMan
from src.WordCounter import WordCounter


def sort_people(people_list, category, direction):
    if direction == "desc":
        people_list.sort(key=lambda p: p[category], reverse=False)
    people_list.sort(key=lambda p: p[category], reverse=True)
    return people_list


def ex1():
    people_list = [
        {"name": "alice", "age": 20, "weight": 160, "sex": "male", "id": 1},
        {"name": "bob", "age": 10, "weight": 130, "sex": "male", "id": 2},
        {"name": "charlie", "age": 15, "weight": 120, "sex": "female", "id": 3},
    ]
    sort_people(people_list, "weight", "desc")
    print(people_list)


def filter_males(people_list):
    new_list = list(filter(lambda p: p["sex"] == "male", people_list))
    return new_list


def ex2():
    people_list = [
        {"name": "alice", "age": 20, "weight": 160, "sex": "male", "id": 1},
        {"name": "bob", "age": 10, "weight": 130, "sex": "male", "id": 2},
        {"name": "charlie", "age": 15, "weight": 120, "sex": "female", "id": 3},
    ]
    filtered_list = filter_males(people_list)
    print(filtered_list)


def calc_bmi(people_list):
    new_list = list(
        map(
            lambda p: (
                {
                    "id": p["id"],
                    "name": p["name"],
                    "weight_kg": p["weight_kg"],
                    "height_meters": p["height_meters"],
                    "bmi": round(p["weight_kg"] / p["height_meters"] ** 2, 1),
                }
            ),
            people_list,
        )
    )
    return new_list


def ex3():
    people_list = [
        {"id": 2, "name": "bob", "weight_kg": 90, "height_meters": 1.7},
        {"id": 3, "name": "charlie", "weight_kg": 80, "height_meters": 1.8},
    ]
    new_people_list = calc_bmi(people_list)
    print(new_people_list)


def get_people(people_list):
    new_list = [p["name"] for p in people_list if p["age"] >= 15]
    return new_list


def ex4():
    people_list = [
        {"name": "alice", "age": 20, "weight": 160, "sex": "male", "id": 1},
        {"name": "bob", "age": 10, "weight": 130, "sex": "male", "id": 2},
        {"name": "charlie", "age": 15, "weight": 120, "sex": "female", "id": 3},
    ]
    print(get_people(people_list))


def ex5():
    sentence = "This is a test of the emergency broadcast system"
    word_counter = WordCounter(sentence)
    word_counter.count_words()
    print(word_counter.get_word_count())  # Returns the number of all the words.
    print(word_counter.get_shortest_word())  # Returns the length of the shortest word.
    print(word_counter.get_longest_word())  # Returns the length of the longest word.


def ex6():
    items = [
        {"id": 1, "desc": "clock", "price": 1.00},
        {"id": 2, "desc": "socks", "price": 2.00},
        {"id": 3, "desc": "razor", "price": 3.00},
    ]
    tm = TaxMan(items, "10%")
    tm.calc_total()
    print(tm.get_total())


def ex7():
    calculator1 = Calculator(4, 3)
    calculator1.add()
    print(calculator1.get_result())

    calculator2 = Calculator(4, 3)
    calculator2.sub()
    print(calculator2.get_result())

    calculator3 = Calculator(2, 3)
    calculator3.mul()
    print(calculator3.get_result())

    calculator4 = Calculator(8, 2)
    calculator4.div()
    print(calculator4.get_result())


def ex8():
    # print(CarCollector.car_list)
    print(CarCollector.get_data())


def ex9():
    f = Fighter(18)
    d = Dwarf(15)
    print(f)
    print(d)
    f.fight(d)
    d.fight(f)
    print(f)
    print(d)


def ex10():
    data = [
        "1, 2322, 10.00, False",
        "2, 5435, 60.30, True",
        "3, 3433, 15.63, False",
        "4, 8439, 12.77, False",
        "5, 3424, 11.34, False",
    ]

    new_list = list(map(lambda d: Invoice(d), data))
    pprint(new_list)

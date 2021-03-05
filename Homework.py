import random
import json


def test_task1():
    number_list = [1, 0, -52, 3, 5, -8, 13, 21, 34, -55, 89]
    for item in number_list:
        if item<=5:
            print(item)

def test_task2():
    numbers_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    numbers_3 = []
    for item1 in numbers_1:
        for item2 in numbers_2:
            if item1==item2:
                numbers_3.append(item2)
    print(numbers_3)

def test_task3():
    numbers = [4, 6, 2, 6, 9, 1, 0, 43]
    x=numbers[0]
    y=numbers[-1]
    print(x,y)

def test_task4():
    string_numbers = "23,45,-7,45,-6,7,8,44,0"
    l=string_numbers.split(',')
    a = []
    for x in l:
        a.append(x)
    b=tuple(a)
    c=set(a)
    print(a,b,c)

def test_task5():
    string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    a=string.count('m')
    print(a)

def test_task6():
    string = "Automation sometimes helps helps helps project help hel and sometimes does not."
    l=string.split()
    c=[]
    x=[]
    for a in l:
        b=len(a)
        c.append(b)
    i = c.index(max(c))
    print("The longest word is:"+l[i])
    for a in l:
        g=l.count(a)
        x.append(g)
    i=x.index(max(x))
    print("The most frequency word if:"+l[i])

def test_task7():
    string = "Exception breakpoints: suspend the program when Exception or its subclasses are thrown.In PyCharm, you can set breakpoints for Python exceptions."
    new_string = string.replace(" ","_")
    print(new_string)

def task8():
    name =input("What's your name")
    print(name)
#Same of task5

def test_task9():
    my_str="rotor playing in car kayak"
    l=my_str.split()
    for a in l:
        rev_str = reversed(a)
        if list(a)==list(rev_str):
            print("This word is palindrome")
        else:
            print("This word is not palindrome")

def test_task10():
    my_dict = {'a': 234, 'b': 34, 'c': 375, 'd': 934, 'e': 5271, 'f': 1945}
    c=[]
    x=[]
    key_list = list(my_dict.keys())
    val_list = list(my_dict.values())
    for key, value in my_dict.items():
        c.append(value)
    i = 0
    while i < 3:
        b = max(c)
        x.append(b)
        c.remove(b)
        i += 1
    for g in x:
        position = val_list.index(g)
        print(key_list[position])
#ортировка элементов от большего к меньшему

#Homework 2

def test_tasks1():
    a_file = open("testtext.txt", "r").readlines()
    list_of_lines = a_file
    n = random.randint(1, len(list_of_lines))
    list_of_lines[n] = "Hello\n"
    a_file = open("testtext.txt", "w")
    a_file.writelines(list_of_lines)
    print(list_of_lines)
    k = random.randint(1, len(list_of_lines))
    del list_of_lines[k]
    print(list_of_lines)
    a_file.close()

def test_tasks2():
    a_file = open("testtext.txt", "r").readlines()
    lists = list(reversed(a_file))
    print(a_file)
    a_file = open("testtext.txt", "w")
    for i in lists:
        a_file.writelines(i)
    print(lists)

def test_tasks3():
    a_file = open("file1.txt", "r").read()
    a_file1 = open("file2.txt", "r").read()
    a_file += a_file1
    a_file2 = open("file3.txt", "w").write(a_file)

def test_tasks4():
        with open("response.json", 'r') as f:
            contents = json.load(f)
            mas = {}
            masiv = {}
            for i in contents['data']:
                 mas.update({i['id']:i['title']})
                 masiv.update({i['id']:i['urls']})
        with open("videos_id_name", "w") as file1:
            json.dump(mas, file1)
        with open("videos_id_urls", "w") as file2:
            json.dump(masiv, file2)
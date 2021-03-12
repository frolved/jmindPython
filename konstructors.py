#
# class Collection:
#     def __init__(self, list):
#         self.list = list
#
#     def __len__(self):
#         return len(self.list)
#
# collection = Collection([1, 2, 3])
# print(len(collection)) # 3
#
#
# class Table:
#     def __init__(self, l, w, h):
#         self.length = l
#         self.width = w
#         self.height = h
#
#
# class KitchenTable(Table):
#     def setPlaces(self, p):
#         self.places = p
#
#
# class DeskTable(Table):
#     def square(self):
#         return self.width * self.length
#
#
# class Person
#     def __init__(self, n, s, q = 1):
#         self.name = n
#         self.surname = s
#         self.qualification = q
#
#     def info(self):
#         return n, s, q
#
#     def __del__(self, n, s, q):
#         print("This mister was the worst:" n, s, q)
#
# class Table:
#     def __init__(self, l, w, h):
#         self.length = l
#         self.width = w
#         self.height = h
#
# class KitchenTable(Table):
#     def setPlaces(self, p):
#         self.places = p
#
# class DeskTable(Table):
#     def square(self):
# #         return self.width * self.length
# class WinDoor:
#     def __init__(self, x, y):
#         self.square = x * y
#
# class Room:
#     def __init__(self, x, y, z):
#         self.square = 2 * z * (x + y)
#         self.wd = []
#     def addWD(self, w, h):
#         self.wd.append(WinDoor(w, h))
#     def workSurface(self):
#         new_square = self.square
#         for i in self.wd:
#             new_square -= i.square
#         return new_square
#
# r1 = Room(6, 3, 2.7)
# print(r1.square) # выведет 48.6
# r1.addWD(1, 1)
# r1.addWD(1, 1)
# r1.addWD(1, 2)
#
# print(r1.workSurface()) # выведет 44.6

a = (i + 1 for i in range(10))
print(type(a))
print(next(a))
print(next(a))
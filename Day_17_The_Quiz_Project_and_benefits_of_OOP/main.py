# class User:
#     def __init__(self, id, name):
#         self.abc = id
#         self.xyzdef = name
#         print("new user is being initialized")


# user1 = User("001", "CVGS")
# user2 = User("002", "Ramya")
# user3 = User("003", "AQWE")

# print(user1.abc)
# print(user1.xyzdef)

# print(user2.abc)
# print(user2.xyzdef)

# print(user3.abc)
# print(user3.xyzdef)

#constructor 2
class Dummy1:
    def __init__(self, input11, input12):
        self.test11 = input11
        self.test12 = input12
    def method1(self):
        self.test12 = 5

#constructor 3
class Dummy2:
    def __init__(self, input21, input22):
        self.test21 = input21
        self.test22 = input22

#constructor 4
class Dummy3:
    def __init__(self, input31, input32):
        self.test31 = input31
        self.test32 = input32

dums1 = Dummy1(1, 1)
print(dums1.test11)
print(dums1.test12)

dums1.method1()
print(dums1.test12)
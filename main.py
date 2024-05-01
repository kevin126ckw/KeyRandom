import random

alist = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L", 13: "M",
         14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y",
         26: "Z", 27: "1", 28: "2", 29: "3", 30: "4", 31: "5", 32: "6", 33: "7", 34: "8", 35: "9", 36: "0"}


num = input("数量:")

for _ in range(int(num)):

    for i in range(1,30):
        if i == 6 or i == 12 or i == 18 or i == 24:
            print("-", end="")
        else:
            a = random.randint(1, 30)
            print(alist[a], end="")

    print()

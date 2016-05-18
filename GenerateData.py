import random

def main():
    f = open('myData.txt', 'w')
    for i in range(100):
        f.write(str(random.randint(0, 20)) + " " + str(random.randint(0, 20)) + "\n")
    f.close()

main()

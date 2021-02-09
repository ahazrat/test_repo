from config import SUPER_SECRET_KEY

def main(j=1000):
    i = 0
    while i<j:
        print(SUPER_SECRET_KEY)
        i+=1


if __name__ == '__main__':
    main(10)
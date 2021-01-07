# Recursive Printing
def printnummer(n):
    while n > 0:
        print(n)
        n -= 2
        if n == 0:
            print(n)

def main():
    print("Voer hieronder een getal in:")
    n = int(input())
    printnummer(n)


main()

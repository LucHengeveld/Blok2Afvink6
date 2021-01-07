# Recursive Multiplication
def vermenigvuldigen(x, y):
    antwoord = x * y
    return antwoord


def main():
    x = int(input("Voor hier X in: "))
    y = int(input("Voor hier Y in: "))
    antwoord = vermenigvuldigen(x, y)
    print("Uitkomst: " + antwoord)


main()

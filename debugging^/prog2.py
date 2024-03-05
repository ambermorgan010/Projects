def main():
    a = float(input())
    b = int(input())
    c = 0
    d = a
    while c < b:
        e = d * 0.05
        d += e
        c += 1
    print(b, d)


if __name__ == "__main__":
    main()

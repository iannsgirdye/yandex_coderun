def main():
    data = int(input()), int(input()), int(input())
    if (data[0] + data[1]) <= data[2]:
        print("NO")
    elif (data[1] + data[2]) <= data[0]:
        print("NO")
    elif (data[2] + data[0]) <= data[1]:
        print("NO")
    else:
        print("YES")


if __name__ == '__main__':
    main()

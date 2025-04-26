def main():
    data = input().split()
    
    for i in range(len(data) - 1):
        if data[i] >= data[i + 1]:
            print("NO")
            break
    else:
        print("YES")    


if __name__ == "__main__":
    main()

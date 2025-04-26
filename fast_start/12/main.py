def main():
    N = int(input())
    data = tuple(map(int, input().split()))
    x = int(input())
    
    nearest = 10000
    for element in data:
        delta_nearest = abs(x - nearest)
        delta_element = abs(x - element)
        if delta_element <= delta_nearest:
            nearest = element
            
    print(nearest)


if __name__ == "__main__":
    main()

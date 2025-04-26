def main():
    t = [0] * 36
    n = int(input())  # 1 <= n <= 35
    
    for i in range(1, n + 1):
        if i <= 2:
            t[i] = 1
        else:
            t[i] = t[i - 1] + t[i - 2]
    
    print(sum(t))


if __name__ == "__main__":
    main()

import sys


def main():
    numbers = list(map(int, sys.stdin.readline().split()))
    result = 0
    for i in range(1, len(numbers) - 1): 
        if (numbers[i - 1] < numbers[i]) and (numbers[i] > numbers[i + 1]):
            result += 1
    print(result)
    

if __name__ == "__main__":
    main()

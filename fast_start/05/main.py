# Пора читать ТЗ
import sys
import math


def main():
    a, b, c = map(float, sys.stdin.readline().split())  # коэффициенты, a != 0
    
    D = b ** 2 - 4 * a * c
    if D < 0:
        print(0)
    else:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        x1, x2 = min(x1, x2), max(x1, x2)
        
        if x1 == x2:
            print(1)
            print(round(x1, 6))
        else:
            print(2)
            print(round(x1, 6), round(x2, 6))


if __name__ == "__main__":
    main()

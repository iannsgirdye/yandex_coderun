import sys


def main():
    words = set()
    
    for line in sys.stdin:
        line = line.split()
        for word in line:
            words.add(word)
    
    print(len(words))


if __name__ == "__main__":
    main()

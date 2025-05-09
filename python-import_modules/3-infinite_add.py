#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    sum = 0
    if len(args) > 0:
        for i, arg in enumerate(args):
            sum = sum + int(arg)

    print(f"{sum}")

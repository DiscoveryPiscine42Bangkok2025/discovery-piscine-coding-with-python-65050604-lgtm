import sys

if len(sys.argv) == 3:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        
        start = min(num1, num2)
        end = max(num1, num2)
        
        result_range = range(start, end + 1)
        print(list(result_range))
    except ValueError:
        print("none")
else:
    print("none")
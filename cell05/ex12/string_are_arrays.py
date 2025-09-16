import sys

if len(sys.argv) == 2:
    input_string = sys.argv[1]
    z_count = input_string.count('z')
    
    if z_count > 0:
        for _ in range(z_count):
            print('z')
    else:
        print("none")
else:
    print("none")
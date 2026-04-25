import sys

if len(sys.argv) < 2:
    print("none")
else: 
    i = sys.argv[1:]
    for j in reversed(i):
        print(j)








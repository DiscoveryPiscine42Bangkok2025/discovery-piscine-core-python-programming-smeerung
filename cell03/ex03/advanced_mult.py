import sys

if sys.argv[1:]:
    print("none")
    sys.exit()

x = 0
while x <= 10:
    print("Table de", x, ":", x*1, x*2, x*3, x*4, x*5, x*6, x*7, x*8, x*9, x*10)
    x += 1

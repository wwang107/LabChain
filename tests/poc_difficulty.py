import math

a = [0.005, 0.05, 0.5, 1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 40, 45, 50, 60, 75, 85, 90, 100, 120, 180,
     240, 300, 360, 420, 500, 600]
max_diff = 6
avg = 60.0
for v in a:
    d = max_diff - int(math.log((v * 900) / avg))
    print(str(v) + "  " + str(d))

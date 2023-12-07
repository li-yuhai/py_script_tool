
f_txt = open('./map2.txt', 'r')
lines = list(f_txt)
all_r = 0.0
all_p = 0.0
for line in lines:
    line = line.strip().split(";")
    r = float(line[1].split('=')[1][:5])
    p = float(line[2].split('=')[1][:5])
    all_r += r
    all_p += p
    # print( r , p )
print("recal: =" , all_r / 24, "pre", all_p /24)

def recursive(x, y, label): # 4
    if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == -1: # ห้ามเกินขอบ array และเป็น -1
        image[x][y] = label
        recursive(x + 1, y, label)  # ขวา 
        recursive(x - 1, y, label)  # ซ้าย
        recursive(x, y + 1, label)  # บน
        recursive(x, y - 1, label)  # ล่าง
        # recursive(x + 1, y+1, label) # ขวาบน
        # recursive(x - 1, y+1, label)  # ซ้ายบน
        # recursive(x + 1, y - 1, label) # ขวาล่าง
        # recursive(x - 1, y - 1, label) # ซ้ายล่าง


image =[[1,1,0,0,0,1,1],
        [1,1,1,0,1,0,1],
        [0,1,1,0,1,0,1],
        [0,1,0,0,1,0,1],
        [0,0,0,1,1,0,0],
        [1,1,0,1,1,0,1],
        [1,1,0,1,1,0,1]]
label = 1 

print("row =  %d" % len(image))
print("column = %d" % len(image[0]))
print("before")
for row in image:
    print(*row, sep="\t")

for i in range(len(image)):
    for j in range(len(image[0])):
            if image[i][j] == 1:
                image[i][j] = -1
print("")

for row in image:
    print(*row, sep="\t")


for i in range(len(image)):
    for j in range(len(image[0])):
        if image[i][j] == -1:
            recursive(i, j, label)
            label = label + 1

print("after counting")
for row in image:
    print(*row, sep="\t")
print("object = %d" %(label-1))

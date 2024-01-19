

def recursive_search(x, y, label):
    if 0 <= x < 5 and 0 <= y < 5 and image[x][y] == -1:
        image[x][y] = label
        recursive_search(x + 1, y, label)  # ขวา
        recursive_search(x - 1, y, label)  # ซ้าย
        recursive_search(x, y + 1, label)  # ล่าง
        recursive_search(x, y - 1, label)  # บน


image = [[1,1,0,0,0],
        [1,1,1,0,1],
        [0,1,1,0,1],
        [0,1,0,0,1],
        [0,0,0,1,1]]
label = 1 


for row in image:
    print(*row, sep="\t")

for i in range(5):
    for j in range(5):
            if image[i][j] == 1:
                image[i][j] = -1
print("")

for row in image:
    print(*row, sep="\t")


for i in range(5):
    for j in range(5):
        if image[i][j] == -1:
            print("x")
            recursive_search(i, j, label)
            label = label + 1

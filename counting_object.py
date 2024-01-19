def Recursion(i,j):
    x = i
    y = j
    r = 0
    
    if img[x][y] != object_num:
        img[x][y] = object_num

    if y+1 <=4 :   
        if img[x][y+1] != object_num and img[x][y+1] != 0:
            Recursion(x,y+1)

    if x+1 <=4 :  
        if img[x+1][y] != object_num and img[x+1][y] != 0:
            Recursion(x+1,y)

    if y-1 >=4 :  
        if img[x][y-1] != object_num and img[x][y-1] != 0:
            Recursion(x,y-1)

    if x-1 >=4 :
        if img[x-1][y] != object_num and mg[x-1][y] != 0:
            Recursion(x-1,y)



object_num = 0

img = [[1,1,0,0,0],
        [1,1,1,0,1],
        [0,1,1,0,1],
        [0,1,0,0,1],
        [0,0,0,1,1]]
for row in img:
    print(*row, sep="\t")

for i in range(5):
    for j in range(5):
            if img[i][j] == 1:
                img[i][j] = -1
print("")

for row in img:
    print(*row, sep="\t")

print("")

for i in range(5):
    for j in range(5):
            if img[i][j] != 0:
                object_num = object_num + 1
                Recursion(i,j)

for row in img:
    print(*row, sep="\t")              
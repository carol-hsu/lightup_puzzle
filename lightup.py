filename = "problem.txt"

f = open(filename)

matrix = []
max_step = int(f.readline().strip())

for line in f.readlines():
    newline = []
    for c in line.strip():
        if c == "x":
            newline.append(-1)
        else:
            newline.append(int(c))
    matrix.append(newline)

def all_good():
    for i in range(8):
        for j in range(8):
            if matrix[i][j] == 0:
                return False
    return True

def print_matrix():
    print("------")
    for i in range(8):
        print(matrix[i])
    
def print_clicks(clicks):

    for i in range(8):
        this_row = []
        for j in range(8):
            if i*8+j in clicks:
                this_row.append("O")
            elif matrix[i][j] == -1:
                this_row.append("X")
            else:
                this_row.append("-")
            
        print(this_row)
    print()

def switch(i, j):
    matrix[i][j] ^= 1
    if i > 0 and matrix[i-1][j] != -1:
        matrix[i-1][j] ^= 1
    if i < 7 and matrix[i+1][j] != -1:
        matrix[i+1][j] ^= 1
    if j > 0 and matrix[i][j-1] != -1:
        matrix[i][j-1] ^= 1
    if j < 7 and matrix[i][j+1] != -1:
        matrix[i][j+1] ^= 1

def lightup(cid, clicks):
    if cid == 64:
        # the last click
        if all_good() and len(clicks) <= max_step:
            print("PASS:", len(clicks))
            print_clicks(clicks)
    elif len(clicks) < max_step:

        r, c = cid//8, cid%8
        if matrix[r][c] == -1:
            ## cannot
            if r == 0 or (r > 0 and matrix[r-1][c] != 0):
                lightup(cid+1, clicks)
        elif r == 0 or (r > 0 and matrix[r-1][c] == -1):
            # can click or 
            switch(r, c)
            clicks.add(cid)
            lightup(cid+1, clicks)
            switch(r, c)
            clicks.remove(cid)
            ## no click
            lightup(cid+1, clicks)

        elif r > 0 and matrix[r-1][c] == 0:
            switch(r, c)
            clicks.add(cid)
            lightup(cid+1, clicks)
            switch(r, c)
            clicks.remove(cid)
        else:
            lightup(cid+1, clicks)

    elif all_good():
        print("PASS earlier:", len(clicks))
        print_clicks(clicks)
            

lightup(0, set())

def main():
    grid_size = int(input())
    g = int((grid_size-1)/2)

    grid = []
    for i in range(grid_size):
        j = str(input())
        grid.append(j)

    grid_size-=1
    if grid[0][0]=="p":
        for k in range(g):
            print("UP")
        for k in range(g):
            print("LEFT")
        
    elif grid[0][-1]=="p":
        for k in range(g):
            print("UP")
        for k in range(g):
            print("RIGHT")
        
    elif grid[grid_size][0]=="p":
        for k in range(g):
            print("DOWN")
        for k in range(g):
            print("LEFT")
        
    elif grid[grid_size][-1]:
        for k in range(g):
            print("DOWN")
        for k in range(g):
            print("RIGHT")
         

main()
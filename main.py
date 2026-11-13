import numpy as np
grid = np.zeros((30, 20) , dtype=int)

grid[4, 8] = 1
grid[4, 9] = 1
grid[4, 7] = 1
#for i in range(5):
  #  path = ((np.random.randint(0,10), (np.random.randint(0,10))))
   # while grid[path] == 1:
     #   path = ((np.random.randint(0,10), (np.random.randint(0,10))))
   # grid[path] = 1
def new_gen(grid , gen):
    the_grid = grid.copy()
    found_true = []
    new_grid = np.zeros_like(grid)
    all_gen_in_one = {}
    cycle = False
    for index in range (gen):
        rows , cols = grid.shape
        for row in range(rows):
            for col in range(cols):
                neighbor = 0
                for i in range(row - 1 , row + 2):
                    for j in range(col-1 , col + 2):

                            if (i , j) != (row , col):
                                neighbor += the_grid[i%rows , j%cols]

                if the_grid[(row , col)] == 1:
                    if neighbor==3 or neighbor==2: 
                        new_grid[(row , col)] = 1
                else:
                    if neighbor == 3:
                        new_grid[(row , col)] = 1
        for gens in all_gen_in_one:
                        if gens != f"Genration {index + 1}":
                            if np.array_equal(all_gen_in_one[gens] ,new_grid):
                                found_true.append([gens , f"Genration {index + 1}" , 'found'])
                                cycle = True
        
        all_gen_in_one[f"Genration {index + 1}"] = new_grid.copy()                
        the_grid , new_grid = new_grid , the_grid
        new_grid.fill(0)
        if cycle:
             break
    return all_gen_in_one , found_true




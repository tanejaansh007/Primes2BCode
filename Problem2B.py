from collections import deque
import random

def grid_constructor(n, p):
    grid = [[random.random() < p for c in range(n)] for r in range(n)] #True if occupied, False if not
    return grid


def has_path(grid, n): #inputs could be (n, p) but I wanted to test hand-made grids

    visited = [[False] * n for _ in range(n)] #array of visited squares: True if visited, False if not
    q = deque() #deque of elements that need checking
    for i in range (n):
        if grid[i][0]: #adding all initial occupied squares
            q.append((i, 0))
            visited[i][0] = True

    while q:
        (r, c) = q.popleft() #removing the next site to check from the queue
        if (c == n-1):
            return True
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]: #possible next moves
            (nr, nc) = (r + dr, c + dc) #computing the new coordinates of the squares to check
            
            if ((0 <= nr < n) and (0 <= nc < n)): #in the correct bounds (should not go outside the n by n square)
                if not visited[nr][nc]: #if not visited yet
                    if grid[nr][nc]: #if occupied
                        q.append((nr, nc)) #adding to queue
                        visited[nr][nc] = True #marking as visited
    return False

def estimate_theta(n, p, M):
    correctTrials = 0 #counter for number of trials that have an occupied path

    for _ in range(M):

        grid = grid_constructor(n, p) #make the grid

        result = has_path(grid, n) #True/False

        if result:
            correctTrials += 1 #adds one if it has a crossing
    
    ratioCorrect = correctTrials/M

    return ratioCorrect

if __name__ == "__main__": #this block can be changed to test the functionality of the code - for instance, I changed it to test sample grids and verify that has_path was working.
    
    M = int(input("How many trials?\n"))
    p = float(input("Probability of any space being occupied, as a decimal:\n"))
    n = int(input("Size of the grid:\n"))

    print("\nEstimate of theta(p, n):", estimate_theta(n, p, M))

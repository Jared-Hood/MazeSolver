import random
import Node


#Generate Maze Randomly

def createmaze(r, c):
    maze = [[0 for i in range(c)]for j in range(r)]
    maze[0][0] = "S"
    maze[r-1][c-1] = "F"

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if ( maze[i][j] != "S" and maze[i][j] != "F"):

                #25% chance of being a wall
                x = random.randrange(0,4)
                if x < 1:
                    maze[i][j] = 1
                else:
                    maze[i][j] = 0

    maze[0][1] = 0
    maze[1][0] = 0
    maze[r - 1][c - 2] = 0
    maze[r - 2][c - 1] = 0

    mazeNode = [[0 for i in range(c)]for j in range(r)]
    for i in range(len(mazeNode)):
        for j in range(len(mazeNode[0])):
            n = Node.Node(maze[i][j])
            n.coord = (j,i)
            mazeNode[i][j] = n

    #Add up down left and right neighbors

    for i in range(len(mazeNode)):
        for j in range(len(mazeNode[0])):
            nb = []     #neighbors

            #corners
            if ( i == 0 and j == 0):
                nb.append(mazeNode[0][1])
                nb.append(mazeNode[1][0])
            elif ( i == len(mazeNode) - 1 and j == 0):
                nb.append(mazeNode[len(mazeNode) - 2][0])
                nb.append(mazeNode[len(mazeNode) - 1][1])
            elif ( i == 0 and j == len(mazeNode[0]) - 1):
                nb.append(mazeNode[0][len(mazeNode[0])-2])
                nb.append(mazeNode[1][len(mazeNode[0])-1])
            elif ( i == len(mazeNode) -1 and j == len(mazeNode[0]) - 1):
                nb.append(mazeNode[len(mazeNode)-1][len(mazeNode[0])-2])
                nb.append(mazeNode[len(mazeNode) - 2][len(mazeNode[0]) - 1])

            #Top
            elif (i == 0):
                nb.append(mazeNode[0][j+1])
                nb.append(mazeNode[0][j-1])
                nb.append(mazeNode[1][j])

            #Bottom
            elif(i == len(mazeNode)-1):
                nb.append(mazeNode[i][j + 1])
                nb.append(mazeNode[i][j - 1])
                nb.append(mazeNode[i-1][j])

            #Left
            elif ( j == 0):
                nb.append(mazeNode[i + 1][j])
                nb.append(mazeNode[i - 1][j])
                nb.append(mazeNode[i][j + 1])

            #Right
            elif ( j == len(mazeNode[0])-1):
                nb.append(mazeNode[i + 1][j])
                nb.append(mazeNode[i - 1][j])
                nb.append(mazeNode[i][j - 1])

            #Middle
            else:
                nb.append(mazeNode[i][j+1])
                nb.append(mazeNode[i][j - 1])
                nb.append(mazeNode[i+1][j])
                nb.append(mazeNode[i-1][j])

            mazeNode[i][j].setNext(nb)

    return mazeNode

#Generate maze from image

def mazeFromImage(pic):
    r = pic.size[1]
    c = pic.size[0]
    pixels = pic.load()

    maze = [[0 for i in range(c)] for j in range(r)]
    maze[0][0] = "S"
    maze[r - 1][c - 1] = "F"

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (maze[i][j] != "S" and maze[i][j] != "F"):
                if pixels[j,i][3] == 0:
                    maze[i][j] = 0
                else:
                    maze[i][j] = 1


    maze[0][1] = 0
    maze[1][0] = 0
    maze[r - 1][c - 2] = 0
    maze[r - 2][c - 1] = 0

    mazeNode = [[0 for i in range(c)] for j in range(r)]
    for i in range(len(mazeNode)):
        for j in range(len(mazeNode[0])):
            n = Node.Node(maze[i][j])
            n.coord = (j, i)
            mazeNode[i][j] = n

    # Add up down left and right neighbors

    for i in range(len(mazeNode)):
        for j in range(len(mazeNode[0])):
            nb = []  # neighbors

            # corners
            if (i == 0 and j == 0):
                nb.append(mazeNode[0][1])
                nb.append(mazeNode[1][0])
            elif (i == len(mazeNode) - 1 and j == 0):
                nb.append(mazeNode[len(mazeNode) - 2][0])
                nb.append(mazeNode[len(mazeNode) - 1][1])
            elif (i == 0 and j == len(mazeNode[0]) - 1):
                nb.append(mazeNode[0][len(mazeNode[0]) - 2])
                nb.append(mazeNode[1][len(mazeNode[0]) - 1])
            elif (i == len(mazeNode) - 1 and j == len(mazeNode[0]) - 1):
                nb.append(mazeNode[len(mazeNode) - 1][len(mazeNode[0]) - 2])
                nb.append(mazeNode[len(mazeNode) - 2][len(mazeNode[0]) - 1])

            # Top
            elif (i == 0):
                nb.append(mazeNode[0][j + 1])
                nb.append(mazeNode[0][j - 1])
                nb.append(mazeNode[1][j])

            # Bottom
            elif (i == len(mazeNode) - 1):
                nb.append(mazeNode[i][j + 1])
                nb.append(mazeNode[i][j - 1])
                nb.append(mazeNode[i - 1][j])

            # Left
            elif (j == 0):
                nb.append(mazeNode[i + 1][j])
                nb.append(mazeNode[i - 1][j])
                nb.append(mazeNode[i][j + 1])

            # Right
            elif (j == len(mazeNode[0]) - 1):
                nb.append(mazeNode[i + 1][j])
                nb.append(mazeNode[i - 1][j])
                nb.append(mazeNode[i][j - 1])

            # Middle
            else:
                nb.append(mazeNode[i][j + 1])
                nb.append(mazeNode[i][j - 1])
                nb.append(mazeNode[i + 1][j])
                nb.append(mazeNode[i - 1][j])

            mazeNode[i][j].setNext(nb)

    return mazeNode
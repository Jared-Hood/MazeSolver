from PIL import Image

def drawMaze(matrix):

    img = Image.new('RGB', (len(matrix[0]),len(matrix)))

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if ( matrix[i][j].value == 1):
                color = (0,0,0)
            elif (matrix[i][j].value == "S"):
                color = (0,255,0)
            elif (matrix[i][j].value == "F"):
                color = (0,0,255)
            else:
                color = (255,255,255)

            img.putpixel((j,i), color)

    return img

def drawPath(path, maze):
    for node in path:
        maze.putpixel(node.coord, (255,0,0))

   # maze.show()
    maze.save('BFS.png')
    return maze


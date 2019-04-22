import maze
import mazePic
import Algos
from PIL import Image
import sys

def main():

    if len(sys.argv) == 3:
        r = int(sys.argv[1])
        c = int(sys.argv[2])
        m = maze.createmaze(r, c)
        start = m[0][0]
        end = m[r - 1][c - 1]
        pic = mazePic.drawMaze(m)
        path = Algos.BFS(start, end)

        try:
            a = mazePic.drawPath(path, pic)
            a.show()
        except:
            print("No path")


    if len(sys.argv) == 2:
        try:
            img = Image.open(sys.argv[1])
            m = maze.mazeFromImage(img)
            start = m[0][0]
            end = m[img.size[1] - 1][img.size[0] - 1]
            path = Algos.BFS(start, end)

            try:
                a = mazePic.drawPath(path, img)
                a.show()
            except:
                print("No path")

        except:
            print("Image not found")

    else:
        print("Input either the height and width or picture name")

if __name__ == "__main__":
    main()

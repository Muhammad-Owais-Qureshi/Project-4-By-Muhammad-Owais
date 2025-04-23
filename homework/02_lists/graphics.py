import tkinter as tk
import time

CANVAS_WIDTH : int = 400
CANVAS_HEIGHT : int = 400

CELL_SIZE : int = 40
ERASER_SIZE : int = 20

def erase_objects(canvas):
   
   cells = []
   for row in range(0 ,CANVAS_HEIGHT , CELL_SIZE):
      row_cells = []
      for col in range(0 ,CANVAS_WIDTH , CELL_SIZE):
          rectangle = canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, 'blue')
          row_cells.append(rectangle)
          cells.append(row_cells)
          return cells

    
def main():
     global grid_cells , canvas
     root = tk.Tk()
     root.title("Canvas")

     canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
     canvas.pack()

     grid_cells = erase_objects(canvas)
       
     root.mainloop()



if __name__ == '__main__':
    main()
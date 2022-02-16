import py_compile


from tkinter import *

class display_a_selected_shape:
    def __init__(self):

        self.width = 250
        self.height = 100
        window = Tk()
        window.title("Display a Selected Shape")

        selected = StringVar()
        selected.set("Rectangle")

        self.combo_box = OptionMenu(window, selected, "Rectangle", "Oval", "Arc", "Polygon", "Line", command = self.process_selection).pack(fill=BOTH)
        

        self.canvas = Canvas(window, bg = "white", width = self.width, height = self.height)
        self.canvas.pack()

        window.mainloop()

    def process_selection(self, selected_item):
        self.canvas.delete("image")
        if selected_item == "Rectangle":
            self.canvas.create_rectangle(5,5,245,95,fill="red", outline="blue", width="3", tag = "image")
            
        elif selected_item == "Oval":
            self.canvas.create_oval(5,5,95,95,fill="blue", outline="red", width="3", tag = "image")
        
        elif selected_item == "Arc":
            self.canvas.create_arc(5,5,200,95,fill="purple", outline="orange", width="3", tag = "image")
        
        elif selected_item == "Polygon":
            self.canvas.create_polygon(5,5,245,95,150,75, 35,35,fill="yellow", outline="green", width="3", tag = "image")
        
        elif selected_item == "Line":
            self.canvas.create_line(5, 95, 245, 5, fill="red", width="3", tag = "image")

display_a_selected_shape()



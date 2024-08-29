import tkinter as tk
from PIL import ImageTk


root = tk.Tk()

root.wait_visibility(root)
root.wm_attributes("-fullscreen", 1)
root.wm_attributes("-transparentcolor", root['bg'])

root.title('joe.bat')

frame = tk.Frame(root)
frame.grid()

root.iconphoto(False, tk.PhotoImage(file='joe.png'))

canvas = tk.Canvas(frame, width=root.winfo_width(), height=root.winfo_height())
img = ImageTk.PhotoImage(file='joe1.png')
image = canvas.create_image(0, 0, anchor='nw', image=img)
canvas.coords(image, 1300, -20)
'''img2 = tk.PhotoImage(file='hand.png')
image2 = canvas.create_image(0, 0, anchor='nw', image=img2)
canvas.coords(image2, 100, 100)'''
canvas.pack()

root.mainloop()

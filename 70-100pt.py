##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

#70 Pt 
#Body and roof of house

Rectangle = drawpad.create_rectangle(250,600,550,250)
line = drawpad.create_line(250,250,400,100)
line2 = drawpad.create_line(400,100,550,250)

#80 Pt
#Windows and a door

Rectangle2 = drawpad.create_rectangle(375,600,450,475)
Rectangle3 = drawpad.create_rectangle(260,500,360,390)
Rectangle4 = drawpad.create_rectangle(440,360,540,260)

#90 Pt
#Door Handle and Chimney

Oval = drawpad.create_oval(425,550,430,545)
line3 = drawpad.create_line(450,150,450,100)
line4 = drawpad.create_line(450,100,500,100)
line5 = drawpad.create_line(500,100,500,200)












root.mainloop()


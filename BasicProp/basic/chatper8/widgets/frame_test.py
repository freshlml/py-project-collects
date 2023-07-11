from tkinter import *
from tkinter import ttk

root = Tk()
root.title("frame test")


# 1. Frame widget is a container just like a simple rectangle.
#    Frame often act as master widgets to manage the slave widgets contained within the frame.
fm = ttk.Frame(root, padding=('10', '10', '20', '20'), borderwidth='50', relief=RIDGE, width='500.01', height='550.9999')
fm.grid(column=0, row=0, sticky=(W, E, N, S))

# 2. configuration options
print(fm.configure())
'''
{'borderwidth': ('borderwidth', 'borderWidth', 'BorderWidth', '', <pixel object: '50'>), 
'padding': ('padding', 'padding', 'Pad', '', (<pixel object: '10'>, <pixel object: '10'>, <pixel object: '20'>, <pixel object: '20'>)), 
'relief': ('relief', 'relief', 'Relief', '', <index object: 'ridge'>), 
'width': ('width', 'width', 'Width', <pixel object: '0'>, <pixel object: '500.01'>), 
'height': ('height', 'height', 'Height', <pixel object: '0'>, <pixel object: '550.9999'>), 
'takefocus': ('takefocus', 'takeFocus', 'TakeFocus', '', ''), 
'cursor': ('cursor', 'cursor', 'Cursor', '', ''), 
'style': ('style', 'style', 'Style', '', ''), 
'class': ('class', '', '', '', '')}
'''
# 1). padding: padding inside the Frame.
#              Single value is same padding all around.
#              Two value of which first is applied to 'W' and 'E' with the other applied to 'N' and 'S'.
#              Four value is applied orderly to 'W', 'N', 'E', 'S'.
#     Four value eg: padding='10i 10 20 20', padding=('10i', '10', '20', '20')
#
# 2). borderwidth: width of the border around the Frame. if the Frame contains nothing widgets, no effect?
#     eg: 50/'50' means 50 pixels, '50c' means 50 centimeters, '50m' means 50 millimeters,
#        '50i' means 50 inches, and '50p' means 50 printer's points (1/72 inch).
#
# 3). relief: the display style of border:
#     eg: RAISED, 'raised'; SUNKEN, 'sunken'; FLAT, 'flat'; RIDGE, 'ridge'; GROOVE, 'groove'; SOLID, 'solid'
#
# 4). width, height: specify the explicit size of the Frame.
#                    if the Frame contains other widgets, normally this is omitted,
#                    and the size of the Frame need to accommodate(容纳) the other widgets.
#     eg: 350/'350' means 350 pixels, '350c' means 350 centimeters, '350m' means 350 millimeters,
#         '350i' means 350 inches, and '350p' means 350 printer's points (1/72 inch).
# 5). takefocus: todo
#
# 6). cursor: todo
#
# 7). style: todo
#
# 8). class: todo
#


root.mainloop()











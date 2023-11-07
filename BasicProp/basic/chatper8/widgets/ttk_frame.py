from tkinter import *
from tkinter import ttk

root = Tk()
root.title("ttk frame test")


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
# width/height
#   1. Typically, the size of a frame is determined by the size and layout of any widgets within it.
#      In turn, this is controlled by the geometry manager that manages the contents of the frame itself.
#   2. If there are a *empty frame* that does not contain other widgets,
#      you can explicitly set its size using the `width` and/or `height` configuration options.
#   3. If the Frame contains other widgets, normally `width` and `height` is omitted.
#
#   width/height value: `350` means 350 pixels, `"350c"` means 350 centimeters, `'350m'` means 350 millimeters,
#                       `'350i'` means 350 inches, and `'350p'` means 350 printer's points (1/72 inch).
#
# padding
#   The `padding` configuration option is used to request extra space around the inside of the widget.
#
#   padding value: `padding = 5`              # 5 pixels on all sides
#                  `padding = (5, '10i')`     # 5 on W and E, 10i on N and S
#                  `padding = (5, 7, 10, 12)` # W: 5, N: 7, E: 10, S: 12
#
# Border
#   1. You can display a border by setting `borderwidth` configuration option(which defaults to `0`, i.e., no border),
#      and the `relief` option, which specifies the visual appearance of the border.
#   2. If the Frame contains nothing widgets, `borderwidth` no effect?
#
#   borderwidth value: `350` means 350 pixels, `"350c"` means 350 centimeters ...
#   relief value: `flat` (default), `raised`, `sunken`, `solid`, `ridge`, or `groove`. (constants.py: SUNKEN='sunken')
#
# style
#   Frames have a `style` configuration option, which is common to all of the themed widgets.
#   This lets you control many other aspects of their appearance or behavior.


root.mainloop()











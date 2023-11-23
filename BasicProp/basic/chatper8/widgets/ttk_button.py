from tkinter import *
from tkinter import ttk

root = Tk()
root.title("ttk button test")

fm = ttk.Frame(root)
fm.grid(column=0, row=0, sticky=(W, E, N, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# button is a widget that displays text or images, typically users will interact(交互) with
bt = ttk.Button(fm, text="button-button\nfadsfasd", width=10, padding=(10, 10, 10, 10),
                command=lambda: print(1))
bt.grid(column=0, row=0, sticky=(W, E, N, S))

# fm.columnconfigure(0, weight=1)
# fm.rowconfigure(0, weight=1)

print(bt.configure())
'''
{'command': ('command', 'command', 'Command', '', ''), 
'default': ('default', 'default', 'Default', <index object: 'normal'>, <index object: 'normal'>), 
'takefocus': ('takefocus', 'takeFocus', 'TakeFocus', 'ttk::takefocus', 'ttk::takefocus'), 
'text': ('text', 'text', 'Text', '', ''), 
'textvariable': ('textvariable', 'textVariable', 'Variable', '', ''), 
'underline': ('underline', 'underline', 'Underline', -1, -1), 
'width': ('width', 'width', 'Width', '', ''), 
'image': ('image', 'image', 'Image', '', ''), 
'compound': ('compound', 'compound', 'Compound', <index object: 'none'>, <index object: 'none'>), 
'padding': ('padding', 'padding', 'Pad', '', ''), 
'state': ('state', 'state', 'State', <index object: 'normal'>, <index object: 'normal'>), 
'cursor': ('cursor', 'cursor', 'Cursor', '', ''), 
'style': ('style', 'style', 'Style', '', ''), 
'class': ('class', '', '', '', '')}
'''
# callback
#   1. Using `command` configuration option specify the callback.
#   2. `default`: If "active", this is a "default" button for the window,
#      i.e. the one that will be invoked if the user presses Return.
#      Regular state is "normal" (You need to set up the event binding separately.)
#
# state
#
#
# displays text
#   1. The `text` configuration option set the displaying text of Button.
#   2. You can change what text is displayed by modifying this configuration option. This can be done at any time.
#   3. You can also have the widget monitor a variable in your script. Anytime the variable changes, the button will
#      display the new value of the variable. This is done with the `textvariable` configuration option (`StringVar`)
#
# Displaying Images
#   1. The `image` configuration option set the displaying text of Button.
#   2. Buttons can display both an image and text at the same time, using the `compound` configuration option.
#      "text"-display text only, "image"-display image only, "center"-display text in the center of image,
#      "top"-display text in the top of image, "bottom"-display text in the bottom of image,
#      "left"-display text in the left of image, "right"-display text in the right of image.
#
# width (无 height, lineheight)
#   1. Specify the explicit width of the contents-box (not the width of Button).
#      If the size of contents-box is less than the size of min-required-contents-box, the remainder contents is hidden.
#      If the size of contents-box is larger than the size of min-required-contents-box, there are some space exists.
#   2. 居中对齐
#
# padding
#   The `padding` configuration option is used to request extra space around the inside of the widget.
#
#   padding value: `padding = 5`              # 5 pixels on all sides
#                  `padding = (5, '10i')`     # 5 on W and E, 10i on N and S
#                  `padding = (5, 7, 10, 12)` # W: 5, N: 7, E: 10, S: 12
#
# style
#   Labels have a `style` configuration option, which is common to all of the themed widgets.
#   This lets you control many other aspects of their appearance or behavior.
#
# underline
#   1. Specify the index of underline of the text, a int value, eg: 0 or 1 or ...
#
# takefocus, cursor, class, todo

root.mainloop()


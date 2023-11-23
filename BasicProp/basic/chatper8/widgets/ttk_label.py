from tkinter import *
from tkinter import ttk

root = Tk()
root.title("ttk label test")

fm = ttk.Frame(root, borderwidth="10", relief=GROOVE)
fm.grid(column=0, row=0, sticky=(W, E, N, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# 1. Label is a widget that displays text or images, typically users will just view but not otherwise interact(交互) with
lb = ttk.Label(fm, text="文本本\n本本本", borderwidth="10", relief=RIDGE, padding=(5, 5, 5, 5), background="red",
               anchor="e", width=50)
lb.grid(column=0, row=0, sticky=(W, E, N, S))

fm.columnconfigure(0, weight=1)
fm.rowconfigure(0, weight=1)

print(lb.configure())
'''
{'background': ('background', 'frameColor', 'FrameColor', '', ''), 
'foreground': ('foreground', 'textColor', 'TextColor', '', ''), 
'font': ('font', 'font', 'Font', '', ''), 
'borderwidth': ('borderwidth', 'borderWidth', 'BorderWidth', '', <pixel object: '100'>), 
'relief': ('relief', 'relief', 'Relief', '', <index object: 'raised'>), 
'anchor': ('anchor', 'anchor', 'Anchor', '', ''), 
'justify': ('justify', 'justify', 'Justify', '', <index object: 'center'>), 
'wraplength': ('wraplength', 'wrapLength', 'WrapLength', '', ''), 
'takefocus': ('takefocus', 'takeFocus', 'TakeFocus', '', ''), 
'text': ('text', 'text', 'Text', '', '文本本本本本'), 
'textvariable': ('textvariable', 'textVariable', 'Variable', '', ''), 
'underline': ('underline', 'underline', 'Underline', -1, -1), 
'width': ('width', 'width', 'Width', '', 100), 
'image': ('image', 'image', 'Image', '', ''), 
'compound': ('compound', 'compound', 'Compound', <index object: 'none'>, <index object: 'none'>), 
'padding': ('padding', 'padding', 'Pad', '', ''), 
'state': ('state', 'state', 'State', <index object: 'normal'>, <index object: 'normal'>), 
'cursor': ('cursor', 'cursor', 'Cursor', '', ''), 
'style': ('style', 'style', 'Style', '', ''), 'class': ('class', '', '', '', '')}
'''
# displays text
#   1. The `text` configuration option set the displaying text of Label.
#   2. You can change what text is displayed by modifying this configuration option. This can be done at any time.
#   3. You can also have the widget monitor a variable in your script. Anytime the variable changes, the label will
#      display the new value of the variable. This is done with the `textvariable` configuration option (`StringVar`)
#   4. wraplength: let Tk calculate the line breaks rather than explicitly embedding line ending in the text string.
#      no effect? todo
#
# Displaying Images
#   1. The `image` configuration option set the displaying text of Label.
#   2. Labels can display both an image and text at the same time, using the `compound` configuration option.
#      "text"-display text only, "image"-display image only, "center"-display text in the center of image,
#      "top"-display text in the top of image, "bottom"-display text in the bottom of image,
#      "left"-display text in the left of image, "right"-display text in the right of image.
#
# width (无 height, lineheight)
#   1. Specify the explicit width of the contents-box (not the width of Label).
#      If the size of contents-box is less than the size of min-required-contents-box, the remainder contents is hidden.
#      If the size of contents-box is larger than the size of min-required-contents-box, there are some space exists.
#   2. justify: horizontal alignment of text, when width is greater than the length of the text. no effect? todo
#      "left", "center" or "right".
#   3. anchor: align，when the contents-box is large than the min-required-contents-box. default value is 'w'.
#      "n" (north), "ne" (north-east), "e", "se", "s", "sw", "w", "nw", or "center"
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
#   2. `borderwidth` no effect? todo
#
#   borderwidth value: `350` means 350 pixels, `"350c"` means 350 centimeters ...
#   relief value: `flat` (default), `raised`, `sunken`, `solid`, `ridge`, or `groove`. (constants.py: SUNKEN='sunken')
#
# style
#   Labels have a `style` configuration option, which is common to all of the themed widgets.
#   This lets you control many other aspects of their appearance or behavior.
#
# underline
#   1. Specify the index of underline of the text, a int value, eg: 0 or 1 or ...
#
# Font
#   1. You can specify the font used to display the label's text using the `font` configuration option.
#
# Color
#   1. `foreground` and `background` configuration options. set the foreground and background color.
#
# state, todo
# takefocus, cursor, class, todo

root.mainloop()

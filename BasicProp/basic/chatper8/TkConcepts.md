# Widgets
Tk提供了一系列 widget class.

## Widget Hierarchy
In our tk_sample example, we created a single *Frame* as a child of the root window, and that Frame had all the other controls as children.  
The root window was a container for the Frame and was, therefore, the **Frame's parent**. The complete hierarchy for the example looked like this:  
![The widget hierarchy of the tk_sample example](hierarchy.png)  

## Creating Widgets
构造 widget class 的实例对象，即创建了对应的 widget. 当创建 widget 时，必须指定其 parent widget. 不过，一个**Tk窗口**是顶层widget, 顶层widget没有parent.  
```python
from tkinter import *
from tkinter import ttk

root = Tk()
f = ttk.Frame(root)  # the at least argument is parent widget
b = ttk.Button(f)
```
Whether or not you save the widget object in a variable is entirely up to you, depending on whether you'll need to refer to it later.  
Because the object is inserted into the widget hierarchy, it won't be garbage collected even if you don't keep your own reference to it.  

> If you sneak a peek at how Tcl manages widgets, you'll see each widget has a **specific pathname**;  
> you'll also see this pathname referred to in Tk reference documentation.  
> Tkinter chooses and manages all these pathname for you behind the scenes, so you should never have to worry about them.  
> If you do, you can get the pathname from a widget by calling str(widget).  

## Configuration Options
All widgets have several configuration options that control how the widget is displayed or how it behaves.  
The available options for a widget depend upon the widget class.  
There is a lot of consistency between different widget classes, so options that do similar things tend to be named the same.  
For example, both a button and a label have a `text` option to adjust the text that the widget displays, while a scrollbar would not have a `text` option since it's not needed.  
Similarly, the button has a `command` option telling it what to do when pushed, while a label, which holds just static text, does not.

Configuration options can be set when the widget is first created by specifying their names and values as optional parameters.  
Later, you can retrieve(取得) the current values of those options, and with a tiny number of exceptions(除了极少数例外), change them at any time.  
```python
from tkinter import *
from tkinter import ttk

root = Tk()
f = ttk.Frame(root)

b = ttk.Button(f, text="Hello", command="buttonPressed")

# 获取 text option 的值
print(b['text'])  # Hello

# 修改 text option 的值
b['text'] = 'World'
# 另外一种方式修改 text option 的值
b.configure(text='World')
print(b['text'])  # World

# 获取 text option 的详细描述
print(b.configure('text'))  # ('text', 'text', 'Text', '', 'World')

# 获取 all option 的详细信息, (option's name, option's name in the database, class, default value, current value)
print(b.configure())
'''
{'command': ('command', 'command', 'Command', '', 'buttonPressed'), 

'default': ('default', 'default', 'Default', <index object: 'normal'>, <index object: 'normal'>), 

'takefocus': ('takefocus', 'takeFocus', 'TakeFocus', 'ttk::takefocus', 'ttk::takefocus'), 

'text': ('text', 'text', 'Text', '', 'World'), 

'textvariable': ('textvariable', 'textVariable', 'Variable', '', ''), 

'underline': ('underline', 'underline', 'Underline', -1, -1), 

'width': ('width', 'width', 'Width', '', ''), 

'image': ('image', 'image', 'Image', '', ''), 

'compound': ('compound', 'compound', 'Compound', 

<index object: 'none'>, <index object: 'none'>), 

'padding': ('padding', 'padding', 'Pad', '', ''), 

'state': ('state', 'state', 'State', <index object: 'normal'>, <index object: 'normal'>), 

'cursor': ('cursor', 'cursor', 'Cursor', '', ''), 

'style': ('style', 'style', 'Style', '', ''), 'class': ('class', '', '', '', '')}
'''

```

## Widget Introspection(内省)
Tk exposes a treasure trove of information about each and every widget that your application can take advantage of.  
Much of it is available via the winfo facility; see the winfo command reference for full details.  

The following are some of the most useful methods:  
- *winfo_class*: a class identifying the type of widget, e.g., TButton for a themed button
- *winfo_children*: a list of widgets that are the direct children of a widget in the hierarchy
- *winfo_parent*: parent of the widget in the hierarchy
- *winfo_toplevel*: the toplevel window containing this widget
- *winfo_width*, *winfo_height*: current width and height of the widget; **not accurate until it appears onscreen**
- *winfo_reqwidth*, *winfo_reqheight*: the width and height that the widget requests of the geometry manager (more on this shortly)
- *winfo_x*, *winfo_y*: the position of the top-left corner of the widget relative to its parent
- *winfo_rootx*, *winfo_rooty*: the position of the top-left corner of the widget relative to the entire screen
- *winfo_vieweable*: whether the widget is displayed or hidden (all its ancestors in the hierarchy must be viewable for it to be viewable)

## Themed Widgets
ttk module provides the themed widgets, which lets you control many other aspects of their appearance or behavior. 
In classic Tk, you could provide a wide range of options to finely control every aspect of an individual widget's behavior, 
e.g., foreground color, background color, font, highlight thickness, selected foreground color, and padding. 
When using the new themed widgets, these changes are made by modifying styles, not adding options to each widget.  


# Geometry Management
Widgets don't appear on the screen just by creating them.  
**Placing widgets on the screen (and precisely where they are placed)** is a separate step called *geometry management*.  

As the tk_sample showed, grid is a selection of *geometry management* of which there are several in Tk (pack, place, grid), grid being the most useful.  

A geometry manager's job is to figure out exactly where those widgets are going to be put. This turns out to be a complex optimization problem, 
and a good geometry manager relies on quite sophisticated(复杂的) algorithms. A good geometry manager provides the flexibility, power, and ease of use that makes programmers happy.  
It also makes it easy to create appealing(有吸引力的) user interface layouts without needing to jump through hoops. Tk's grid is, without a doubt, one of the absolute best.  
A poor geometry manager... well, all the Java programmers who have suffered through "GridBagLayout" please raise their hands.  

## Considering
The geometry manager has to balance multiple constraints(约束). Consider these situations:  
1. The widgets may have a *natural size*, e.g., the natural width of a label would depend on the text it displays and the font used to display it.
    - What if the application window containing all these different widgets isn't big enough to accommodate(容纳) them? 
    - The geometry manager must decide which widgets to shrink(收缩) to fit, by how much, etc.
2. If the application window is bigger than the natural size of all the widgets.
    - How is the extra space used? Is extra space placed between each widget, and if so, how is that space distributed(被分配)? 
    - Is it used to make certain widgets larger than they usually are, such as a text entry growing to fill a wider window? Which widgets should grow?
3. If the application window is resized, how does the **size** and **position** of each widget inside it change? 
    - Will certain areas (e.g., a text entry area) expand or shrink while other parts stay the same size, or is the area distributed differently?
    - Do certain widgets have a minimum size that you want to avoid going below? A maximum size? Does the window itself have a minimum or maximum size?
4. How can widgets in different parts of the user interface be aligned with each other? 
    - How much space should be left between them? This is needed to present a clean layout and comply with platform-specific user interface guidelines.
5. For a complex user interface, which may have many frames nested in other frames nested in the window (etc.).
    - How can all the above be accomplished, trading off the conflicting demands of different parts of the entire user interface?

## How it Works
Geometry management in Tk relies on the concept of **master** and **slave** widgets.  
A master is a widget, typically a toplevel application window or a frame. It contains other widgets, called slaves.  
You can think of a geometry manager taking control of the master widget and deciding how all the slave widgets will be displayed within.  

The geometry manager collects information about the **slaves** in the **master** and the total size of the master.  
It asks each **slave** widget for its natural size, i.e., how large it would ideally be displayed.  
The geometry manager's internal algorithm calculates the area each **slave** will be allocated (if any!).  
The **slave** is then responsible for rendering itself within that particular rectangle.  
And of course, we repeat the whole thing whenever the size of the master changes (e.g., because the toplevel window was resized), 
the natural size of a slave changes (e.g., because we've changed the text in a label), or any geometry manager parameters change (e.g., like row, column, or sticky).

Each master can be managed by only one geometry manager, different masters can have different geometry managers.

We've been assuming that slave widgets are the immediate children of their master in the widget hierarchy.  
While this is usually the case, and mostly there's no good reason to do it any other way, it's also possible (with some restrictions) to get around(绕过) this.


# Event Handling
As with most user interface toolkits, Tk runs an *event loop* that receives events from the operating system.  
These are things like button presses, keystrokes, mouse movement, window resizing, and so on.  

Generally, Tk takes care of managing this event loop for you. It will figure out what widget the event applies to (did a user click on this button? if a key was pressed, which textbox had the focus?), 
and dispatch(调度) it accordingly(依照于此).  
Individual widgets know how to respond to events; for example, a button might change color when the mouse moves over it and revert(恢复) back when the mouse leaves.  

It's critical(关键的) in event-driven applications that the event loop not be blocked(阻塞). The event loop should run continuously(连续不断地), normally executing dozens(数十) of steps per second.  
At every step, it processes an event. If your program is performing a long operation, it can potentially(潜在地) block the event loop.  
In that case, no events would be processed, no drawing would be done, and it would appear as if your application is frozen.  
There are many ways to avoid this happening, mostly related to the structure of your application. We'll discuss this in more detail in a later chapter.  

## Command Callbacks
You often want your program to **handle some event in a particular way**, e.g., do something when a button is pushed.  
For those events that are most frequently customized, the widget will allow you to specify a callback as a widget configuration option(eg, the `command` option of the *button*).  

## Event, Bind, Unbind, Virtual Event
For events that don't have a widget-specific command callback associated with them, you can use Tk's `bind` to capture any event and then execute an arbitrary piece of code.  
more details see the doc of `bind`.  
```python
from tkinter import *
Misc.bind(...)
```





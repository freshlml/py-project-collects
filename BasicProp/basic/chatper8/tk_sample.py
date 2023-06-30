from tkinter import *
from tkinter import ttk

root = Tk()  # tk窗口 (Application Window)
root.title("Feet to Meters")


def calculate(*args, **kwargs):
    try:
        value = float(feet_var.get())
        meters_var.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass


s = ttk.Style()
s.configure('Danger.TFrame', background='gray')

# 创建 Frame widget (Frame is a container)，指定其 parent widget 为tk窗口
mf = ttk.Frame(root, style="Danger.TFrame", padding="3 3 12 12")  # padding="W N E S"
# grid函数，将 Frame 放置到其 parent widget 上, column、row参数指定放置的网格位置
# sticky参数指定: if cell is larger on which sides will this widget stick to the cell boundary
# note: 默认情况下，tk窗口被鼠标拖拽产生伸缩不会造成cell的伸缩
mf.grid(row=0, column=0, sticky=(W, E, N, S))

# 为tk窗口配置column=0, 表示index=0的column的所有cell在x方向随tk窗口被鼠标拖拽产生伸缩而伸缩(一旦cell伸缩，sticky参数将发挥作用)
root.columnconfigure(0, weight=1)
# 为tk窗口配置row=0, 表示index=0的row的所有cell在y方向随tk窗口被鼠标拖拽产生伸缩而伸缩(一旦cell伸缩，sticky参数将发挥作用)
root.rowconfigure(0, weight=1)
# note: 如果同时配置column与row，并不表示坐标为(column, row)的一个cell，而是一个十字形状
# note: 可以配置多个column或row，拉伸的值均分给这多个column或row


feet_var = StringVar()
# 创建 Entry widget (one-line text), 指定其parent widget 为Frame widget
feet_entry = ttk.Entry(mf, width=7, textvariable=feet_var)
# grid函数，将 Entry 放置到其 parent widget 上, column、row参数指定放置的网格位置
# sticky参数指定: if cell is larger on which sides will this widget stick to the cell boundary
# note: 默认情况下，Frame跟随tk窗口伸缩产生的伸缩不会造成cell的伸缩
feet_entry.grid(row=0, column=1, sticky=W)
mf.columnconfigure(1, weight=1)  # 为Frame配置column=1(整个第2列)的所有cell，使得这些cell随Frame的伸缩而伸缩


c = ttk.Style()
c.configure('Danger.TLabel', background='blue')

meters_var = StringVar()
meters_label = ttk.Label(mf, style="Danger.TLabel", textvariable=meters_var)
meters_label.grid(row=1, column=1, sticky=(W, E))


ttk.Button(mf, text="Calculate", command=calculate).grid(row=2, column=2, sticky=W)

ttk.Label(mf, text="feet").grid(row=0, column=2, sticky=W)

ttk.Label(mf, text="is equivalent to").grid(row=1, column=0, sticky=E)

ttk.Label(mf, text="meters").grid(row=1, column=2, sticky=W)


for child in mf.winfo_children():
    child.grid_configure(padx=10, pady=10)


feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()



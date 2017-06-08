# 导入tkinter包,3.6版本
import tkinter
root = tkinter.Tk()
# 进入消息循环
root.mainloop()

#############################

# # 另一种导包方式
# import tkinter as tk
# root = tk.Tk()
# # 进入消息循环
# root.mainloop()

#############################

# #标题的窗口
# import tkinter as tk
# #没有写标题会默认tk为标题
# root = tk.Tk(className="标题")
# #进入消息循环
# root.mainloop()

#############################

# # 带有列表的窗口
#
# from tkinter import *           # 导入 Tkinter 库
# root = Tk(className="列表窗口")      # 创建窗口对象的背景色
#                                 # 创建列表
# li  = ['C','python','php','html','SQL','java']
# listb  = Listbox(root)          #  创建两个列表组件
#
# for item in li:                 # 第一个小部件插入数据
#     listb.insert(0,item)
#
# listb.pack()                    # 将小部件放置到主窗口中
# root.mainloop()                 # 进入消息循环
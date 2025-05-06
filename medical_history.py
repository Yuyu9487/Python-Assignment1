import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Table Example")

# 创建 Treeview 表格
table = ttk.Treeview(root, columns=("Name", "Age", "Disease", "Allergy"), show="headings")
table.heading("Name", text="Name")
table.heading("Age", text="Age")
table.heading("City", text="City")
table.heading("Disease", text="Disease")
table.heading("Allergy", test="Allergy")

# 插入一些数据
table.insert("", "end", values=("Alice", 30, "Asthma","Seafood"))
table.insert("", "end", values=("Bob", 25, "Babesiosis","Protein"))
table.insert("", "end", values=("Charlie", 35, "Cervical Cancer","None"))

table.pack()
root.mainloop()
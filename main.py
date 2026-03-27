# from tkinter import *
import numpy as np
# window = Tk()
# window.minsize(width=500, height=200)
# my_label = Label(text="Hello", font=("Arial",24,"bold"))
# my_label.pack()
# canvas = Canvas(width=100, height=50)


# window.mainloop()

# my_arr = np.array([4,5,6,8,5])
# print(my_arr.shape)

# import pandas as pd

# data = {"Name":['John','Sonw'], "Age":[45,89]}
# # df = pd.DataFrame(data)
# # print(df)
# print(pd.Series(data))

# mul = lambda a,b : a*b
# print(mul(4,5))

data = [("A",25),("B",20),("C",45)]

sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)
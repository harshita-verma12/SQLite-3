import tkinter as tk

window = tk.Tk()
window.title("GUI")
window.geometry("400x300")

label = tk.Label(window,text="HELLO ! welcome to the expense tracker.")
label.grid(column=0, row=0, columnspan=2, pady=5)

l1 = tk.Label(window, text="SPEND WISELY!", font=("Arial",50,"bold"),fg="red",bg ="blue")
l1.grid(column=0, row=1, columnspan=2, pady=10)

txt = tk.Entry(window,width=10)
txt.grid(column=1, row=2, padx=10, pady=5)

def clicked():
    res ="you are registered successfully!"+ txt.get()
    l1.configure(text=res)


bt = tk.Button(window, text="Register!" , command=clicked)
bt.grid(column=1, row=3, pady=10)




window.mainloop()
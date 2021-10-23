from tkinter import *


def relogio():
    import time

    agora = time.localtime()
    hor = agora.tm_hour
    mim = agora.tm_min
    seg = agora.tm_sec

    if hor < 10:
        hor = f"0{hor}"
    if mim < 10:
        mim = f"0{mim}"
    if seg < 10:
        seg = f"0{seg}"
    
    label.config(text=f"{hor}:{mim}:{seg}", font="normal 30", bg="white", relief="raised", borderwidth=4)
    app.after(1000, relogio)


app = Tk()
app.title("Relogio Local")
app.geometry("350x250")
app.resizable(False, False)
app["bg"] = "gray"

label = Label(app)
label.place(x=84, y=100)

relogio()

app.mainloop()

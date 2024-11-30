
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\12244\Desktop\Git\itms448-groupproject\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("300x600")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 300,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    300.0,
    220.0,
    fill="#7195A4",
    outline="")

canvas.create_rectangle(
    0.0,
    561.0,
    300.0,
    600.0,
    fill="#7195A4",
    outline="")

canvas.create_text(
    54.0,
    61.0,
    anchor="nw",
    text="Transaction ",
    fill="#000000",
    font=("DMSerifText Regular", 36 * -1)
)

canvas.create_text(
    88.0,
    110.0,
    anchor="nw",
    text="History",
    fill="#000000",
    font=("DMSerifText Regular", 36 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    150.0,
    391.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("historyButton.png"))
History = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("History clicked"),
    relief="flat"
)
History.place(
    x=10.0,
    y=539.0,
    width=55.0,
    height=42.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("investButton.png"))
Invest = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Invest clicked"),
    relief="flat"
)
Invest.place(
    x=86.0,
    y=539.0,
    width=55.0,
    height=42.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=160.0,
    y=539.0,
    width=55.0,
    height=42.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=236.0,
    y=539.0,
    width=55.0,
    height=42.0
)

button_image_hover_2 = PhotoImage(
    file=relative_to_assets("invest_hover_1.png"))

def Invest_hover(e):
    Invest.config(
        image=button_image_hover_2
    )
def Invest_leave(e):
    Invest.config(
        image=button_image_2
    )

Invest.bind('<Enter>', Invest_hover)
Invest.bind('<Leave>', Invest_leave)


button_image_hover_3 = PhotoImage(
    file=relative_to_assets("button_hover_2.png"))

def button_3_hover(e):
    button_3.config(
        image=button_image_hover_3
    )
def button_3_leave(e):
    button_3.config(
        image=button_image_3
    )

button_3.bind('<Enter>', button_3_hover)
button_3.bind('<Leave>', button_3_leave)


button_image_hover_4 = PhotoImage(
    file=relative_to_assets("button_hover_3.png"))

def button_4_hover(e):
    button_4.config(
        image=button_image_hover_4
    )
def button_4_leave(e):
    button_4.config(
        image=button_image_4
    )

button_4.bind('<Enter>', button_4_hover)
button_4.bind('<Leave>', button_4_leave)


canvas.create_text(
    17.0,
    552.0,
    anchor="nw",
    text="History",
    fill="#000000",
    font=("DMSerifText Regular", 12 * -1)
)

canvas.create_text(
    98.0,
    552.0,
    anchor="nw",
    text="Invest",
    fill="#FFFFFF",
    font=("DMSerifText Regular", 12 * -1)
)

canvas.create_text(
    162.0,
    552.0,
    anchor="nw",
    text="Exchange",
    fill="#FFFFFF",
    font=("DMSerifText Regular", 12 * -1)
)

canvas.create_text(
    246.0,
    552.0,
    anchor="nw",
    text="Budget",
    fill="#FFFFFF",
    font=("DMSerifText Regular", 12 * -1)
)

canvas.create_text(
    30.0,
    256.0,
    anchor="nw",
    text="Transaction 4  -- 11/29/24 9:32 pm -- $28.27",
    fill="#000000",
    font=("IstokWeb Regular", 12 * -1)
)

canvas.create_text(
    30.0,
    321.0,
    anchor="nw",
    text="Transaction 3  -- 11/28/24 3:25 pm -- $28.27",
    fill="#000000",
    font=("IstokWeb Regular", 12 * -1)
)

canvas.create_text(
    30.0,
    386.0,
    anchor="nw",
    text="Transaction 2  -- 11/27/24 9:54 am -- $28.27",
    fill="#000000",
    font=("IstokWeb Regular", 12 * -1)
)

canvas.create_text(
    30.0,
    441.0,
    anchor="nw",
    text="Transaction 1  -- 11/26/24 6:17 pm -- $28.27",
    fill="#000000",
    font=("IstokWeb Regular", 12 * -1)
)
window.resizable(False, False)
window.mainloop()
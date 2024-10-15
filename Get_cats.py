import requests
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO


def get_cat(url):
    info_image = requests.get(url)
    image = BytesIO(info_image.content)
    img = Image.open(image)
    img_tk = ImageTk.PhotoImage(img)
    img.thumbnail(500,400)
    return img_tk

window = Tk()
window.title('Cats')
window.geometry(f'500x400+{window.winfo_screenwidth()//2-250}+{window.winfo_screenheight()//2-200}')
window.iconbitmap('cat_icons.ico')
url = 'https://cataas.com/cat'
img = get_cat(url)
t_m = Label(window, image=img)

btn = Button(window, text='Получить кота')
t_m.pack()





window.mainloop()
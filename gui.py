from tkinter import *
import PyPDF2
from tkinter import filedialog 
from Summarizer import summarize
from functools import partial
root=Tk()
root.title('Summarize your Document')
root.iconbitmap()
root.geometry("500x500")
my_text=Text(root, height=80, width=100)
my_text.pack(pady=10)
result=""
def open_pdf():

    open_file=filedialog.askopenfilename(
        initialdir="C:/Users/sinha/OneDrive/proj",
        title="Summarize pdf",
        filetypes=(
            ("PDF Files","*.pdf"),
            ("All Files","*.*")
        )
    )
    if open_file:
        result=summarize(open_file)
        my_text.insert(1.0, result)


def clear_text_box():
    my_text.delete(1.0 , END)


my_menu=Menu(root)
root.config(menu=my_menu)
file_menu=Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Open",command=open_pdf)
file_menu.add_command(label="Clear",command=clear_text_box)
file_menu.add_separator
file_menu.add_command(label="Exit",command=root.quit)
root.mainloop()
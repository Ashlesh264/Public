import qrcode
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os


# Creating the window
wn = Tk()
wn.title('QR Code Generator')
wn.geometry('700x800')
wn.config(bg='SteelBlue3')

# Label for the window
headingFrame = Frame(wn, bg="azure", bd=5)
headingFrame.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.1)
headingLabel = Label(headingFrame, text="Generate QR Code", bg='azure', font=('Times', 20, 'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# Input Frame
Frame1 = Frame(wn, bg="SteelBlue3")
Frame1.place(relx=0.1, rely=0.15, relwidth=0.7, relheight=0.3)

Label(Frame1, text="Enter the text/URL: ", bg="SteelBlue3", fg='azure', font=('Courier', 13, 'bold')).place(relx=0.05, rely=0.2, relheight=0.08)
text = Entry(Frame1, font=('Century 12'))
text.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

# Save Location
Frame2 = Frame(wn, bg="SteelBlue3")
Frame2.place(relx=0.1, rely=0.35, relwidth=0.7, relheight=0.3)

Label(Frame2, text="Enter the location to save the QR Code: ", bg="SteelBlue3", fg='azure', font=('Courier', 13, 'bold')).place(relx=0.05, rely=0.2, relheight=0.08)
loc = Entry(Frame2, font=('Century 12'))
loc.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

# QR Code Name
Frame3 = Frame(wn, bg="SteelBlue3")
Frame3.place(relx=0.1, rely=0.55, relwidth=0.7, relheight=0.3)

Label(Frame3, text="Enter the name of the QR Code: ", bg="SteelBlue3", fg='azure', font=('Courier', 13, 'bold')).place(relx=0.05, rely=0.2, relheight=0.08)
name = Entry(Frame3, font=('Century 12'))
name.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

# QR Code Size
Frame4 = Frame(wn, bg="SteelBlue3")
Frame4.place(relx=0.1, rely=0.75, relwidth=0.7, relheight=0.2)

Label(Frame4, text="Enter the size from 1 to 40 (1=21x21): ", bg="SteelBlue3", fg='azure', font=('Courier', 13, 'bold')).place(relx=0.05, rely=0.2, relheight=0.08)
size = Entry(Frame4, font=('Century 12'))
size.place(relx=0.05, rely=0.4, relwidth=0.5, relheight=0.2)

# QR Code Generator Function
def generateCode():
    try:
        if not text.get() or not loc.get() or not name.get():
            messagebox.showerror("Error", "All fields are required!")
            return

        qr_size = int(size.get())
        if qr_size < 1 or qr_size > 40:
            raise ValueError("Size must be between 1 and 40.")

        qr = qrcode.QRCode(version=qr_size, box_size=10, border=5)
        qr.add_data(text.get())
        qr.make(fit=True)

        file_path = os.path.join(loc.get() or os.path.expanduser("~"), f"{name.get()}.png")
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(file_path)

        # Preview QR Code
        qr_image = ImageTk.PhotoImage(img)
        qr_label = Label(wn, image=qr_image, bg="SteelBlue3")
        qr_label.image = qr_image
        qr_label.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.3)

        messagebox.showinfo("Success", f"QR Code saved at {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Generate Button
button = Button(wn, text='Generate Code', font=('Courier', 15), command=generateCode)
button.place(relx=0.35, rely=0.9, relwidth=0.25, relheight=0.05)

# Run the Window
wn.mainloop()

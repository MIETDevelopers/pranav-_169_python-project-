import PIL.Image
import cv2
import pytesseract
import tkinter.filedialog
import pyttsx3
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox as msg

class upload_screen(Tk):
    def __init__(self):
        super().__init__()
        self.title("Text Extractor")
        self.config(bg="#FFFFFF")
        self.geometry("800x500")
        self.maxsize(800, 500)

        self.icon = ImageTk.PhotoImage(PIL.Image.open("text_icon.jpg"))
        self.icon_label = Label(image=self.icon, bg="white").place(x=25, y=120)

        self.f1 = Frame(self, height=400, width=400).place(x=350, y=40)
        Label(self.f1, text="Extraction of text from image",
              font="MicrosoftYaheiUiLight 18").place(x=400, y=80)
        Label(self.f1, text="Insert image",
              font="MicrosoftYaheiUiLight 13").place(x=400, y=160)
        Button(self.f1, text="Browse", font="MicrosoftYaheiUiLight 10",
               command=self.browse).place(x=550, y=160)

        Label(self.f1, text="To exit",
              font="MicrosoftYaheiUiLight 13").place(x=400, y=260)
        Button(self.f1, text="Exit", font="MicrosoftYaheiUiLight 10",
               command=self.destroy).place(x=550, y=260)

    def browse(self):
        self.path = tkinter.filedialog.askopenfilename(
            filetypes=[("JPG File", ".jpg"), ("PNG file", ".png"), ("All files", "*.*")])
        if (self.path):
            Label(self, text="To extract text:",
                  font="MicrosoftYaheiUiLight 13").place(x=400, y=370)
            Button(self, text="Extract Text", font="MicrosoftYaheiUiLight 10",
                   command=self.extract_text).place(x=550, y=370)

        else:
            msg.showerror("Error", "File not selected")

    def extract_text(self):
        img = cv2.imread(self.path)
        gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("img", gray_scale)
        cv2.waitKey(0)
        text = pytesseract.image_to_string(gray_scale)
        self.destroy()
        text_screen = text_extractor(text)
        text_screen.mainloop()


class text_extractor(Tk):
    def __init__(self, extracted_text):
        super().__init__()
        self.text_ = extracted_text
        self.title("Text Extractor")
        self.config(bg="#FFFFFF")
        self.geometry("800x750")
        self.maxsize(1300, 750)
        Button(self, text="Save file", font="MicrosoftYaheiUiLight 10",
               command=self.save_file).place(x=700, y=675)
        Label(self, text=self.text_,
              font="MicrosoftYaheiUiLight 12",padx=10,pady=10).place(x=175, y=50)
        Button(self, text="Text to speech", font="MicrosoftYaheiUiLight 10",
               command=self.text_to_audio).place(x=600, y=675)
        Button(self, text="Back", font="MicrosoftYaheiUiLight 10",
               command=self.back).place(x=500, y=675)
    
    def back(self):
        self.destroy()
        main_ = upload_screen()
        main_.mainloop()
        

    def save_file(self):
        file=tkinter.filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"),("Microsoft Word file",".docx")])

        file_obj = open(file,"w")
        file_obj.write(self.text_)
        file_obj.close()

    def text_to_audio(self):
        t1=pyttsx3.init()
        t1.say(self.text_)
        t1.setProperty('rate',120)
        t1.setProperty('volume',0.9)
        t1.runAndWait()
      
    

root = upload_screen()
root.mainloop()

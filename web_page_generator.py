import tkinter as tk
from tkinter import *
from tkinter import ttk
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title("Web Page Generator")

        self.varText = StringVar()

        #Creates label for Enter custom text
        self.lblEnter = Label(self.master, text="Enter custom text or click the Default HTML page button", font=("Helvetica", 12))
        self.lblEnter.grid(row=0, column=0,padx=(30,0), pady=(30,0))

        #Creates label display
        self.lblDisplay = Label(self.master, text="", font=("Helvetica", 12))
        self.lblDisplay.grid(row=1, column=1,padx=(30,30), pady=(30,0))

        #Creates display input text box
        self.displayText = Entry(self.master,text=self.varText, font=("Helvetica", 12))
        self.displayText.grid(row=1, column=1,padx=(30,30), pady=(30,0), sticky=E)

        #Creates Default HTML Page
        self.btn = Button(self.master, text="Default HTML Page", width=20, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=0, padx=(0,10) , pady=(30,0), sticky=NE)
        
        #Creates Submit Button
        self.btnSubmit = Button(self.master, text="Submit Custom Text", width=20, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NW)

        
    #Adding new function that will create HTML document
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
    #Defining function to return Input data
    def submit(self):
        customText = ""
        customText = self.displayText.get()
        customFile = open("customindex.html", "w")
        customContent = "<html>\n<body>\n<h1>" + customText + "</h1>\n</body>\n</html>"
        customFile.write(customContent)
        customFile.close()
        webbrowser.open_new_tab("customindex.html")



        
        
        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

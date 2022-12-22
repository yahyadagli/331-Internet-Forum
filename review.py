"""
    Stage: Development-01
    @author: Giragos Başak 119202045
    @author: Janberk Özsezer 120202040

    Stage: Development-02
    @author: Mustafa Yahya Dağlı 119202067
    @author: Gökay Tan 122202114

    Stage: Development-03 
    Review Session 
    @author: Arda Çelik 119202051
    @author: Janberk Özsezer 120202040
    @author: Ata Aral Candar 120202044
"""

import tkinter as tk
from tkinter import messagebox  # unnecessary import, it isn't used. (dev-03)
from tkinter import *

class LoginWindow:
    # constructor
    def __init__(self):
        self.window = tk.Tk()

        self._initializeGUI()
        self._addGUIElementsToFrame()

        # start the GUI frame
        self.window.mainloop()


    """
        Initialize GUI elements. If it is necessary, you can add
        more elements.

        ! PLEASE RENAME THE OBJECTS ACCORDING TO THEIR PURPOSES !
        ! YOU CAN ADD MORE ELEMENTS IF IT IS NECESSARY !
    """
    def _initializeGUI(self):
        self.lbl01 = tk.Label(text="Username")
        self.lbl02 = tk.Label(text="Password")

        self.username = tk.Entry()
        self.password = tk.Entry()

        self.cancel = tk.Button(text="Cancel", command=self.exit_button)
        self.login = tk.Button(text="Login", command=self.blank_page)

        self.cancel.bind("<Button-1>", self.handle_click) # What it's get used to be is to see login button on the left. (Dev-03)
                                                        # It seems a little bit complicated. To sum up, swapping these two buttons might be better. (Dev-03)
        self.login.bind("<Button-1>", self.handle_click) #To use button 2 can be defined to distinguish easilly. (dev-03)
    
    
    """
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """
    def _addGUIElementsToFrame(self):
        self.lbl01.grid(row=0, column=0, padx=10, pady=5)
        self.username.grid(row=0, column=1, padx=10, pady=5)

        self.lbl02.grid(row=1, column=0, padx=10, pady=5)
        self.password.grid(row=1, column=1, padx=10, pady=5)

        self.cancel.grid(row=2, column=0, padx=10, pady=5)
        self.login.grid(row=2, column=1, padx=10, pady=5)


    """
        Action listener for the buttons. If "event.widget" is from
        one of the buttons, apply the related operation.

        :param event: action event for detecting which button is clicked
    """
    def handle_click(self, event):
        pass

    def exit_button(self):
        exit()

    def blank_page(self):
        if self.username.get() == 'janberk' and self.password.get() == '123':
            
            
            self.window = tk.Tk()
            self._initializeGUI()
            self._addGUIElementsToFrame()
            self.window.title("Forum")
            self.window.geometry("400x300")


            # instead of adding check button, combobox might be better to have a better visualisation. (Dev-03) 
            # The system let me to pick more than one button. To warn the user in this case could be more beneficial (Dev-03) . 
            self.lbl03 = tk.Label (self.window, text="Kategori Seçiniz")
            self.lbl03.grid(padx=10, pady=10)
            # Adding the checkbutton library from Tkinter and we created 4 buttons in the form of 2 rows and 2 columns  
            self.chek1=Checkbutton(self.window, text = "Sesli Sohbet", onvalue = 1, offvalue = 0, height=5, width = 20)
            self.chek1.grid(row=1, column=0, padx=11, pady=10)
    
            self.chek2=Checkbutton(self.window, text = "Blog", onvalue = 1, offvalue = 0, height=5, width = 20)
            self.chek2.grid(row=1, column=1, padx=11, pady=5)
              
            self.chek3=Checkbutton(self.window, text = "Görüntülü Sohbet", onvalue = 1, offvalue = 0, height=5, width = 20)
            self.chek3.grid(row=2, column=0, padx=11, pady=10)
             
            self.chek4=Checkbutton(self.window, text = "Haberler", onvalue = 1, offvalue = 0, height=5, width = 20)
            self.chek4.grid(row=2, column=1, padx=11, pady=5)

            self.btn01 = tk.Button(self.window, text="Yönlendir") 
            self.btn01.grid(padx=10, pady=10) 

            self.window.mainloop()
            
        
# main method for testing the application
if __name__ == "__main__":
    LoginWindow()
    
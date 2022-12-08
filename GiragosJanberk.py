"""
    Stage: Development-01
    @author: Giragos Başak 119202045
    @author: Janberk Özsezer 120202040
"""

import tkinter as tk


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

        self.cancel.bind("<Button-1>", self.handle_click)
        self.login.bind("<Button-1>", self.handle_click)
       
    
        


       




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
            self.window.mainloop()
            
        



# main method for testing the application
if __name__ == "__main__":
    LoginWindow()
    
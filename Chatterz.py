import os, sys
import customtkinter
from Views.View import App

if __name__== "__main__":
    try:
        root = customtkinter.CTk()
        app = App(root)
        app.mainPage()
        while True:
            root.update()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
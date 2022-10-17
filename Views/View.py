import os, sys
from cgitb import text
from re import A
import tkinter
from tkinter import font
from tkinter.tix import COLUMN
from turtle import color
import customtkinter
from Models import global_variables
from Controllers.CoreController import Controller

class App:
    WIDTH = 620
    HEIGHT = 700
    TITLE = "Chatterz"

    def __init__(self, root):
        # Initializing my App class by the parent class constructor
        self.root = root

        # General settings of the app that all pages are going to have
        self.root.title(self.TITLE)
        self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # Text font creation
        self.TITLE_FONT = font.Font(family="Helvetica",
                                    name="TITLE_FONT",
                                    size=30, 
                                    weight="bold")

    def mainPage(self):
        for i in self.root.winfo_children():
            i.destroy()
        
       
        # Main page background color configuration
        self.root.configure(bg=("gray20", "white"))

        # Grid layout configuration (2x4)
        self.root.rowconfigure(0, minsize=40)
        self.root.rowconfigure((4,5), weight=0, minsize=0)
        self.root.rowconfigure((1,2,3), weight=1)
        self.root.rowconfigure((4,5,6,7,8,9,10,12), weight=0, minsize=0)
        self.root.columnconfigure((0,1), weight=1, minsize = 0)
        self.root.columnconfigure(2, weight=0, minsize = 0)
        self.root.columnconfigure(3, weight=0, minsize = 0)

        # Text of labels
        text_page_label = tkinter.StringVar(value=self.TITLE)
        text_description_label = tkinter.StringVar(value="    Introducing to you one of the best\n\nchatting apps in terms"+ 
                                            " of security and privacy.\n\n\n"+  
                                            "    This app's architecture is produced with\n\n"+ 
                                            "peer to peer communication in mind.\n\n")

        # Labels
        page_label = customtkinter.CTkLabel(master=self.root,
                               textvariable=text_page_label,
                               width=120,
                               height=25,
                               text_font="TITLE_FONT",
                               text_color=("white", "gray20")
        ).grid(row=0, 
            column=0, 
            columnspan=2, 
            pady=50
        )

        separatingBarrier = customtkinter.CTkFrame(master=self.root,
                               width=2,
                               height=300,
                               corner_radius=300,
                               fg_color="grey40"
        ).place(relx=0.68,
                rely=0.52, 
                anchor=tkinter.CENTER
        )

        descriptionLabel = customtkinter.CTkLabel(master=self.root,
                               textvariable=text_description_label,
                               width=120,
                               height=25,
                               text_font=("TkTextFont",14),
                               justify=tkinter.LEFT,
                               text_color=("white", "gray20")
        ).grid(row=1, 
            column=0, 
            rowspan=2, 
            sticky="w", 
            padx=30
        )

        # Login button
        loginButton = customtkinter.CTkButton(master=self.root,
                                  text="LOGIN",
                                  command=self.loginPage,
                                  text_color="black",
                                  corner_radius=6,
                                  height=50,
                                  fg_color="green",
                                  text_font=("TkCaptionFont",14),
                                  border_color="grey30",
                                  border_width=2
        ).grid(row=1, 
            column=1, 
            padx=20, 
            pady=30,
            sticky="sw"
        )

        # Register button
        registerButton = customtkinter.CTkButton(master=self.root,
                                  text="REGISTER",
                                  command=self.registerPage,
                                  text_color="black",
                                  corner_radius=6,
                                  height=50,
                                  fg_color="grey50",
                                  text_font=("TkCaptionFont",14),
                                  border_color="grey30",
                                  border_width=2
        ).grid(row=2, 
            column=1, 
            padx=20, 
            pady=30,
            sticky="nw"
        )

    def loginPage(self):
        for i in self.root.winfo_children():
            i.destroy()
        
        ######## Configuration ########
        # Main page background color configuration
        self.root.configure(bg=("gray20", "white"))

        # Grid layout configuration (2x4)
        self.root.rowconfigure(0, minsize=80)
        self.root.rowconfigure(5, minsize=420)
        self.root.rowconfigure((1,2,3,4), weight=1)
        self.root.rowconfigure((6,7,8,9,10,12), weight=0, minsize=0)
        self.root.columnconfigure(0, weight=1, minsize=630)
        self.root.columnconfigure((1,2,3), weight=0, minsize = 0)

        ######## Text of labels ########
        text_page_label = tkinter.StringVar(value="Login")
        text_email_label = tkinter.StringVar(value="Email")
        text_password_label = tkinter.StringVar(value="Password")

        ######## Labels ########
        page_label = customtkinter.CTkLabel(master=self.root,
                               textvariable=text_page_label,
                               width=120,
                               height=25,
                               text_font="TITLE_FONT",
                               text_color=("white", "gray20")
        ).grid(row=0, 
            column=0, 
            columnspan=2, 
            pady=50
        )

        emailLabel = customtkinter.CTkLabel(master=self.root,
                               textvariable=text_email_label,
                               width=120,
                               height=25,
                               text_font=("TkTextFont",14),
                               justify=tkinter.LEFT,
                               text_color=("white", "gray20"),
                               anchor="w"
        ).grid(row=1, 
            column=0, 
            sticky="ws", 
            padx=150
        )

        passwordLabel = customtkinter.CTkLabel(master=self.root,
                               textvariable=text_password_label,
                               width=100,
                               height=25,
                               text_font=("TkTextFont",14),
                               justify=tkinter.LEFT,
                               text_color=("white", "gray20"),
                               anchor="w"
        ).grid(row=3, 
            column=0, 
            sticky="ws", 
            padx = 150
        )

        ######## Entries ########
        emailEntry = customtkinter.CTkEntry(master=self.root,
                               placeholder_text="Enter your email ...",
                               width=999,
                               height=40,
                               border_width=2,
                               corner_radius=6,
        )
        emailEntry.grid(row = 2,
            column = 0,
            sticky = "wne",
            padx = 150
        )
        
        passwordEntry = customtkinter.CTkEntry(master=self.root,
                               placeholder_text="Enter your password ...",
                               width=999,
                               height=40,
                               border_width=2,
                               corner_radius=6
        )
        passwordEntry.grid(row = 4,
            column = 0,
            sticky = "wne",
            padx = 150
        )

        ######## Buttons ########
        # Back to previous page button
        backButton = customtkinter.CTkButton(master=self.root,
                                  text="←",
                                  command=self.mainPage,
                                  text_color="white",
                                  corner_radius=26,
                                  width=50,
                                  height=50,
                                  fg_color="grey40",
                                  text_font=("TkCaptionFont",24),
                                  border_color="grey30",
                                  border_width=2
        ).grid(row=0, 
            column=0, 
            padx=0, 
            pady=0,
            sticky="nw"
        )

        loginButton = customtkinter.CTkButton(master=self.root,
                                  text="LOGIN",
                                  command=lambda : self.login(emailEntry.get(), passwordEntry.get()),
                                  text_color="black",
                                  corner_radius=6,
                                  height=50,
                                  fg_color="green",
                                  text_font=("TkCaptionFont",14),
                                  border_color="grey30",
                                  border_width=2
        ).grid(row=5, 
            column=0, 
            padx=220, 
            pady=20,
            sticky="nwe"
        )

    def registerPage(self):
        ######## Cleaning widgets ########
        for i in self.root.winfo_children():
            i.destroy()
        
        ######## Configuration ########
        # Main page background color configuration
        self.root.configure(bg=("gray20", "white"))

        # Grid layout configuration (2x4)
        self.root.rowconfigure(0, minsize=80)
        self.root.rowconfigure(5, minsize=150)
        self.root.rowconfigure((1,2,3,4), weight=1)
        self.root.rowconfigure((6,7,8,9,10,12), weight=0, minsize=0)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)
        self.root.columnconfigure(3, weight=0, minsize = 0)

        ######## Text of labels ########
        text_page_label = tkinter.StringVar(value="Register")
        text_name_label = tkinter.StringVar(value="Name")
        text_surname_label = tkinter.StringVar(value="Surname")
        text_email_label = tkinter.StringVar(value="Email")
        text_password_label = tkinter.StringVar(value="Password")
        text_pass_conf_label = tkinter.StringVar(value="Password\nconfirmation")

        ######## Labels ########
        page_label = customtkinter.CTkLabel(master=self.root,
                               textvariable=text_page_label,
                               width=120,
                               height=25,
                               text_font="TITLE_FONT",
                               text_color=("white", "gray20")
        ).grid(row=0, 
            column=0, 
            columnspan=2, 
            pady=50
        )

        emailLabel = customtkinter.CTkLabel(master=self.root,
                               textvariable=text_email_label,
                               width=120,
                               height=25,
                               text_font=("TkTextFont",14),
                               justify=tkinter.LEFT,
                               text_color=("white", "gray20"),
                               anchor="w"
        ).grid(row=1, 
            column=0, 
            sticky="ws", 
            padx=40
        )

        passwordLabel = customtkinter.CTkLabel(master=self.root,
                               textvariable=text_password_label,
                               width=120,
                               height=25,
                               text_font=("TkTextFont",14),
                               justify=tkinter.LEFT,
                               text_color=("white", "gray20"),
                               anchor="w"
        ).grid(row=2, 
            column=0, 
            sticky="ws", 
            padx=40
        )

        passConfLabel = customtkinter.CTkLabel(master=self.root,
                               textvariable=text_pass_conf_label,
                               width=120,
                               height=25,
                               text_font=("TkTextFont",14),
                               justify=tkinter.LEFT,
                               text_color=("white", "gray20"),
                               anchor="w"
        ).grid(row=3, 
            column=0, 
            sticky="ws", 
            padx=40
        )

        ######## Entries ########
        emailEntry = customtkinter.CTkEntry(master=self.root,
                               placeholder_text="Enter your email ...",
                               width=999,
                               height=40,
                               border_width=2,
                               corner_radius=6,
        )
        emailEntry.grid(row = 1,
            column = 0,
            columnspan = 2,
            sticky = "ws",
            padx = (200,160)
        )

        passwordEntry = customtkinter.CTkEntry(master=self.root,
                               placeholder_text="Enter your password ...",
                               width=999,
                               height=40,
                               border_width=2,
                               corner_radius=6,
        )
        passwordEntry.grid(row = 2,
            column = 0,
            columnspan = 2,
            sticky = "wse",
            padx = (200,160)
        )
        
        passConfEntry = customtkinter.CTkEntry(master=self.root,
                               placeholder_text="Enter your password again ...",
                               width=250,
                               height=40,
                               border_width=2,
                               corner_radius=6,
        )
        passConfEntry.grid(row = 3,
            column = 0,
            columnspan = 2,
            sticky = "wse",
            padx = (200,160)
        )

        ####### Buttons ########
        # Back to previous page button
        backButton = customtkinter.CTkButton(master=self.root,
                                  text="←",
                                  command=self.mainPage,
                                  text_color="white",
                                  corner_radius=26,
                                  width=50,
                                  height=50,
                                  fg_color="grey40",
                                  text_font=("TkCaptionFont",24),
                                  border_color="grey30",
                                  border_width=2
        ).grid(row=0, 
            column=0, 
            padx=0, 
            pady=0,
            sticky="nw"
        )

        registerButton = customtkinter.CTkButton(master=self.root,
                                  text="REGISTER",
                                  command=lambda : self.register(emailEntry.get(), passwordEntry.get()),
                                  text_color="black",
                                  corner_radius=6,
                                  height=50,
                                  fg_color="green",
                                  text_font=("TkCaptionFont",14),
                                  border_color="grey30",
                                  border_width=2
        ).grid(row=4, 
            column=0,
            columnspan = 2, 
            padx=220, 
            pady=50,
            sticky="nwe"
        )

    def friendsList(self):
        ######## Cleaning widgets ########
        for i in self.root.winfo_children():
            i.destroy()
        
        ######## Configuration ########
        # Main page background color configuration
        self.root.configure(bg=("gray20", "white"))

        # Grid layout configuration (2x4)
        self.root.rowconfigure(0, minsize=40)
        self.root.rowconfigure((1,2,3,4,5,6,7,8,9,10,12), weight=0, minsize=30)
        self.root.columnconfigure((0,1), weight=1, minsize = 0)
        self.root.columnconfigure(2, weight=0, minsize = 50)
        self.root.columnconfigure(3, weight=0, minsize = 70)

        ######## Entries ########
        searchEntry = customtkinter.CTkEntry(master=self.root,
                               placeholder_text="Search",
                               width=999,
                               height=30,
                               border_width=2,
                               corner_radius=0,
        )
        searchEntry.grid(row = 1,
            column = 0,
            columnspan = 2,
            sticky = "nwes"
        )

        ####### Buttons ########
        friendsListButton = customtkinter.CTkButton(master=self.root,
                                  text="Friend's list",
                                  command=self.friendsList,
                                  corner_radius=0,
                                  height=50,
                                  fg_color="grey30",
                                  text_font=("TkCaptionFont",14),
                                  border_color="grey30",
                                  border_width=0,
                                  state = "disabled",
                                  text_color_disabled="black"
        ).grid(row=0, 
            column=0, 
            padx=0, 
            pady=0,
            sticky="nwe"
        )

        chatHistoryButton = customtkinter.CTkButton(master=self.root,
                                  text="Chat history",
                                  command=self.chatHistory,
                                  text_color="black",
                                  corner_radius=0,
                                  height=50,
                                  fg_color="grey40",
                                  text_font=("TkCaptionFont",14),
                                  border_color="grey30",
                                  border_width=0
        ).grid(row=0, 
            column=1, 
            columnspan = 2,
            padx=0, 
            pady=0,
            sticky="nwe"
        )

        disconnectButton = customtkinter.CTkButton(master=self.root,
                                  text="X",
                                  command=self.disconnect,
                                  text_color="black",
                                  corner_radius=0,
                                  width = 70,
                                  height=50,
                                  fg_color="red",
                                  text_font=("TkCaptionFont",14),
                                  border_color="grey30",
                                  border_width=0
        ).grid(row=0, 
            column=3, 
            padx=0, 
            pady=0,
            sticky="ne"
        )

        searchButton = customtkinter.CTkButton(master=self.root,
                                  text="Search",
                                  command=lambda : self.addFriend(searchEntry.get()),
                                  text_color="black",
                                  corner_radius=0,
                                  width = 110,
                                  height=40,
                                  fg_color="grey30",
                                  text_font=("TkCaptionFont",14),
                                  border_color="grey30",
                                  border_width=0
        ).grid(row=1, 
            column=2, 
            columnspan=2,
            padx=0, 
            pady=0,
            sticky="ne"
        )
        
        friends = self.cont.showFriends()
        friendsList = []
        i = 0
        for friend in friends:
            friendsList.append(customtkinter.CTkButton(master=self.root,
                                  text=friend,
                                  command=lambda fr=friend: self.chat(fr),
                                  text_color="black",
                                  corner_radius=0,
                                  width = 110,
                                  height=50,
                                  fg_color="grey70",
                                  text_font=("TkCaptionFont",14),
                                  border_color="black",
                                  border_width=2
            ))
            friendsList[i].grid(row=i+2, 
                    column=0, 
                    columnspan=4,
                    padx=0, 
                    pady=0,
                    sticky="nwe"
            )
            i+=1


    def chatHistory(self):
        ######## Cleaning widgets ########
        for i in self.root.winfo_children():
            i.destroy()
        
        ######## Configuration ########
        # Main page background color configuration
        self.root.configure(bg=("gray20", "white"))

        # Grid layout configuration (2x4)
        self.root.rowconfigure(0, minsize=40)
        self.root.rowconfigure((1,2,3,4,5,6,7,8,9,10,12), weight=0, minsize=0)
        self.root.columnconfigure((0,1), weight=1, minsize = 0)
        self.root.columnconfigure(2, weight=0, minsize = 0)
        self.root.columnconfigure(3, weight=0, minsize = 70)

        ####### Buttons ########
        friendsListButton = customtkinter.CTkButton(master=self.root,
                                  text="Friend's list",
                                  command=self.friendsList,
                                  corner_radius=0,
                                  height=50,
                                  fg_color="grey40",
                                  text_font=("TkCaptionFont",14),
                                  border_color="grey30",
                                  border_width=0,
        ).grid(row=0, 
            column=0, 
            padx=0, 
            pady=0,
            sticky="nwe"
        )

        chatHistoryButton = customtkinter.CTkButton(master=self.root,
                                  state = "disabled",
                                  text_color_disabled="black",
                                  text="Chat history",
                                  command=self.chatHistory,
                                  text_color="black",
                                  corner_radius=0,
                                  height=50,
                                  fg_color="grey30",
                                  text_font=("TkCaptionFont",14),
                                  border_color="grey30",
                                  border_width=0
        ).grid(row=0, 
            column=1, 
            columnspan = 2,
            padx=0, 
            pady=0,
            sticky="nwe"
        )

        disconnectButton = customtkinter.CTkButton(master=self.root,
                                  text="X",
                                  command=self.disconnect,
                                  text_color="black",
                                  corner_radius=0,
                                  width = 70,
                                  height=50,
                                  fg_color="red",
                                  text_font=("TkCaptionFont",14),
                                  border_color="grey30",
                                  border_width=0
        ).grid(row=0, 
            column=3, 
            padx=0, 
            pady=0,
            sticky="ne"
        )

        chats = self.cont.showMessageHistory()
        chatList = []
        i = 0
        for chat in chats:
            chatList.append(customtkinter.CTkButton(master=self.root,
                                  text=chat[0]+"\n"+chat[1],
                                  command=lambda ch=chat[0]: self.chat(ch),
                                  text_color="black",
                                  corner_radius=0,
                                  width = 110,
                                  height=70,
                                  fg_color="grey90",
                                  text_font=("TkCaptionFont",14),
                                  border_color="black",
                                  border_width=2,
            ))
            chatList[i].grid(row=i+1, 
                column=0, 
                columnspan=4,
                padx=0, 
                pady=0,
                sticky="nwe",
            )
            i+=1
    
    def chat(self, email):
        ######## Cleaning widgets ########
        for i in self.root.winfo_children():
            i.destroy()
        
        ######## Configuration ########
        # Main page background color configuration
        self.root.configure(bg=("gray20", "white"))

        # Grid layout configuration (2x4)
        self.root.rowconfigure((0,1), minsize=40)
        self.root.rowconfigure((2,3,4,5,6,7,8,9,10,12), weight=0, minsize=0)
        self.root.columnconfigure((0,1), weight=0, minsize = 0)
        self.root.columnconfigure(2, weight=1, minsize = 0)
        self.root.columnconfigure(3, weight=1, minsize = 0)

        ####### Buttons ########
        # Back to previous page button
        backButton = customtkinter.CTkButton(master=self.root,
                                  text="←",
                                  command=self.chatHistory,
                                  text_color="white",
                                  corner_radius=26,
                                  width=50,
                                  height=50,
                                  fg_color="grey40",
                                  bg_color="grey50",
                                  text_font=("TkCaptionFont",24),
                                  border_color="grey30",
                                  border_width=2
        ).grid(row=0, 
            column=0, 
            padx=0, 
            pady=0,
            sticky="nw"
        )

        sendButton = customtkinter.CTkButton(master=self.root,
                                  text="send",
                                  command=lambda: self.sendMessage(email, sendEntry.get()),
                                  text_color="white",
                                  corner_radius=5,
                                  width=50,
                                  height=50,
                                  fg_color="grey40",
                                  bg_color="grey50",
                                  text_font=("TkCaptionFont",20),
                                  border_color="grey30",
                                  border_width=2
        ).place(relx=0.885,
                rely=0.965, 
                anchor="w"
        )
        ######## Entries ########
        sendEntry = customtkinter.CTkEntry(master=self.root,
                               placeholder_text="Aa",
                               width=550,
                               height=50,
                               border_width=2,
                               corner_radius=0,
        )
        sendEntry.place(relx=0,
                rely=0.965, 
                anchor="w"
        )

        ######## Labels ########
        messages = self.showLastTenMessages(email)
        chatterLabel = customtkinter.CTkLabel(master=self.root,
                               text=email,
                               width=120,
                               height=25,
                               text_font=("TkTextFont",14),
                               justify=tkinter.LEFT,
                               text_color=("white", "gray20"),
                               bg_color="grey50",
        ).grid(row=0, 
            column=1, 
            columnspan=3,
            sticky="wnse", 
            padx=0,
        )

        i=0
        for message in messages:
            if message[1]==global_variables.MSG_RECVD:
                messageRecievedLabel = customtkinter.CTkLabel(master=self.root,
                               text=message[0],
                               width=120,
                               height=40,
                               text_font=("TkTextFont",14),
                               justify=tkinter.LEFT,
                               text_color=("white", "gray20"),
                               fg_color="grey50",
                               corner_radius=20
                )
                messageRecievedLabel.grid(row=i+2, 
                    column=0, 
                    columnspan=4,
                    sticky="wns", 
                    padx=30,
                    pady=10
                )
                i+=1
            elif message[1]==global_variables.MSG_SENT:
                messageSentLabel = customtkinter.CTkLabel(master=self.root,
                               text=message[0],
                               width=120,
                               height=40,
                               text_font=("TkTextFont",14),
                               justify=tkinter.LEFT,
                               text_color=("white", "gray20"),
                               fg_color="#0080FF",
                               corner_radius=20
                )
                messageSentLabel.grid(row=i+2, 
                    column=0, 
                    columnspan=4,
                    sticky="ens", 
                    padx=30,
                    pady=10
                )
                i+=1
            else:
                print("message status is not being properly attributed")
            
        


    def on_closing(self, event=0):
        self.root.destroy()

    def login(self, email, password):
        self.cont = Controller()
        self.cont.login(email, password)
        if(self.cont.loginServer.error == None):
            self.friendsList()

    def register(self, email, password):
        Controller.register(email, password)
    
    def addFriend(self, searchedEmail):
        self.cont.addFriend(searchedEmail)
        self.friendsList()
    
    def showFriends(self):
        return self.cont.showFriends()
    
    def showMessageHistory(self):
        return self.cont.showMessageHistory()

    def showLastTenMessages(self, email):
        return self.cont.showLastTenMessages(email)
    
    def sendMessage(self, friendEmail, message):
        self.cont.sendMessage(friendEmail, message)
        self.chat(friendEmail)

    def disconnect(self):
        self.cont.disconnect()
        self.mainPage()

    def __del__(self):
        self.cont.__del__()
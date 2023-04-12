import socket
import tkinter as tk 
from tkinter import messagebox
from tkinter import ttk 
import threading
from datetime import datetime

HOST = socket.gethostbyname(socket.gethostname())
PORT = 65432
HEADER = 64
FORMAT = "utf8"
DISCONNECT = "x"

LARGE_FONT = ("verdana", 13,"bold")

#option
SIGNUP = "signup"
LOGIN = "login"
LOGOUT = "logout"
SEARCH = "search"
LIST = "listall"
BOOK = "booking"

ADMIN_USERNAME = 'admin'
ADMIN_PSWD = 'admin'

#GUI intialize
class Hotel_App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.geometry("500x200")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.resizable(width=False, height=False)

        container = tk.Frame(self)
        container.pack(side="top", fill = "both", expand = True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, HomePage,BookingPage):
            frame = F(container, self)

            self.frames[F] = frame 

            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame(StartPage)
    
    def showFrame(self, container):
        frame = self.frames[container]
        if container==HomePage:
            self.geometry("700x500")
        elif container == BookingPage:
            self.geometry("450x500")
        else:
            self.geometry("500x500")
        frame.tkraise()

    # close-programe function
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()
            try:
                option = LOGOUT
                client.sendall(option.encode(FORMAT))
            except:
                pass

    def logIn(self,curFrame,sck):
        try:
            user = curFrame.entry_user.get()
            pswd = curFrame.entry_pswd.get()

            if user == "" or pswd == "":
                curFrame.label_notice = "Fields cannot be empty"
                return 
       
            #notice server for starting log in
            option = LOGIN
            sck.sendall(option.encode(FORMAT))

            #send username and password to server
            sck.sendall(user.encode(FORMAT))
            print("input:", user)

            sck.recv(1024)
            print("s responded")

            
            sck.sendall(pswd.encode(FORMAT))
            print("input:", pswd)


            # see if login is accepted
            accepted = sck.recv(1024).decode(FORMAT)
            print("accepted: "+ accepted)

            if accepted == "1":
                if user =="admin":
                    self.showFrame(AdminPage)
                else:
                    self.showFrame(HomePage)
                
                curFrame.label_notice["text"] = ""
            elif accepted == "2":
                curFrame.label_notice["text"] = "invalid username or password"
            elif  accepted == "0":
                curFrame.label_notice["text"] = "user already logged in"

        except:
            curFrame.label_notice["text"] = "Error: Server is not responding"
            print("Error: Server is not responding")

    def signUp(self,curFrame, sck):
        
        try:
        
            user = curFrame.entry_user.get()
            pswd = curFrame.entry_pswd.get()
            stk = curFrame.entry_stk.get()

            if pswd == "":
                curFrame.label_notice["text"] = "password cannot be empty"
                return
            
            

            #notice server for starting log in
            option = SIGNUP
            sck.sendall(option.encode(FORMAT))
            
            
            #send username and password to server
            sck.sendall(user.encode(FORMAT))
            print("input:", user)

            sck.recv(1024)
            print("s responded")

            sck.sendall(pswd.encode(FORMAT))
            print("input:", pswd)
            sck.sendall(stk.encode(FORMAT))
            print("input:", stk)


            # see if login is accepted
            accepted = sck.recv(1024).decode(FORMAT)
            print("accepted: "+ accepted)

            if accepted == "True":
                self.showFrame(HomePage)
                curFrame.label_notice["text"] = ""
            else:
                curFrame.label_notice["text"] = "username already exists"

        except:
            curFrame.label_notice["text"] = "Error 404: Server is not responding"
            print("404")

    def logout(self,curFrame, sck):
        try:
            option = LOGOUT
            sck.sendall(option.encode(FORMAT))
            accepted = sck.recv(1024).decode(FORMAT)
            if accepted == "True":
                self.showFrame(StartPage)
        except:
            curFrame.label_notice["text"] = "Error: Server is not responding"
    def Booking(self,curFrame,sck):
        self.showFrame(BookingPage)
    def Back(self,curFrame,sck):
        self.showFrame(HomePage)
    def BookRoom(self,curFrame, sck):
        try:
            id = curFrame.entry_id.get()
            name = curFrame.entry_name.get()
            hotel = curFrame.entry_hotel.get()
            request = curFrame.entry_request.get()
            datein = curFrame.entry_datein.get()
            dateout = curFrame.entry_dateout.get()

            if name == "":
                curFrame.label_notice["text"] = "name cannot be empty"
                return
            

            #notice server for starting log in
            option = BOOK
            sck.sendall(option.encode(FORMAT))
            
           
            sck.sendall(id.encode(FORMAT))
            print("input:", id)

            sck.recv(1024)
            print("s responded")

            sck.sendall(name.encode(FORMAT))
            print("input:", name)
            sck.sendall(hotel.encode(FORMAT))
            print("input:", hotel)
            sck.sendall(request.encode(FORMAT))
            print("input:", request)
            sck.sendall(datein.encode(FORMAT))
            print("input:", datein)
            sck.sendall(dateout.encode(FORMAT))
            print("input:", dateout)
            # see if login is accepted
            accepted = sck.recv(1024).decode(FORMAT)
            print("accepted: "+ accepted)

            if accepted == "True":
                curFrame.label_notice["text"] = "Booking thanh cong" 
            else:
                curFrame.label_notice["text"] = "Booking khong thanh cong"

        except:
            curFrame.label_notice["text"] = "Error 404: Server is not responding"
            print("404")
        
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="bisque2")

        label_title = tk.Label(self, text="LOG IN", font=LARGE_FONT,fg='#20639b',bg="bisque2")
        label_user = tk.Label(self, text="username ",fg='#20639b',bg="bisque2",font='verdana 10 ')
        label_pswd = tk.Label(self, text="password ",fg='#20639b',bg="bisque2",font='verdana 10 ')
        label_stk = tk.Label(self, text="bank number(use for signup) ",fg='#20639b',bg="bisque2",font='verdana 10 ')

        self.label_notice = tk.Label(self,text="",bg="bisque2")
        self.entry_user = tk.Entry(self,width=20,bg='white')
        self.entry_pswd = tk.Entry(self,width=20,bg='white')
        self.entry_stk = tk.Entry(self,width=20,bg='white')

        button_log = tk.Button(self,text="LOG IN", bg="#20639b",fg='floral white',command=lambda: controller.logIn(self, client)) 
        button_log.configure(width=10)
        button_sign = tk.Button(self,text="SIGN UP",bg="#20639b",fg='floral white', command=lambda: controller.signUp(self, client)) 
        button_sign.configure(width=10)
        
        label_title.pack()
        label_user.pack()
        self.entry_user.pack()
        label_pswd.pack()
        self.entry_pswd.pack()
        label_stk.pack()
        self.entry_stk.pack()
        self.label_notice.pack()

        button_log.pack()
        button_sign.pack()

class BookingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="bisque2")

        label_title = tk.Label(self, text="BOOKING PAGE", font=LARGE_FONT,fg='#20639b',bg="bisque2")
        label_title.pack()
        label_id = tk.Label(self, text="ID",fg='#20639b',bg="bisque2",font='verdana 10 ')
        label_request = tk.Label(self, text="so phong",fg='#20639b',bg="bisque2",font='verdana 10 ')
        label_name = tk.Label(self, text="Ten Khach Hang",fg='#20639b',bg="bisque2",font='verdana 10 ')
        label_hotel = tk.Label(self, text="Khach San",fg='#20639b',bg="bisque2",font='verdana 10 ')
        label_datein = tk.Label(self, text="Ngay Bat Dau",fg='#20639b',bg="bisque2",font='verdana 10 ')
        label_dateout = tk.Label(self, text="Ngay Roi Di",fg='#20639b',bg="bisque2",font='verdana 10 ')

        self.label_notice = tk.Label(self,text="",bg="bisque2")
        self.entry_id = tk.Entry(self,width=20,bg='white')
        self.entry_name = tk.Entry(self,width=20,bg='white')
        self.entry_request = tk.Entry(self,width=20,bg='white')
        self.entry_hotel = tk.Entry(self,width=20,bg='white')
        self.entry_datein = tk.Entry(self,width=20,bg='white')
        self.entry_dateout = tk.Entry(self,width=20,bg='white')
        label_id.pack()
        self.entry_id.pack()
        label_name.pack()
        self.entry_name.pack()
        label_request.pack()
        self.entry_request.pack()
        label_hotel.pack()
        self.entry_hotel.pack()
        label_datein.pack()
        self.entry_datein.pack()
        label_dateout.pack()
        self.entry_dateout.pack()
        self.label_notice.pack()
        button_back = tk.Button(self, text="Back",bg="#20639b",fg='#f5ea54', command=lambda: controller.Back(self,client))
        button_book = tk.Button(self, text="Booking", bg="#20639b",fg='#f5ea54',command=lambda: controller.BookRoom(self, client))
        button_book.configure(width=10)
        button_back.configure(width=10)
        button_book.pack() 
        button_back.pack()
    

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="bisque2")
        
        label_title = tk.Label(self, text="HOME PAGE", font=LARGE_FONT,fg='#20639b',bg="bisque2")
        button_back = tk.Button(self, text="Booking",bg="#20639b",fg='#f5ea54', command=lambda: controller.Booking(self,client))
        button_list = tk.Button(self, text="List all", bg="#20639b",fg='#f5ea54',command=self.listAll)

        self.entry_search = tk.Entry(self)

        label_title.pack(pady=10)

        button_list.configure(width=10)
        button_back.configure(width=10)

        self.entry_search.pack()

        self.label_notice = tk.Label(self, text="", bg="bisque2" )
        self.label_notice.pack(pady=4)

        button_list.pack(pady=2) 
        button_back.pack(pady=2)

        self.frame_detail = tk.Frame(self, bg="steelblue1")

        self.frame_list = tk.Frame(self, bg="tomato")
        
        self.tree = ttk.Treeview(self.frame_list)

        
        self.tree["column"] = ("ID", "Ten Phong", "Khach San", "Mo Ta", "Gia Phong")
        
        
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("ID", anchor='c', width=30)
        self.tree.column("Ten Phong", anchor='c', width=130)
        self.tree.column("Khach San", anchor='c', width=130)
        self.tree.column("Mo Ta", anchor='c', width=130)
        self.tree.column("Gia Phong", anchor='c', width=80)

        self.tree.heading("0", text="", anchor='c')
        self.tree.heading("ID", text="ID", anchor='c')
        self.tree.heading("Ten Phong", text="Ten Phong", anchor='c')
        self.tree.heading("Khach San", text="Khach San", anchor='c')
        self.tree.heading("Mo Ta", text="Mo Ta", anchor='c')
        self.tree.heading("Gia Phong", text="Gia Phong", anchor='c')
        
        self.tree.pack(pady=20)
        
   
    def recieveRooms(self):
        room = []
    
        rooms = []
        data = ''
        while True:
            data = client.recv(1024).decode(FORMAT)
            client.sendall(data.encode(FORMAT))
            if data == "end":
                break
            
            for i in range(8):
                data = client.recv(1024).decode(FORMAT)
                client.sendall(data.encode(FORMAT))
                room.append(data) 

            
            rooms.append(room)
            room = []

        return rooms

    def listAll(self):
        try:
            self.frame_detail.pack_forget()

            option = LIST
            client.sendall(option.encode(FORMAT))
            
            rooms = self.recieveRooms()
            
            x = self.tree.get_children()
            for item in x:
                self.tree.delete(item)

            i = 0
            for m in rooms:
                self.tree.insert(parent="", index="end", iid=i, 
                        values=( m[0], m[1], m[2], m[3], m[4]))
                
                i += 1

            self.frame_list.pack(pady=10)
        except:
            self.label_notice["text"] = "Error"
           

    

    def receiveDetails(self):
        option = "details"
        client.sendall(option.encode(FORMAT))

        row = []
        details = []
        data = ""

        while True:
            data = client.recv(1024).decode(FORMAT)
            if (data == "end"):
                break
            
            for i in range(5):
                data = client.recv(1024).decode(FORMAT)
                client.sendall(data.encode(FORMAT)) 
                row.append(data)

            details.append(row)
            row = []
        
        return details



#GLOBAL socket initialize
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)

client.connect(server_address)


app = Hotel_App()



#main
try:
    app.mainloop()
except:
    print("Error: server is not responding")
    client.close()

finally:
    client.close()

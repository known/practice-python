from tkinter import Tk, Menu
import tkinter.messagebox as MessageBox


def close_window(root):
    if MessageBox.askyesno("退出", "关闭程序？", icon="question"):
        root.destroy()

class MyWindow():
    def __init__(self):
        self.root = Tk()
        self.root.title("报文客户端")
        self.root.resizable(0, 0)
        self.center_window(500, 300)

        menu = MyMenu(self.root)
        self.root.config(menu=menu.menubar)

        self.root.protocol("WM_DELETE_WINDOW", lambda: close_window(self.root))
        self.root.mainloop()

    def center_window(self, width, height):
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        offsetleft = (screenwidth - width) / 2
        offsettop = (screenheight - height) / 2
        size = '%dx%d+%d+%d' % (width, height, offsetleft, offsettop)
        self.root.geometry(size)

class MyMenu():
    message_status = 1

    def __init__(self, root):
        self.menubar = Menu(root)
        self.optionmenu = Menu(self.menubar, tearoff=0)
        self.optionmenu.add_command(
            label="发送",
            command=lambda: self.send(root)
        )
        self.optionmenu.add_command(
            label="接收",
            command=lambda: self.receive(root)
        )
        self.optionmenu.add_separator()
        self.optionmenu.add_command(
            label="退出",
            command=lambda: close_window(root)
        )
        self.menubar.add_cascade(
            label="系统",
            menu=self.optionmenu
        )

        self.frmae = ""

    def send(self, root):
        MessageBox.showinfo("提示", "发送成功！")

    def receive(self, root):
        MessageBox.showinfo("提示", "接收成功！")

if __name__ == "__main__":
    my_win = MyWindow()

# package command: pyinstaller -F -w app.py
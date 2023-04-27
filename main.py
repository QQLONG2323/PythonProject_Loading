import tkinter as tk
from tkinter import ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x900")
        self.title("旅遊資訊整合小程式")

# 建立mainFrame
        mainFrame = ttk.Frame(self)
        mainFrame.pack(padx=30, pady=50,)

# 建立mainFrame的圖
        logoImage = Image.open('./plane.jpg')
        resizeImage = logoImage.resize((800, 150), Image.LANCZOS)
        self.logoTkimage = ImageTk.PhotoImage(resizeImage)
        logoLabel = ttk.Label(mainFrame, image=self.logoTkimage)
        logoLabel.pack(pady=(0, 50))


# 建立UpFrame
        UpFrame = ttk.LabelFrame(mainFrame, text="機場人數即時資訊", bootstyle="danger")
        UpFrame.pack(fill=tk.X)
        b1 = ttk.Button(UpFrame, text="查詢", bootstyle=SUCCESS)
        b1.pack(side=LEFT, padx=5, pady=10)
        b2 = ttk.Button(UpFrame, text="清除", bootstyle=(INFO, OUTLINE))
        b2.pack(side=LEFT, padx=5, pady=10)

# 設定欄位名稱
        columns = ('#1', '#2', '#3', '#4', '#5', '#6')
        self.tree_T = ttk.Treeview(UpFrame, columns=columns, show='headings')
        self.tree_T.heading('#1', text='時間區段')
        self.tree_T.column("#1", minwidth=0, width=100)
        self.tree_T.heading('#2', text='入境人數')
        self.tree_T.column("#2", minwidth=0, width=100)
        self.tree_T.heading('#3', text='出境人數')
        self.tree_T.column("#3", minwidth=0, width=100)
        self.tree_T.heading('#4', text='到站轉機')
        self.tree_T.column("#4", minwidth=0, width=100)
        self.tree_T.heading('#5', text='離站轉機')
        self.tree_T.column("#5", minwidth=0, width=100)
        self.tree_T.heading('#6', text='過境人數')
        self.tree_T.column("#6", minwidth=0, width=100)
        self.tree_T.pack(side=tk.LEFT, fill=tk.X)

# 建立topFrame
        top_Frame = ttk.LabelFrame(mainFrame, text="台灣銀行匯率查詢", bootstyle="info")
        top_Frame.pack(fill=tk.X)
        b1 = ttk.Button(top_Frame, text="查詢", bootstyle=SUCCESS, command=pass)
        b1.pack(side=LEFT, padx=5, pady=10)
        b2 = ttk.Button(top_Frame, text="清除", bootstyle=(INFO, OUTLINE), command=pass)
        b2.pack(side=LEFT, padx=5, pady=10)
# 設定欄位名稱
        columns = ('#1', '#2', '#3')
        self.tree_C = ttk.Treeview(top_Frame, columns=columns, show='headings')
        self.tree_C.heading('#1', text='幣別')
        self.tree_C.column("#1", minwidth=0, width=150)
        self.tree_C.heading('#2', text='現金匯率本行買入')
        self.tree_C.column("#2", minwidth=0, width=240)
        self.tree_C.heading('#3', text='現金匯率本行賣出')
        self.tree_C.column("#3", minwidth=0, width=240)
        self.tree_C.pack(side=tk.LEFT, fill=tk.X)


# 建立bottomFrame
        bottomFrame = ttk.LabelFrame(mainFrame, text="今天航班資訊", bootstyle="primary")
        bottomFrame.pack(fill=tk.X)
        b1 = ttk.Button(bottomFrame, text="查詢", bootstyle=SUCCESS)
        b1.pack(side=LEFT, padx=5, pady=10)
        b2 = ttk.Button(bottomFrame, text="清除", bootstyle=(INFO, OUTLINE))
        b2.pack(side=LEFT, padx=5, pady=10)
# 建立Treeview
        columns = ('#1', '#2', '#3', '#4', '#5', '#6')
        self.tree_A = ttk.Treeview(bottomFrame, columns=columns, show='headings')
        self.tree_A.heading('#1', text='出發地')
        self.tree_A.column("#1", minwidth=0, width=50)
        self.tree_A.heading('#2', text='時間')
        self.tree_A.column("#2", minwidth=0, width=50)
        self.tree_A.heading('#3', text='班機資訊')
        self.tree_A.column("#3", minwidth=0, width=150)
        self.tree_A.heading('#4', text='航廈')
        self.tree_A.column("#4", minwidth=0, width=50)
        self.tree_A.heading('#5', text='登機門')
        self.tree_A.column("#5", minwidth=0, width=100)
        self.tree_A.heading('#6', text='狀態')
        self.tree_A.column("#6", minwidth=0, width=150)
        self.tree_A.pack(side=tk.LEFT, fill=tk.X)
        
def main():
    window = Window()
    window.mainloop()


if __name__ == "__main__":
    main()
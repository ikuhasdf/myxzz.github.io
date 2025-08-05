import tkinter as tk
from tkinter import messagebox, filedialog
import time
import random

class Minesweeper:
    def __init__(self, master, rows=10, cols=10, mines=10):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.game_over = False
        self.board = [[0] * cols for _ in range(rows)]
        self.buttons = [[None] * cols for _ in range(rows)]
        self.create_board()
        self.place_mines()
        self.calculate_mine_counts()
        self.create_buttons()

    def create_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.board[i][j] = 0

    def place_mines(self):
        mine_count = 0
        while mine_count < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if self.board[row][col] != -1:
                self.board[row][col] = -1
                mine_count += 1

    def calculate_mine_counts(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != -1:
                    count = 0
                    for x in range(max(0, i - 1), min(i + 2, self.rows)):
                        for y in range(max(0, j - 1), min(j + 2, self.cols)):
                            if self.board[x][y] == -1:
                                count += 1
                    self.board[i][j] = count

    def create_buttons(self):
        for i in range(self.rows):
            for j in range(self.cols):
                btn = tk.Button(self.master, text="", width=3, height=1)
                btn.grid(row=i, column=j)
                btn.bind("<Button-1>", lambda e, row=i, col=j: self.click(row, col))
                btn.bind("<Button-3>", lambda e, row=i, col=j: self.right_click(row, col))
                self.buttons[i][j] = btn

    def click(self, row, col):
        if self.game_over:
            return
        if self.board[row][col] == -1:
            self.game_over = True
            self.reveal_all_mines()
            messagebox.showinfo("游戏结束", "你踩到地雷了！")
            self.master.destroy()
        else:
            self.reveal_cell(row, col)
            if self.check_win():
                messagebox.showinfo("游戏胜利", "恭喜你，扫雷成功！")

    def right_click(self, row, col):
        if self.game_over:
            return
        btn = self.buttons[row][col]
        if btn["text"] == "":
            btn.config(text="🚩")
        elif btn["text"] == "🚩":
            btn.config(text="")

    def reveal_cell(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.buttons[row][col]["text"] != "":
            return
        self.buttons[row][col]["text"] = str(self.board[row][col])
        self.buttons[row][col].config(state=tk.DISABLED)
        if self.board[row][col] == 0:
            for x in range(max(0, row - 1), min(row + 2, self.rows)):
                for y in range(max(0, col - 1), min(col + 2, self.cols)):
                    self.reveal_cell(x, y)

    def reveal_all_mines(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == -1:
                    self.buttons[i][j]["text"] = "💣"
                    self.buttons[i][j].config(state=tk.DISABLED)

    def check_win(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != -1 and self.buttons[i][j]["text"] == "":
                    return False
        return True

class Windows95Simulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Windows 95 Simulator")
        self.root.geometry("800x600")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg="teal")

        # 创建桌面
        self.create_desktop()

        # 创建任务栏
        self.create_taskbar()

        # 更新时钟
        self.update_clock()

    def create_desktop(self):
        self.desktop_frame = tk.Frame(self.root, bg="teal")
        self.desktop_frame.pack(fill=tk.BOTH, expand=True)

        # 我的电脑图标
        self.my_computer_icon = self.create_icon(self.desktop_frame, "我的电脑", self.open_my_computer)

        # 回收站图标
        self.recycle_bin_icon = self.create_icon(self.desktop_frame, "回收站", self.open_recycle_bin)

    def create_icon(self, parent, text, command):
        icon = tk.Label(parent, text=text, bg="teal", fg="white")
        icon.pack(side=tk.TOP, padx=10, pady=10)
        icon.bind("<Button-1>", command)
        return icon

    def create_taskbar(self):
        # 任务栏
        self.taskbar = tk.Frame(self.root, bg="gray", height=30)
        self.taskbar.pack(side=tk.BOTTOM, fill=tk.X)

        # 开始按钮
        self.start_button = tk.Button(self.taskbar, text="开始", bg="gray", fg="white", command=self.open_start_menu)
        self.start_button.pack(side=tk.LEFT, padx=5)

        # 时钟
        self.clock = tk.Label(self.taskbar, text="12:00 PM", bg="gray", fg="white")
        self.clock.pack(side=tk.RIGHT, padx=5)

    def update_clock(self):
        current_time = time.strftime("%I:%M %p")
        self.clock.config(text=current_time)
        self.root.after(1000, self.update_clock)  # 每秒更新一次

    def open_my_computer(self, event):
        my_computer = tk.Toplevel()
        C_GB = 100
        my_computer.title("我的电脑")
        my_computer.geometry("300x200")
        my_computer.config(bg="white")
        C = tk.Label(my_computer, text=f"C盘空间{C_GB}GB，已用{400}MB").pack()

    def open_recycle_bin(self, event):
        my_DEL = tk.Toplevel()
        my_DEL.title("回收站")
        my_DEL.geometry("300x200")
        my_DEL.config(bg="white")
        C = tk.Label(my_DEL, text="无文件").pack()

    def open_start_menu(self):
        start_menu = tk.Menu(self.root, tearoff=0)
        start_menu.add_command(label="程序", command=self.open_programs)
        start_menu.add_command(label="文档", command=self.open_documents)
        start_menu.add_command(label="控制面板", command=self.open_settings)
        start_menu.add_command(label="关机", command=self.shutdown)
        start_menu.post(self.start_button.winfo_rootx(), self.start_button.winfo_rooty() - start_menu.winfo_reqheight())

    def open_programs(self):
        start_menu1 = tk.Menu(self.root, tearoff=1)
        start_menu1.add_command(label="扫雷", command=self.open_Minesweeper)
        start_menu1.add_command(label="记事本", command=self.open_notepad)
        start_menu1.post(self.start_button.winfo_rootx(), self.start_button.winfo_rooty() - start_menu1.winfo_reqheight())

    def open_Minesweeper(self):
        game_window = tk.Toplevel(self.root)
        game_window.title("扫雷")
        game_window.resizable(False, False)
        game = Minesweeper(game_window)

    def open_notepad(self):
        txt_window = tk.Toplevel(self.root)
        txt_window.title("记事本")

        # 创建文本编辑区域
        txt = tk.Text(txt_window)
        txt.pack(fill=tk.BOTH, expand=True)

        # 创建菜单栏
        menubar = tk.Menu(txt_window)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="保存", command=lambda: self.save_file(txt))
        menubar.add_cascade(label="文件", menu=file_menu)
        txt_window.config(menu=menubar)

    def save_file(self, text_widget):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text_widget.get("1.0", tk.END))
            messagebox.showinfo("保存成功", "文件已保存！")
    def save_file1(self, text_widget):
        file_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Microsoft Word Files", "*.docx"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text_widget.get("1.0", tk.END))
            messagebox.showinfo("保存成功", "文件已保存！")
    def open_documents(self):
        start_menu2 = tk.Menu(self.root, tearoff=1)
        start_menu2.add_command(label="Word", command=self.open_word)
        start_menu2.add_command(label="Excel", command=self.open_excel)
        start_menu2.add_command(label="PowerPoint", command=self.open_powerpoint)
        start_menu2.post(self.start_button.winfo_rootx(), self.start_button.winfo_rooty() - start_menu2.winfo_reqheight())

    def open_word(self):
        word_window = tk.Toplevel(self.root)
        word_window.title("Word")
        word_window.geometry("400x300")
        label = tk.Label(word_window, text="Word 文档").pack()

        menubar = tk.Menu(word_window)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="保存", command=self.save_file1)
        menubar.add_cascade(label="文件", menu=file_menu)
        word_window.config(menu=menubar)

    def open_excel(self):
        excel_window = tk.Toplevel(self.root)
        excel_window.title("Excel")
        excel_window.geometry("400x300")
        label = tk.Label(excel_window, text="Excel 表格").pack()

    def open_powerpoint(self):
        powerpoint_window = tk.Toplevel(self.root)
        powerpoint_window.title("PowerPoint")
        powerpoint_window.geometry("400x300")
        label = tk.Label(powerpoint_window, text="PowerPoint 演示文稿").pack()

    def open_settings(self):
        s = tk.Toplevel()
        s.title("控制面板")
        s.geometry("800x600")
        label = tk.Label(s, text="此功能尚未实现").pack()

    def shutdown(self):
        if messagebox.askyesno("关机", "确定要关机吗？"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Windows95Simulator(root)
    root.mainloop()
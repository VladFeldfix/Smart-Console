import tkinter as tk
from tkinter import ttk
from datetime import datetime
import os 
import subprocess
import platform

# region OBJ COLOR PACK
class color_pack:
    def __init__(self, color):
        color = color.upper()
        colors = {}
        colors["RED"] = "#ba4b43"
        colors["YELLOW"] = "#bab643"
        colors["GREEN"] = "#34ad6f"
        colors["BLUE"] = "#43a4ba"
        colors["PURPLE"] = "#8543ba"
        colors["PINK"] = "#b443ba"
        colors["BROWN"] = "#ba7d43"
        colors["GREY"] = "#8f8f8f"
        if color in colors:
            self.COLOR_MAIN = colors[color]
        else:
            self.COLOR_MAIN = color
        self.COLOR_BACKGROUND = self.adjust_brightness(self.COLOR_MAIN, 0.3)
        self.COLOR_MSG_USER = self.invert_hex(self.COLOR_MAIN)
        self.COLOR_MSG_APP = self.adjust_brightness(self.COLOR_MAIN, 1.2)
        self.COLOR_OUTER_MENU = self.adjust_brightness(self.COLOR_MAIN, 5.0)
    
    def adjust_brightness(self, hex_color, factor):
        """
        Adjust brightness of a hex color.
        :param hex_color: str, color in hex format (e.g. "#33cc99")
        :param factor: float, >1.0 to lighten, <1.0 to darken
        :return: str, adjusted hex color
        """
        # Remove '#' if present
        hex_color = hex_color.lstrip('#')
        
        # Convert to RGB
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        
        # Apply factor and clamp values between 0–255
        r = max(0, min(255, int(r * factor)))
        g = max(0, min(255, int(g * factor)))
        b = max(0, min(255, int(b * factor)))
        
        # Return new hex color
        return f"#{r:02x}{g:02x}{b:02x}"

    def invert_hex(self, hex_color):
        """
        Invert a HEX color.
        Example: #123456 -> #edcba9
        """
        # Remove "#" if present
        hex_color = hex_color.lstrip('#')

        # Parse to integer
        value = int(hex_color, 16)

        # Invert and ensure 6 hex digits
        inverted = 0xFFFFFF - value

        return f"#{inverted:06x}"
# endregion
# region OBJ CHAT BUBBLE
class ChatBubble(tk.Frame):
    """A single chat bubble widget."""
    def __init__(self, master, message, color_pack, sender="User"):
        super().__init__(master, bg=master["bg"])

        # Style colors
        if sender == "User":
            bg_color = color_pack.COLOR_MSG_USER   # WhatsApp green bubble
            timestamp_color = color_pack.COLOR_MSG_APP
            anchor = "e"
            padx = (50, 10)
        else:
            bg_color = color_pack.COLOR_MSG_APP  # WhatsApp gray bubble
            timestamp_color = color_pack.COLOR_MSG_USER
            anchor = "w"
            padx = (10, 50)

        # Force all bubbles to same width
        self.columnconfigure(0, weight=1)
        bubble = tk.Frame(self, bg=bg_color, bd=1, relief="solid")
        bubble.grid(sticky="we", padx=padx, pady=5)  # grid allows width control

        # Message label
        msg_label = tk.Label(
            bubble,
            text=message,
            font=("Arial", 12),
            bg=bg_color,
            wraplength=280,  # consistent wrap width
            justify="left",  # controls multiline alignment
            anchor="w"       # anchors the text to the left side
        )
        msg_label.pack(padx=10, pady=(5, 0), fill=tk.X)

        # Timestamp
        time_str = datetime.now().strftime("%H:%M")
        time_label = tk.Label(
            bubble,
            text=time_str,
            font=("Arial", 8),
            bg=bg_color,
            fg=timestamp_color
        )
        time_label.pack(anchor="e", padx=8, pady=(0, 3))
# endregion
# region OBJ DATABASE
class Database:
    def __init__(self, name: str, path: str, headers: tuple):
        self.data = {}
        self.path = path
        self.full_path = self.path+"/"+name+".csv"
        self.headers = headers
        self.name = name
        self.error = None
        self.create()
    
    def create(self):
        if not os.path.isfile(self.full_path):
            header = ""
            for column in self.headers:
                header += column+","
            header = header[:-1]
            try:
                file = open(self.full_path, 'w')
                file.write(header+"\n")
                file.close()
            except Exception as e:
                self.error = str(e)
    
    def load_data(self):
        if not os.path.isfile(self.full_path):
            self.create()
        
        file = open(self.full_path, 'r')
        headers = file.readline()
        lines = file.readlines()
        file.close()

        for line in lines:
            line = line.replace("\n", "")
            line = line.split(",")
            self.data[line[0]] = line[1:]
    
    def insert(self, data):
        self.data[data[0]] = data[1:]
    
    def delete(self, key):
        if key in self.data:
            del self.data[key]

    def commit(self):
        file = open(self.full_path, 'w')
        txt = ""
        for col in self.headers:
            txt += col+","
        txt = txt[:-1]
        file.write(txt+"\n")
        for pk, vals in self.data.items():
            txt = ""
            for val in vals:
                txt += val+","
            txt = txt[:-1]
            file.write(pk+","+txt+"\n")
        file.close()
# endregion
# region OBJ SC
class SmartConsole:
    def __init__(self, application_name, application_rev, info, color):
        # theme color
        self.color_pack = color_pack(color)

        # vars
        self.main_menu_items = {}
        self.application_name = application_name
        self.application_rev = str(application_rev)
        self.info = info
        self.settings = {}
        self.databases = {}
        self.log = []
        self.log_headers = []
        self.allow_empty_message = False

        # gui
        self.root = tk.Tk()
        self.root.title(self.application_name+" v"+self.application_rev)
        self.root.geometry("400x600")
        self.root.configure(bg=self.color_pack.COLOR_OUTER_MENU)
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.__exit)
        self.root.iconbitmap("favicon.ico")
        self.byebye = False

        # Top bar (like WhatsApp header)
        header = tk.Frame(self.root, bg=self.color_pack.COLOR_MAIN, height=50)
        header.pack(fill=tk.X)

        tk.Label(
            header,
            text=self.application_name+" v"+self.application_rev,
            bg=self.color_pack.COLOR_MAIN,
            fg="white",
            font=("Arial", 14, "bold")
        ).pack(side=tk.LEFT, padx=15, pady=10)

        # Chat area
        self.chat_frame = tk.Frame(self.root, bg=self.color_pack.COLOR_BACKGROUND)
        self.chat_frame.pack(fill=tk.BOTH, expand=True)
        
        # Progress Bar
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure(
            "Custom.Horizontal.TProgressbar",
            troughcolor=self.color_pack.COLOR_BACKGROUND,   # background track color
            background=self.color_pack.COLOR_MAIN  # progress bar color
        )
        self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", mode="determinate", style="Custom.Horizontal.TProgressbar",)
        self.progress_bar.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
        
        # Scrollbar
        self.canvas = tk.Canvas(self.chat_frame, bg=self.color_pack.COLOR_BACKGROUND, highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.chat_frame, command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg=self.color_pack.COLOR_BACKGROUND)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw", width=self.canvas.winfo_reqwidth())
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Keep bubbles full width on resize
        self.canvas.bind("<Configure>", self.__update_frame_width)

        # Input bar
        self.input_frame = tk.Frame(self.root, bg=self.color_pack.COLOR_OUTER_MENU, height=50)
        self.input_frame.pack(fill=tk.X, side=tk.BOTTOM)

        self.entry = tk.Entry(
            self.input_frame,
            font=("Arial", 12),
            relief="flat",
            bg=self.color_pack.COLOR_OUTER_MENU,
            disabledbackground=self.color_pack.COLOR_OUTER_MENU
        )
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 5), pady=10)
        self.entry.focus()
        self.entry.config(state="disabled")

        self.send_btn = tk.Button(
            self.input_frame,
            text="Send",
            font=("Arial", 11, "bold"),
            bg=self.color_pack.COLOR_MAIN,
            fg="white",
            relief="flat",
        )
        self.send_btn.pack(side=tk.RIGHT, padx=(5, 10), pady=10)
        self.send_btn.config(state="disabled")

    def __update_frame_width(self, event):
        """Ensure the scrollable frame always matches the canvas width."""
        canvas_width = event.width
        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.scrollable_frame,
            anchor="nw",
            width=self.canvas.winfo_reqwidth()
        )
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)

    def __add_message(self, message, sender="User"):
        bubble = ChatBubble(self.scrollable_frame, message, self.color_pack, sender)
        bubble.pack(fill=tk.X, anchor="e" if sender == "User" else "w")
        self.root.update_idletasks()
        self.canvas.yview_moveto(1.0)

    def __send_message(self, event=None):
        msg = self.entry.get().strip()
        if not msg:
            return
        self.__add_message(msg, sender="User")
        self.entry.delete(0, tk.END)
    
    def __edit_settings(self):
        for key, val in self.settings.items():
            if self.question("The current value of "+key+" is: "+val+"\nWould you like to change it?"):
                new_val = self.input("Insert new value for: "+key)
                self.settings[key] = new_val
                self.print("The new value of "+key+" is: "+new_val)
        self.__save_settings()
        self.restart()

    def __save_settings(self):
        file = open("settings.txt", 'w')
        for key, val in self.settings.items():
            file.write(key+" > "+val+"\n")
        file.close()

    def __load_settings(self):
        file = open("settings.txt", 'a')
        file.close()     
        file = open("settings.txt", 'r')
        lines = file.readlines()
        file.close()
        for line in lines:
            if ">" in line:
                line = line.split(">")
                key = line[0].strip()
                val = line[1].strip()
                if key in self.settings:
                    self.settings[key] = val
        
        self.__save_settings()

    def __help(self):
        os.popen("help.pdf")
        self.restart()
    
    def __version_history(self):
        os.popen("Software version history.pdf")
        self.restart()

    def __exit(self):
        self.entry.delete(0, tk.END)
        self.entry.config(state='disabled')
        self.send_btn.config(state='disabled')
        txt = "Good Bye"
        if not self.byebye:
            self.byebye = True
            self.print(txt)
        def close_program():
            os._exit(0)
            self.root.destroy()
        self.root.after(2000, close_program)
    
    def __is_leap_year(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def __is_valid_date(self, day, month, year):
        if year < 1 or month < 1 or month > 12 or day < 1:
            return False

        # Days in each month
        month_days = [31, 29 if self.__is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        return day <= month_days[month - 1]

    # endregion
    # region SETUP
    def add_main_menu_item(self, function_name:str, function):
        self.main_menu_items[function_name] = function

    def add_settings_key(self, key:str):
        self.settings[key] = "None"

    def display_main_menu(self):
        self.__load_settings()
        txt = ""
        txt += self.application_name+" v"+self.application_rev+"\n"
        txt += self.info+"\n"
        if len(self.settings) > 0:
            self.main_menu_items["SETTINGS"] = self.__edit_settings
            txt += "\nSettings:\n"
            for key, val in self.settings.items():
                txt += " * "+key+" > "+val+"\n"
        
        self.main_menu_items["HELP"] = self.__help
        self.main_menu_items["VERSION HISTORY"] = self.__version_history
        self.main_menu_items["EXIT"] = self.__exit
        txt += "\nMain Menu:\n"
        i = 0
        options = {}
        for key, val in self.main_menu_items.items():
            i += 1
            options[str(i)] = val
            txt += "("+str(i)+") "+key+"\n"
            
        txt += "\nSelect your action"
        ans = self.input(txt)

        while not ans in options:
            ans = self.input("Invalid choice")
        options[ans]()

    def launch(self):
        self.root.mainloop()
    
    def restart(self):
        self.allow_empty_message = True
        self.input("Done! Press Send to continue...")
        self.display_main_menu()
    # endregion
    # region MESSAGES
    def print(self, txt: str):
        self.__add_message(txt, sender="sc")

    def input(self, prompt: str) -> str:
        """
        Simulate a blocking input() in Tkinter.
        Shows a prompt in the chat and waits for user to enter text.
        Returns the entered text.
        """
        # Show the prompt in the chat
        self.__add_message(prompt, sender="Computer")
        self.entry.config(state="normal")
        self.send_btn.config(state="normal")

        # Create a StringVar to hold the user's input
        user_input = tk.StringVar()

        # Define a handler that sets the variable when user presses Enter
        def on_enter(event=None):
            value = self.entry.get().strip()
            send = False
            if value:  # only accept non-empty input
                send = True
            if self.allow_empty_message:
                send = True
                self.allow_empty_message = False
            if send:
                user_input.set(value)
                self.__send_message(value)
                self.entry.delete(0, tk.END)
                self.entry.config(state="disabled")
                self.send_btn.config(state="disabled")

        # Bind Enter key temporarily
        self.entry.bind("<Return>", on_enter)
        self.send_btn.configure(command=on_enter)

        # Wait for the variable to be set
        self.root.wait_variable(user_input)

        # Unbind Enter key to restore normal behavior
        self.entry.unbind("<Return>")

        return user_input.get()
    
    def question(self, prompt: str):
        ans = self.choose(prompt, ("YES","NO"))
        return ans == "YES"

    def choose(self, prompt:str, options:tuple):
        # setup text
        i = 0
        txt = prompt+"\n"
        available_options = []
        for option in options:
            i += 1
            txt += "("+str(i)+") "+option+"\n"
            available_options.append(str(i))
        txt = txt[:-1]

        # get input
        choice = self.input(txt)
        while not choice in available_options:
            choice = self.input("Invalid choice")
        
        # return selected option
        return options[int(choice)-1]

    def input_date(self, txt: str):
        ans = self.input(txt)
        ok = False
        while not ok:
            if "-" in ans:
                original_date = ans
                ans = ans.split("-")
                if len(ans) == 3:
                    year = ans[0]
                    month = ans[1]
                    day = ans[2]
                    try:
                        year = int(year)
                        month = int(month)
                        day = int(day)
                        if self.__is_valid_date(day, month, year):
                            ok = True
                    except:
                        pass
            if not ok:
                ans = self.input("Invalid date format")
        return original_date

    # endregion
    # region SETTINGS
    def get_settings_value(self, key: str):
        return self.settings[key]
    # endregion
    # region LOADING BAR
    def set_loading_bar(self, percent: int):
        self.progress_bar['value'] = percent
    # endregion
    # region SCRIPT
    def run_script(self, path: str, functions: dict):
        # open file
        if not os.path.isfile(path):
            self.print("File not found: "+path)
            return False
        file = open(path, 'r')
        lines = file.readlines()
        file.close()

        # read script
        ln = 0
        for line in lines:
            ln += 1
            if "(" in line:
                line = line.replace("\n", "")
                line = line.replace(")", "")
                line = line.split("(")
                command = line[0].strip()
                if not command in functions:
                    self.print("Error in script: "+path+"\nUnknown command: "+command+"\nIn line: "+str(ln))
                    return False
                arguments = []
                for argument in line[1].strip().split(","):
                    arguments.append(argument.strip())
                if len(arguments) == 1 and arguments[0] == "":
                    arguments = []
                if len(arguments) != len(functions[command][1]):
                    self.print("Error in script: "+path+"\nInvalid number of arguments for command: "+command+"\nIn line: "+str(ln)+"\nExpected number of arguments: "+str(len(functions[command][1]))+"\n"+str(functions[command][1])+"\nGiven number of arguments: "+str(len(arguments))+"\n"+str(arguments))
                    return False
                if len(arguments) > 0:
                    functions[command][0](arguments)
                else:
                    functions[command][0]()

        # all good
        return True
    # endregion
    # region DATABASE
    def database_connect(self, name: str, path: str, headers: tuple):
        database = Database(name, path, headers)
        if not database.error:
            self.databases[name] = database
        else:
            self.print(database.error)
    
    def database_insert(self, name: str, data: tuple):
        self.databases[name].insert(data)
    
    def database_commit(self, name: str):
        self.databases[name].commit()

    def database_delete(self, name: str, key: str):
        self.databases[name].delete(key)
    
    def database_data(self, name: str):
        return self.databases[name].data.items()

    def database_headers(self, name: str):
        return self.databases[name].headers
    # endregion
    # region TIME
    def today(self) -> str:
        """Returns the current date in YYYY-MM-DD format."""
        return datetime.now().strftime("%Y-%m-%d")
    
    def now(self) -> str:
        """Returns the current time in HH:MM:SS format."""
        return datetime.now().strftime("%H:%M:%S")

    def current_year(self) -> str:
        """Returns the current year in YYYY format."""
        return datetime.now().strftime("%Y")

    def current_month(self) -> str:
        """Returns the current month in MM format."""
        return datetime.now().strftime("%m")

    def current_day(self) -> str:
        """Returns the current day in DD format."""
        return datetime.now().strftime("%d")

    def current_hour(self) -> str:
        """Returns the current hour in HH format."""
        return datetime.now().strftime("%H")

    def current_minute(self) -> str:
        """Returns the current minute in MM format."""
        return datetime.now().strftime("%M")

    def current_second(self) -> str:
        """Returns the current second in SS format."""
        return datetime.now().strftime("%S")

    def compare_dates(self, date1: str, date2: str) -> int:
        """
        Returns the number of days between date1 and date2.
        Dates must be in 'YYYY-MM-DD' format.
        """
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        return (d2 - d1).days
    # endregion
    # region LOG
    def write_to_log(self, txt: str):
        self.log.append(txt)
    
    def add_log_header(self, header: str):
        self.log_headers.append(header)
    
    def display_log(self):
        file = open("Log.html", 'w')
        file.write('<!DOCTYPE html>\n')
        file.write('<html lang="en">\n')
        file.write('<head>\n')
        file.write('    <meta charset="UTF-8">\n')
        file.write('    <title>Log</title>\n')
        file.write('    <style>\n')
        file.write('        body {\n')
        file.write('            font-family: "Courier New", "Courier", "monospace";\n')
        file.write('        }\n')
        file.write('    </style>\n')
        file.write('</head>\n')
        file.write('<body>\n')
        file.write('    <h1>'+self.application_name+' v'+self.application_rev+'</h1>\n')
        file.write('    <b><text>Date: '+self.today()+' '+self.now()+'</text><br>\n')
        if len(self.log_headers) > 0:
            for header in self.log_headers:
                file.write('    <text>'+header+'</text><br>\n')
        if len(self.settings) > 0:
            file.write('    <text>Settings:</text><br>\n')
            file.write('    <ul>\n')
            for key, val in self.settings.items():
                file.write('        <li>'+key+' > '+val+'</li>\n')
            file.write('    </ul></b>\n')
            file.write('    <hr>\n')
        i = 0
        for line in self.log:
            i += 1
            file.write('    <text>['+str(i)+'] '+line+'</text><br>\n')
        file.write('</body>\n')
        file.write('</html>\n')
        file.close()
        os.popen("Log.html")
    # endregion
    # region FILES
    def test_paths(self, paths: tuple):
        for path in paths:
            if not os.path.isfile(path) and not os.path.isdir(path):
                self.print("Error! Path not found: "+path)
                return False
        return True

    def open(self, path: str):
        """
        Attempts to open the specified file or folder in the system's file explorer.
        Returns True if successful, False otherwise.
        """
        try:
            if platform.system() == "Windows":
                os.startfile(path)
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", path])
            else:  # Linux and other Unix-like systems
                subprocess.run(["xdg-open", path])
            return True
        except Exception as e:
            self.print(str(e))
            return False
    # endregion
# endregion
# Download SmartConsole.py from: https://github.com/VladFeldfix/Smart-Console/blob/main/SmartConsole.py
from SmartConsole import *
import os

class ExampleProgram:
    # constructor
    def __init__(self):
        # load smart console
        self.sc = SmartConsole("Example Program", "1.0")

        # set-up main memu
        self.sc.add_main_menu_item("INSERT TEXT", self.insert_text)
        self.sc.add_main_menu_item("ASK ME", self.ask_me)
        self.sc.add_main_menu_item("CREATE A FATAL ERROR", self.fatal)
        self.sc.add_main_menu_item("RUN SCRIPT",self.run)
        self.sc.add_main_menu_item("EDIT SCRIPT",self.edit)
        self.sc.add_main_menu_item("READ CSV FILE", self.open_csv)
        self.sc.add_main_menu_item("READ DATABASE", self.opeb_db)
        self.sc.add_main_menu_item("SHOW CURRENT TIME", self.timestampt)
        
        # get settings
        self.path_script = self.sc.get_setting("Script location")
        self.path_output = self.sc.get_setting("Output location")

        # test all paths
        self.sc.test_path(self.path_script)
        self.sc.test_path(self.path_output)

        # display main menu
        self.sc.start()
    
    def insert_text(self):
        text = self.sc.input("Type your input text here")
        self.sc.print("Your text is: "+text)
        self.sc.good("That's how you make it green OK: "+text)
        self.sc.warning("That's how you make it yellow WARNING: "+text)
        self.sc.error("That's how you make it red ERROR: "+text)
        self.sc.restart()
    
    def ask_me(self):
        ans = self.sc.question("Is everything okay?")
        if ans:
            self.sc.print("Im glad everything is ok")
        else:
            ch = self.sc.choose("Whats wrong?",["I'm sad", "I'm sick"])
            if ch == "I'm sad":
                self.sc.good("Here is a green message to cheer you up")
            else:
                self.sc.print("I'm sorry to hear that, feel better")
                self.sc.good("Here is a green message to make you healthy")
        self.sc.hr()
        self.sc.restart()
    
    def fatal(self):
        self.sc.fatal_error("This is a fatal error!")

    def open_csv(self):
        path = self.sc.input("Insert path to csv")
        self.sc.test_path(path)
        csv = self.sc.load_csv(path)
        print(csv)
        self.sc.save_csv(self.path_output, csv)
        self.sc.restart()
    
    def opeb_db(self):
        path = self.sc.input("Insert path to csv")
        self.sc.test_path(path)
        db = self.sc.load_database(path, ["First Name", "Last Name", "Score"])
        print(db)
        givendict = {"key1": "val1","key2": "val2"}
        db = self.sc.invert_database(givendict)
        print(db)
        self.sc.save_database(self.path_output, db)
        self.sc.open_folder(self.path_output)
        self.sc.restart()

    def run(self):
        script_loc = self.sc.get_setting("Script location")+"/script.txt"
        self.sc.test_path(script_loc)
        functions = {}
        functions["START"] = (self.start, ("Argument0", "Argument1", "Argument3"))
        functions["SHOWDATE"] = (self.show_date, ())
        self.sc.run_script(script_loc, functions)
        self.sc.restart()
    
    def edit(self):
        script_loc = self.sc.get_setting("Script location")+"/script.txt"
        self.sc.test_path(script_loc)
        os.popen(script_loc)
        self.sc.restart()
    
    def timestampt(self):
        self.sc.print("today: "+self.sc.today())
        self.sc.print("current_year: "+self.sc.current_year())
        self.sc.print("current_month: "+self.sc.current_month())
        self.sc.print("current_day: "+self.sc.current_day())
        self.sc.print("current_week: "+self.sc.current_week())
        self.sc.print("current_weekday: "+self.sc.current_weekday())
        self.sc.print("now: "+self.sc.now())
        self.sc.print("right_now: "+self.sc.right_now())
        self.sc.print("current_hour: "+self.sc.current_hour())
        self.sc.print("current_minute: "+self.sc.current_minute())
        self.sc.print("current_second: "+self.sc.current_second())
        self.sc.print("current_millisecond: "+self.sc.current_millisecond())
        self.sc.print("current_time: "+self.sc.current_time())
        self.sc.restart()
    
    # SCRIPT FUNCTIONS
    def start(self, arguments):
        for arg in arguments:
            self.sc.print(arg)
    
    def show_date(self, arguments):
        todays_date = self.sc.today()
        self.sc.print(todays_date)

        givenDate = self.sc.input("Insert a date YYYY-MM-DD")
        res = self.sc.test_date(givenDate)
        if res:
            self.sc.good("that is a good date")
        
        fromto = self.sc.compare_dates(todays_date, givenDate)
        tofrom = self.sc.compare_dates(givenDate, todays_date)
        self.sc.print("This is how many days have passed from "+todays_date+" to "+givenDate+": "+str(fromto))
        self.sc.print("This is how many days have passed from "+givenDate+" to "+todays_date+": "+str(tofrom))

ExampleProgram()
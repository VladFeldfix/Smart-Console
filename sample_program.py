from SmartConsole import SmartConsole
import threading
import time

class SampleProgram:
    def __init__(self):
        info = "This is a sample app to demonstrate the capabilities of the smart console tool"
        self.sc = SmartConsole("Sample App", 1.0, info, "BLUE")
        self.sc.add_main_menu_item("LOAD", self.progressbar)
        self.sc.add_main_menu_item("FILE", self.file)
        self.sc.add_main_menu_item("LOG", self.log)
        self.sc.add_main_menu_item("TIME", self.time)
        self.sc.add_main_menu_item("DATABASE", self.database)
        self.sc.add_main_menu_item("START", self.start)
        self.sc.add_settings_key("Key1")
        self.sc.add_settings_key("Key2")
        self.sc.display_main_menu()
        self.sc.launch()
    
    def progressbar(self):
        self.sc.set_loading_bar(0)
        def run():
            self.sc.set_loading_bar(0)
            for i in range(101):
                time.sleep(0.05)  # Simulate loading
                self.sc.set_loading_bar(i)
            self.sc.input("ok")
            self.sc.restart()

        threading.Thread(target=run).start()

    def file(self):
        self.sc.open("Y:/Rafael/Cables/Vlad Fedlfix/Tools/New SC/help.pdf")
        self.sc.restart()

    def log(self):
        self.sc.add_log_header("total number of lines: 100")
        for i in range(100):
            self.sc.write_to_log("random text #"+str(i))
        self.sc.display_log()

    def time(self):
        self.sc.print(self.sc.today())
        self.sc.print(self.sc.now())
        self.sc.print(self.sc.current_day())
        self.sc.print(self.sc.current_month())
        self.sc.print(self.sc.current_year())
        self.sc.print(self.sc.current_hour())
        self.sc.print(self.sc.current_minute())
        self.sc.print(self.sc.current_second())
        self.sc.print(int(self.sc.compare_dates(self.sc.today(),"2025-10-21")))
    
    def database(self):
        self.sc.database_connect("test","Y:/Rafael/Cables/Vlad Fedlfix/Tools/New SC",("vlad","hello","world"))
        self.sc.database_insert("test",("40","20","30"))
        self.sc.database_insert("test",("14","20","30"))
        self.sc.database_delete("test",("54m185"))
        self.sc.database_commit("test")
        for key, val in self.sc.database_data("test"):
            txt = key+" "+str(val)
            self.sc.print(txt)
        
        for h in self.sc.database_headers("test"):
            self.sc.print(h)

    def start(self):
        # call script
        commands = {}
        commands["TEST"] = (self.test, ("arg1", "arg2"))
        commands["TEST1"] = (self.test1, ("arg1", "arg2"))
        commands["TEST2"] = (self.test2, ())
        self.sc.run_script("script.txt", commands)
        
        # restart
        self.sc.restart()
    
    def test(self, args):
        self.sc.print(args)
    
    def test1(self, args):
        for a in args:
            self.sc.print(a)
    
    def test2(self):
        self.sc.print("ok")

SampleProgram()

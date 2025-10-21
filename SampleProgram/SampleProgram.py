from SmartConsole import SmartConsole

class SampleProgram:
    def __init__(self):
        info = "This is a sample app to demonstrate the capabilities of the smart console tool"
        color = "BLUE"
        self.sc = SmartConsole("Sample App", 1.0, info, color)
        self.sc.add_main_menu_item("START", self.start)
        self.sc.add_settings_key("Key1")
        self.sc.add_settings_key("Key2")
        self.sc.display_main_menu()
        self.sc.launch()


    def start(self):
        # print/input
        self.sc.print("Hello world")
        ans = self.sc.input("Send me a message")
        if "Hello" in ans:
            self.sc.input("Hi there!")
        
        # compare dates
        txt = "Comparing dates:\n"
        before = self.sc.compare_dates("2025-10-21", "2025-10-22")
        after = self.sc.compare_dates("2025-10-21", "2025-10-20")
        exactly = self.sc.compare_dates("2025-10-21", "2025-10-21")
        txt += "When DATE 1 is BEFORE DATE 2 the return value is "+str(before)
        txt += "When DATE 1 is AFTER DATE 2 the return value is "+str(after)
        txt += "When DATE 1 is THE SAME AS DATE 2 the return value is "+str(exactly)
        self.sc.print(txt)
        self.sc.restart()

SampleProgram()
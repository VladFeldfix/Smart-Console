from SmartConsole import SmartConsole

class SampleProgram:
    def __init__(self):
        info = "This is a sample app to demonstrate the capabilities of the smart console tool"
        color = "BLUE"
        self.sc = SmartConsole("Sample App", 1.0, info, color, "640x480")
        self.sc.add_main_menu_item("INPUT OUTPUT", self.io)
        self.sc.add_main_menu_item("COMPARE DATES", self.compare_dates)
        self.sc.add_settings_key("Key1")
        self.sc.add_settings_key("Key2")
        self.sc.display_main_menu()
        self.sc.launch()


    def io(self):
        # print/input
        self.sc.print("Hello world!")
        ans = self.sc.input("Send me a message")
        if "hello" in ans.lower():
            self.sc.input("Hi there!")
    
    def compare_dates(self):
        # compare dates
        date1 = self.sc.input_date("Insert date 1 in format YYYY-MM-DD")
        date2 = self.sc.input_date("Insert date 2 in format YYYY-MM-DD")
        result = self.sc.compare_dates(date1, date2)
        if result > 0:
            self.sc.print(date1+" is "+str(result)+" days before "+date2)
        elif result < 0:
            self.sc.print(date1+" is "+str(result)+" days after "+date2)
        else:
            self.sc.print(date1+" is the same as"+date2)
        self.sc.restart()

SampleProgram()
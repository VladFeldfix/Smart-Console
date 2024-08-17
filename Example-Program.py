# Download SmartConsole.py from: https://github.com/VladFeldfix/Smart-Console/blob/main/SmartConsole.py
from SmartConsole import *

class ExampleProgram:
    # constructor
    def __init__(self):
        # load smart console
        self.sc = SmartConsole("Example Program", "1.0")

        # set-up main memu
        self.sc.add_main_menu_item("RUN", self.run)
        self.sc.add_main_menu_item("EDIT SCRIPT", self.edit)

        # get settings
        self.path_script = self.sc.get_setting("Script location")
        self.path_output = self.sc.get_setting("Output location")

        # test all paths
        self.sc.test_path(self.path_script)
        self.sc.test_path(self.path_output)

        # load databases
        self.load_database()

        # display main menu
        self.sc.start()
    
    def run(self):
        try:
            print(colored("text",'white','on_red'))
            self.sc.fatal_error("text")
            print(colored("text",'white','on_red'))
        except Exception as e:
            print(e)

    def edit(self):
        pass
    
    def load_database(self):
        pass


ExampleProgram()
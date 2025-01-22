<h1>Smart-Console</h1>
<h2>INSTALLATION</h2>
<p>Download Smart-Console.py and put it to your Python folder</p>
<p>Typically something like: C:\Python310\Lib\SmartConsole.py</p>
<h2>CONSTRUCTOR</h2>
<b>__init__(name, version)</b>
<ol>
  <li>name - The name of the application</li>
  <li>version - The version of the application</li>
</ol>
<h2>FLOW</h2>
<b>start()</b>
<ol>
  <li>Start the application displaying the application header, version, and main menu</li>
</ol>
<b>restart()</b>
<ol>
  <li>Restarts the application</li>
</ol>
<b>exit()</b>
<ol>
  <li>Exits the application</li>
</ol>
<h2>MAIN MENU</h2>
<b>add_main_menu_item(name, function)</b>
<ol>
  <li>name - The name of the function for example: "RUN"</li>
  <li>function - The function to call when this menu item is selected. For example: self.run</li>
</ol>
<h2>INPUT</h2>
<b>input(text)</b>
<ol>
  <li>text - The prompt of the input</li>
  <li>RETURN VALUE: The inserted text</li>
</ol>
<b>question(text)</b>
<ol>
  <li>text - The prompt of the question</li>
  <li>RETURN VALUE: True or False</li>
</ol>
<b>choose(text, options)</b>
<ol>
  <li>text - The prompt of the displayed menu</li>
  <li>options - A list of possible options</li>
  <li>RETURN VALUE: The text of the selected option</li>
</ol>
<h2>OUTPUT</h2>
<b>print(text)</b>
<ol>
  <li>text - The text to display</li>
</ol>
<b>good(text)</b>
<ol>
  <li>text - The text of the good message to display</li>
</ol>
<b>warning(text)</b>
<ol>
  <li>text - The text of the warning message to display</li>
</ol>
<b>error(text)</b>
<ol>
  <li>text - The text of the error to display</li>
</ol>
<b>fatal_error(text)</b>
<ol>
  <li>text - The text of the fatal error to display before exiting the application</li>
</ol>
<b>hr()</b>
<ol>
  <li>Draws a horizontal line</li>
</ol>
<h2>SETTINGS</h2>
<b>open_settings()</b>
<ol>
  <li>Opens "settings.txt" to edit</li>
</ol>
<b>get_setting(var)</b>
<ol>
  <li>var - the name of the setting</li>
  <li>RETURN VALUE: The value of the given setting</li>
</ol>
<h2>HELP</h2>
<b>help()</b>
<ol>
  <li>Displays the help file "help.pdf"</li>
</ol>
<h2>FILE HANDLER</h2>
<b>test_path(path)</b>
<ol>
  <li>path - Throws a fatal error if the given path is missing</li>
</ol>
<b>open_folder(path)</b>
<ol>
  <li>path - Open a given folder with Windows File Explorer</li>
</ol>
<b>load_csv(path)</b>
<ol>
  <li>path - The location of the .csv file</li>
  <li>RETURN VALUE: the content of the given .csv file as a list</li>
</ol>
<b>save_csv(path, data)</b>
<ol>
  <li>path - The location of the .csv file to save</li>
  <li>data - a list to be saved as a .csv file</li>
</ol>
<h2>SCRIPT</h2>
<b>run_script(path, functions)</b>
<ol>
  <li>path - The location of the script file to read</li>
  <li>functions - a directory of functions to activate. For example:<br>{"START": (self.start, ("Argument0", "Argument1", "Argument3") ) }</li>
</ol>
<h2>DATABASES</h2>
<b>save_database(path, data)</b>
<ol>
  <li>path - The location of the file to save</li>
  <li>data - a directory</li>
</ol>
<b>load_database(path, headers)</b>
<ol>
  <li>path - The location of the file to load</li>
  <li>headers - the headers of the directory</li>
</ol>
<b>invert_database(database)</b>
<ol>
  <li>database - a directory to invert</li>
  <li>RETURN VALUE: the inverted version of the given directory</li>
</ol>
<h2>DATE</h2>
<b>today()</b>
<ol>
  <li>Returns today's date</li>
  <li>RETURN VALUE: current date in format: YYYY-MM-DD</li>
</ol>
<b>current_year()</b>
<ol>
  <li>RETURN VALUE: current year in format: YYYY</li>
</ol>
<b>current_month()</b>
<ol>
  <li>RETURN VALUE: current month in format: MM</li>
</ol>
<b>current_day()</b>
<ol>
  <li>RETURN VALUE: current day in format: DD</li>
</ol>
<b>current_week()</b>
<ol>
  <li>RETURN VALUE: current week number in format: WW</li>
</ol>
<b>current_weekday()</b>
<ol>
  <li>RETURN VALUE: current weekday number: 1-Sunday, 2-Monday, 3-Tuesday, 4-Wednesday, 5-Thursday, 6-Friday, 7-Saturday, in format: 0</li>
</ol>
<b>now()</b>
<ol>
  <li>RETURN VALUE: current time in format: HH:MM</li>
</ol>
<b>right_now()</b>
<ol>
  <li>RETURN VALUE: current time in format: HH:MM:SS</li>
</ol>
<b>current_hour()</b>
<ol>
  <li>RETURN VALUE: current hour number in format: HH</li>
</ol>
<b>current_minute()</b>
<ol>
  <li>RETURN VALUE: current minute number in format: MM</li>
</ol>
<b>current_second()</b>
<ol>
  <li>RETURN VALUE: current second number in format: SS</li>
</ol>
<b>current_millisecond()</b>
<ol>
  <li>RETURN VALUE: current millisecond number in format: MS</li>
</ol>
<b>current_time()</b>
<ol>
  <li>RETURN VALUE: current time in format: HH:MM:SS:MS</li>
</ol>
<b>test_date(givenDate)</b>
<ol>
  <li>givenDate - a text in the format YYYY-MM-DD</li>
  <li>RETURN VALUE: True or False that the given text is in the following date format: YYYY-MM-DD</li>
</ol>
<b>compare_dates(firstDate, secondDate)</b>
<ol>
  <li>firstDate - a text in the format YYYY-MM-DD</li>
  <li>secondDate - a text in the format YYYY-MM-DD</li>
  <li>RETURN VALUE: The number of days between firstDate to secondDate</li>
</ol>

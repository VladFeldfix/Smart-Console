<h1>Smart-Console</h1>
<h2>CONSTRUCTOR</h2>
<b>__init__(name, version)</b>
<ol>
  <li>name - The name of the application</li>
  <li>version - The version of the application</li>
</ol>
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
<b>add_main_menu_item(name, function)</b>
<ol>
  <li>name - The name of the function for example: "RUN"</li>
  <li>function - The function to call when this menu item is selected. For example: self.run</li>
</ol>
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
  <li>RETURN VALUE: The number of the selected option</li>
</ol>
<b>print(text)</b>
<ol>
  <li>text - The text to display</li>
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
<b>open_settings()</b>
<ol>
  <li>Opens "settings.txt" to edit</li>
</ol>
<b>get_setting(var)</b>
<ol>
  <li>var - the name of the setting</li>
  <li>RETURN VALUE: The value of the given setting</li>
</ol>
<b>help()</b>
<ol>
  <li>Displays the help file "help.pdf"</li>
</ol>
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

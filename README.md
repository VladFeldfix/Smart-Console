<h1>Smart-Console</h1>
<b>__init__(self, name, version)</b>
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
<b>add_main_menu_item(self, name, function)</b>
<ol>
  <li>name - The name of the function for example: "RUN"</li>
  <li>function - The function to call when this menu item is selected. For example: self.run</li>
</ol>
<b>input(self, text)</b>
<ol>
  <li>text - The prompt of the input</li>
  <li>RETURN VALUE: The inserted text</li>
</ol>
<b>question(self, text)</b>
<ol>
  <li>text - The prompt of the question</li>
  <li>RETURN VALUE: True or False</li>
</ol>
<b>choose(self, text, options)</b>
<ol>
  <li>text - The prompt of the displayed menu</li>
  <li>options - A list of possible options</li>
  <li>RETURN VALUE: The number of the selected option</li>
</ol>
<b>print(self, text)</b>
<ol>
  <li>text - The text to display</li>
</ol>

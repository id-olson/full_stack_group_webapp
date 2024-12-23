# Using .editorconfig

The `.editorconfig` file in the root directory ensures we all have the same styling settings applied for all .js and .py files.

### What the file does

This file is used to set 2 space indentation for all javascript files and 4 space indentation for all python files.

### Setting it up in your IDE

No plugin installation is needed for many common IDEs, including IntelliJ and VSCode. For a full list of supported IDEs, see: https://editorconfig.org/.

- For .js files: VSCode requires downloading the `EditorConfig for VS Code` extension in order for the .editorconfig file to be applied whenever formatting with `Alt+Shift+f`.
- For .py files: .editorconfig doesn't interface with the python formatter, but it will correctly dictate how many spaces are used when pressing the `Tab` key.

### Verifying proper setup

Open our project directory in an IDE. Verify that the properties defined in .editorconfig are enforced when formatting .js files. For example, change `indent_style = 2` to `indent_style = 6`, reformat a .js file, and see if the change is reflected.

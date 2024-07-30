# CSV to JSON Converter in Python
### Overview
*This project is a CSV to JSON converter built using Python, designed to provide a user-friendly graphical interface (GUI) for seamless data conversion. The converter takes CSV (Comma-Separated Values) files and transforms them into JSON (JavaScript Object Notation) format, which is widely used for data interchange in web applications.*

### Features
* User-Friendly GUI: The application features an intuitive graphical user interface that simplifies the conversion process for users of all skill levels.
* Flexible Input: Users can select any CSV file from their filesystem, making it easy to convert data from various sources.
* Error Handling: The converter includes robust error handling to manage common issues that may arise during file conversion, such as improperly formatted CSV files.
* Output Options: The converted JSON data can be saved to a specified location, allowing users to manage their files effectively.

### Usage
1. Launch the Application: Run the GUI application by executing the following command in your terminal:

*python "Convert CSV - Python.py"*

2. Select CSV File: Use the file dialog to choose the CSV file you wish to convert.
3. Convert and Save: Click the convert button to process the file. The application will generate a JSON file and prompt you to save it to your desired location.

### Example
Given a CSV file with the following content:
----------------
name,age
Alice,30
Bob,25
---------------

The output JSON will be:

[
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]

### Support
*For any issues or feature requests, please open an issue in the GitHub repository. Contributions are welcome!*

### Demo Video

https://github.com/user-attachments/assets/8630c2bb-0864-4ce9-b8ea-f5d83c25b516

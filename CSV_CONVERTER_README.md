# CSV to Excel Converter

This project provides a simple and efficient solution to convert all CSV files in a specified folder to Excel files. This implementation was developed based on a Notion ticket requirement.

## Features

- 🔍 **Automatic Discovery**: Automatically finds all CSV files in the specified folder
- 🚁 **Error Handling**: Handles corrupted or invalid CSV files gracefully
- 📐 #�Creates Output Folder**: Automatically creates the output folder if it doesn't exist
- 📉 **Progress Tracking**: Provides real-time feedback and a comprehensive summary report
- 🙌 **Preserves Data**: Maintains all data integrity during conversion

## Requirements

```text
pip install pandas openpyxl
```

Or install from the provided requirements.txt:

```text
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
python csv_to_excel_converter.py
```

This will:
- Look for CSV files in the `documents/` folder
- Create Excel files in the `excel_output/` folder

### Custom Folders

You can also use the function directly with custom folders:

```python
from csv_to_excel_converter import convert_csv_to_excel

# Use custom folders
convert_csv_to_excel(input_folder='my_csv_files', output_folder='my_excel_files')
```

## Example Output

```
查 Found 1 CSV files to convert...
┅ Converted: sample_data.csv → sample_data.xlsx

📊 CONVERSION SUMMARY:
┅ Successfully converted: 1 files
┌ Failed: 0 files
```

## File Structure

```
mcp-test/
├── csv_to_excel_converter.py  # Main converter script
├── requirements.txt            # Python dependencies
├── documents/                  # Input folder for CSV files
│   └── sample_data.csv          # Sample CSV file
└── excel_output/               # Output folder for Excel files (created automatically)
      └── sample_data.xlsx      # Converted Excel file
```

## Function Documentation

### `convert_csv_to_excel(documents_folder='documents', output_folder='excel_output')`

**Parameters:**
- `documents_folder` (str, optional): Path to the folder containing CSV files. Defaults to 'documents'.
- `output_folder` (str, optional): Path to the folder where Excel files will be saved. Defaults to 'excel_output'.

**Returns:**
- `tuple`: A tuple containing two lists:
  - `converted_files`: List of successfully converted files
  - `failed_files`: List of tuples containing (filename, error_message)

## Error Handling

The script includes robust error handling:

1. **File Not Found**: If the specified input folder doesn't exist or contains no CSV files
2. **Corrupted CSV**: If a CSV file is corrupted or cannot be parsed
3. **Permission Errors**: If there are permission issues with reading or writing files
4. **Memory Issues**: If a CSV file is too large to fit in memory

## Troubleshooting

### Common Issues

1. **`ModuleNotFoundError: No module named 'pandas'`**
   - Solution: `pip install pandas openpyxl`

2. **`FileNotFoundError: [Errno 2] No such file or directory`**
   - Solution: Ensure the `documents/` folder exists and contains CSV files

3. **`PermissionError: [Errno 13] Permission denied`**
   - Solution: Check file permissions and ensure you have write access to the output folder

## Supported Formats

- **Input**: All standard CSV formats (comma-separated, semicolon-separated, etc.)
- **Output**: Excel .xlsx format (OpenXML)

## License

MIT License - feel free to use, modify, and distribute.

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

## Original Requirement

This implementation was developed based on the following Notion ticket requirement:

> Ticket: we currently have a file called documents that has a lot of .csv file.
> We need to have a function that can parse each of these file to convert them in excel files.

This solution fulfills all the requirements and provides additional features for reliability and ease of use.

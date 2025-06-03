import pandas as pd
import os
from pathlib import Path

def convert_csv_to_excel(documents_folder='documents', output_folder='excel_output'):
    """
    Convert all CSV files in a folder to Excel files
    """
    # Create output folder if it doesn't exist
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    
    # Get all CSV files in the documents folder
    csv_files = [f for f in os.listdir(documents_folder) if f.endswith('.csv')]
    
    if not csv_files:
        print(f"No CSV files found in {documents_folder}")
        return
    
    print(f"Found {len(csv_files)} CSV files to convert...")
    
    converted_files = []
    failed_files = []
    
    for csv_file in csv_files:
        try:
            # Read CSV file
            csv_path = os.path.join(documents_folder, csv_file)
            df = pd.read_csv(csv_path)
            
            # Create Excel filename
            excel_filename = csv_file.replace('.csv', '.xlsx')
            excel_path = os.path.join(output_folder, excel_filename)
            
            # Convert to Excel
            df.to_excel(excel_path, index=False)
            
            converted_files.append(csv_file)
            print(f"✅ Converted: {csv_file} → {excel_filename}")
            
        except Exception as e:
            failed_files.append((csv_file, str(e)))
            print(f"❌ Failed to convert {csv_file}: {e}")
    
    # Summary
    print(f"\n📊 COL�EQSISION SUMMARY:")
    print(f"✅ Successfully converted: {len(converted_files)} files")
    print(f"❌ Failed: {len(failed_files)} files")
    
    return converted_files, failed_files

# Usage
if __name__ == "__main__":
    convert_csv_to_excel('documents', 'excel_output')

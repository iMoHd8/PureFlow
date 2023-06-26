# PureFlow - README

This tool is designed to clean datasets by removing null values, special characters, links, hashtags, and mentions from specific columns. It also performs various text cleaning operations to preprocess the data.

## Usage:
1. Prepare your dataset in a supported format (CSV, Excel, etc.).
2. Place the dataset file in the same directory as this cleaning tool.
3. Open a command prompt or terminal.
4. Navigate to the directory containing the cleaning tool and dataset file.
5. Install the cleaning tool using the this commands:
   pip install PureFlow
6. Import The PureFlow Package and start using It:
   import PureFlow as pf
   pf.clean_dataset()
   pf.remove_nulls()

## Parameters:
- `columns_name`: Provide the names of the columns to clean. Use ['all'] to clean all columns or ['column1', 'column2'] to clean specific columns.
- `remove_nan` (Optional): Specify if null values should be removed. Default is False.
- `save_it_as_csv` (Optional): Specify if the cleaned dataset should be saved as a new CSV file. Default is True.

## Output:
- The cleaned dataset will be displayed on the console.
- If `save_it_as_csv` is True, the cleaned dataset will be saved as "Cleaned_Dataset.csv" in the same directory.

## Note:
- Make sure you have Python and the necessary dependencies (Pandas) installed.
- Ensure that your dataset file is not open or locked by any other program during the cleaning process.

## Example Usage:
pip install PureFlow
import PureFlow as pf
pf.clean_dataset('dataset name', ['columns name'])
Cleaning in progress...
Cleaned dataset:
    ...
    [Display a sample of cleaned data here]
    ...
Cleaning completed successfully. The cleaned dataset has been saved as "Cleaned_Dataset.csv".

For any issues or inquiries, please contact me:

E-Mail: iMoHd8@hotmail.com
LinkedIn: https://www.linkedin.com/in/mohammed-mahameed
GitHub: https://github.com/iMoHd8
Instagram: https://www.instagram.com/i.mohd.8/

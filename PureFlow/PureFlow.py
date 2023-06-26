import pandas as pd
import re



def remove_nulls(dataset, columns_names):
     """
     This Function Takes a dataset and the names of the columns that you want to remove the null values from it.
     and it returns the dataset after removing the null values

     Parameters
     ----------
     `dataset`: An Excel dataset can be in CSV, Excel, or any other Excel format
     `columns_names`: The names of the columns that you want to remove the null values from it like ['text'].
                    if you want to remove The null values from ALL columns, then just pass ['all'].

     Outputs
     ----------
     `dataset`: the same dataset but without the null values.

     Examples
     ----------
          >>> print(dataset)
                    text        label       
          0      hey         NaN
          1      NaN        positive
          2      hate       negative

          Drop the null values in 'text' column only.

          >>> remove_nans(dataset, ['text'])
                    text        label       
          0      hey         NaN
          2      hate       negative

          Drop the null values in 'label' column only.

          >>> remove_nans(dataset, ['label'])
                    text        label
          1      NaN        positive
          2      hate       negative

          Drop the null values in all columns.

          >>> remove_nans(dataset, ['all'])
                    text        label       
          2      hate       negative
     """

     #Assign The Dataset To Valriable after convert it into Data Frame.
     dataset = pd.DataFrame(data=dataset, columns=dataset.columns)

     #Check the Columns From Which Null Values Should be Removed
     match columns_names:
          case ["all"]:
               dataset = dataset.dropna(how='any')
          case _:
               for column in columns_names:
                    dataset = dataset.dropna(subset=[column])

     return dataset


def clean_dataset(dataset, columns_name, remove_null = False, save_it_as_csv = True):
     """
     This Function Takes a dataset and the names of the column that you want to Clean.
     it returns Cleaned Dataset and Will Saved it in New Excel File

     Parameters
     ----------
     `dataset`: An Excel dataset can be in CSV, Excel, or any other Excel format
     `columns_name`: The names of the columns that you want to remove the null values from it like ['text'].
                    if you want to remove The null values from ALL columns, then just pass ['all'].
     `remove_nan` (Optional): Boolean Parameter to Check If You Want to Remove the Null Values with The Cleaning Process.
                              The Default is False
                              'True': Will Remove The Null Values.
                              'False': Will Not Remove The Null Values.

     `save_it_as_csv` (Optional): Boolean Parameter to Check If You Want to Save The Cleaning Process
                                  in New File as CSV after Cleaning or Not.
                                  The Default is True
                                  'True': Will Save the Changes in New CSV File.
                                  'False': Will Not Save the Changes in New CSV File.

     Outputs
     ----------
     `dataset`: Cleaned Dataset

     """

     #Assign The Dataset To Valriable after convert it into Data Frame.
     dataset = pd.DataFrame(data=dataset, columns=dataset.columns)
     
     #True If You Want to Remove the Null Values with The Cleaning Process. The Default is False (Optional Parameter)
     if remove_null == True:
          dataset = remove_nulls(dataset, [columns_name])

     #The regular expressions used for cleaning
     re_processed_feature_1 = re.compile('https?\S+')
     re_processed_feature_2 = re.compile(r"#\S*")
     re_processed_feature_3 = re.compile(r"@\S*\s")
     re_processed_feature_4 = re.compile(r"[?]*\s")
     re_processed_feature_5 = re.compile(r"[\W\d\_]+")
     re_processed_feature_6 = re.compile(r'\s+[a-zA-Z]\s+')
     re_processed_feature_7 = re.compile(r'\^[a-zA-Z]\s+')
     re_processed_feature_8 = re.compile(r'^\s+')
     re_processed_feature_9 = re.compile(r'\s+')
     re_processed_feature_10 = re.compile(r"\W")
     re_processed_feature_11 = re.compile(r'[^\x00-\x7F]+')

     #Remove the extra characters and information by iterating row by row.
     for row in range(0, len(dataset)):
          #Remove links
          processed_feature = re_processed_feature_1.sub('', dataset[columns_name].iloc[row])

          #Remove Hashtags
          processed_feature = re_processed_feature_2.sub(' ', processed_feature)

          #Remove Mentions
          processed_feature = re_processed_feature_3.sub(' ', processed_feature)

          #Remove a ? sign
          processed_feature = re_processed_feature_4.sub(' ', processed_feature)

          #Remove any non-word character, digit, or underscore
          processed_feature = re_processed_feature_5.sub(' ', processed_feature)

          #Remove a Single Character 
          processed_feature = re_processed_feature_6.sub(' ', processed_feature)

          #Remove a Single Character if it The First Character in The Line
          processed_feature = re_processed_feature_7.sub(' ', processed_feature)

          #Remove a spaces if it The First Character in The Line
          processed_feature = re_processed_feature_8.sub('', processed_feature)

          #Remove More One Space
          processed_feature = re_processed_feature_9.sub(' ', processed_feature)

          #Keep Only Words
          processed_feature = re_processed_feature_10.sub(' ', processed_feature)

          #remove special characters
          processed_feature = re_processed_feature_11.sub('', processed_feature)


          #Changing The Original Row to Cleaned Row
          dataset[columns_name].iloc[row] = processed_feature

     #Remove The Null Values After Cleaning the Dataset
     dataset = remove_nulls(dataset, [columns_name])

     #Showing The First 5 Columns
     print(dataset.head())

     if save_it_as_csv is True:
          #Save The Changes in New File as CSV
          dataset.to_csv("Cleaned_Dataset.csv")


     return dataset
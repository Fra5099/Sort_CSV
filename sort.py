import pandas as pd
import textwrap
import csv

def filter_csv():
    # read the CSV file
    df = pd.read_csv('instances.csv', encoding='utf-8-sig')
    # select columns to keep
    df = df.sort_values(by=["document_title"], ascending=False)
    keep_cols = ["fragment","document_title","document_url"]

    # keep only specific columns
    df = df.loc[:, keep_cols]
    # write the result to a new CSV file
    df.to_csv('output_file.csv', index=False, encoding='utf-8-sig')
    

def textBB(row):
    title = row[0]
    description = row[1]
    link = row[2]

    # Wrap the text to a specific width
    wrapped_description = textwrap.fill(description, width=40)

    # Add a border around the wrapped text
    bordered_text = f'+{"-"*40}+\n|{title.center(40)}|\n+{"-"*40}+\n\n{wrapped_description}\n\n{"-"*40}\n|{"Link:".ljust(11)}{link.ljust(27)}|\n+{"-"*40}+'

    # Print the bordered text
    print(bordered_text)
    

def read_csv():
    with open('output_file.csv', encoding="utf-8-sig") as csv_file:
        # Create a CSV reader object
        reader = csv.reader(csv_file)
        
        # Skip the header row

        # Loop over each row in the CSV file
        for row in reader:
            # Print the values in each row
            textBB(row)

def main():
    filter_csv()
    read_csv()

main()

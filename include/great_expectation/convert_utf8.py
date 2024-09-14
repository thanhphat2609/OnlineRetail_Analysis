import csv

def convert_csv_iso8859_1_to_utf8(input_file, output_file):
    with open(input_file, 'r', encoding='iso-8859-1') as infile:
        reader = csv.reader(infile)
        
        # Open the output file with UTF-8 encoding
        with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
            writer = csv.writer(outfile)
            
            # Write each row from the input file to the output file
            for row in reader:
                writer.writerow(row)

# Example usage
input_file = '../dataset/Online_Retail.csv'
output_file = '../dataset/online_retail.csv'
convert_csv_iso8859_1_to_utf8(input_file, output_file)
print(f"CSV file converted from ISO-8859-1 to UTF-8 and saved as {output_file}")

import csv
from io import StringIO

# The CSV data as a string (you could also read this from a file)
csv_data = """Name,COMPANY
A Anoop,HDFC Bank Limited
A Brindha Devi,HDFC Bank Limited
A C Leo Arokiaraja,HDFC Bank Limited
A C Patil,HDFC Bank Limited
A Chinnadurai,HDFC Bank Limited
A Dhanapal,HDFC Bank Limited
A Durgaprasad Rao,HDFC Bank Limited
A Gayathri,HDFC Bank Limited
A Gopinath,HDFC Bank Limited
A Ignatius,HDFC Bank Limited
A K Gupta,Axis Bank Limited
A K Malik,HDFC Bank Limited
A Kalyana Raman,HDFC Bank Limited
A Kalyanaraman,HDFC Bank Limited
A Kannan,HDFC Bank Limited
A Krishnan,HDFC Bank Limited
A Manoj Stephen,HDFC Bank Limited
A Mukundan,HDFC Bank Limited
A N S Srinivaas,HDFC Bank Limited
"""

# Use StringIO to simulate a file object for the csv.reader
csv_file = StringIO(csv_data)

# Read the CSV data
reader = csv.DictReader(csv_file)

# Process each row
for row in reader:
    print(f"Name: {row['Name']}, Company: {row['COMPANY']}")

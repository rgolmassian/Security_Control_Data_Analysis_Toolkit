import csv
import xml.etree.ElementTree as ET

def convert_file():
    # Load the XML file (Most recent XML file can be obtained from https://public.cyber.mil/stigs/cci/)
    tree = ET.parse('U_CCI_List.xml')
    root = tree.getroot()

    # Open a CSV file for writing
    with open('U_CCI_List.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(['id', 'status', 'publishdate', 'contributor', 'definition', 'type', 'reference_creator', 'reference_title', 'reference_version', 'reference_location', 'reference_index'])

        # Write each <cci_item> element as a row in the CSV file
        for event, cci_item in ET.iterparse('U_CCI_List.xml'):
            if cci_item.tag == '{http://iase.disa.mil/cci}cci_item':
                id = cci_item.get('id')
                status = cci_item.find('{http://iase.disa.mil/cci}status').text
                publishdate = cci_item.find('{http://iase.disa.mil/cci}publishdate').text
                contributor = cci_item.find('{http://iase.disa.mil/cci}contributor').text
                definition = cci_item.find('{http://iase.disa.mil/cci}definition').text
                type = cci_item.find('{http://iase.disa.mil/cci}type').text

                # Extract reference data from each <reference> element and write to CSV file
                references = cci_item.findall('{http://iase.disa.mil/cci}references/{http://iase.disa.mil/cci}reference')
                for i, reference in enumerate(references):
                    reference_creator = reference.get('creator')
                    reference_title = reference.get('title')
                    reference_version = reference.get('version')
                    reference_location = reference.get('location')
                    reference_index = reference.get('index')

                    # Write row to CSV file
                    writer.writerow([id, status, publishdate, contributor, definition, type, reference_creator, reference_title, reference_version, reference_location, reference_index])

                # Clear the element from memory to save space
                cci_item.clear()

# Execute the function
convert_file()
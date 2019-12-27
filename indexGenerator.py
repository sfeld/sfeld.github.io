import csv

def generate_table_row(row):
    """
    Input: ['Tamarine', 'Palo Alto', '$$$', 'Dinner']

    Output:
    <tr>
    <td>Tamarine</td>
    <td>Palo Alto</td>
    <td>Row 1 Data 3</td>
    <td>Row 1 Data 4</td>
    </tr>
    """
    row_string = ""
    row_string += '<tr>'
    for i in row:
        row_string += '<td>' + i + '</td>'
    row_string += '</tr>\n'
    return row_string


def main():
    with open ("TheList.csv") as f:
        data_list = list(csv.reader(f))
        #print (data_list)

    with open ("index_template.html") as template_file:
        template = template_file.read()
    table = ""
    for row in data_list[1:]:
        table += generate_table_row(row)

    output = template.replace('{{table_content}}', table)
    with open('index.html','w') as outfile:
        outfile.write(output)

if __name__ == "__main__":
    main()

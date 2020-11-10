import xlsxwriter

# XLSX
workbook = xlsxwriter.Workbook('Machine3_processes.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

# DATA



#a_file = open("centos_pstree.txt", "r")
a_file = open("machine3_pstree.txt", "r")

list_of_lines = a_file.readlines()


for lines in list_of_lines:
    
    name = lines[slice(21)].strip()
    pid = lines[slice(21,27)].strip()
    UID = lines[slice(36,45)].strip()

    
    # first file
    worksheet.write(row, col,     name)
    worksheet.write(row, col + 1, pid)
    worksheet.write(row, col + 2, UID)

    row += 1

a_file.close()

workbook.close()
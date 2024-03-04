import gspread


gc = gspread.service_account(filename='cred.json')

# Open a sheet from a spreadsheet in one go
# wks = gc.open("letay").sheet1

# ID: 1389787624
# worksheet = gc.open("letay").add_worksheet(title='Другое', rows=1000, cols=500)

worksheet_try = gc.open("letay").get_worksheet(0)
worksheet_other = gc.open("letay").get_worksheet(1)

# worksheet_other.append_row(['89106155366', 'Nikita'])
# gc.open("letay").del_worksheet()
# print(gc.open("letay").del_worksheet_by_id(1))

# Update a range of cells using the top left corner address
# wks.update('A3', [[5, 7], [2, 12]])

# Or update a single cell
# wks.update('B12', ["it's down there somewhere, let me take another look."])

# Format the header
# wks.format('A1:B1', {'textFormat': {'bold': True}})

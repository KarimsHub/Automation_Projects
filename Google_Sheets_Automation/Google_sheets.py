import ezsheets

ss = ezsheets.Spreadsheet('1Qit1982XhY0mpbCJt3Ofh9Q2CSQRgA8slFivANKl_2U')

print(ss.title)

# creating new file: ezsheets.createSpreadsheet('')
# upload an existing file: ezsheets.upload('')
# list the spreadhssets in google account: ezsheets.listSpreadsheets()
# ss.downloadAsCSV() # only downloads the first sheet as file
# ss.downloadAsPDF()
# refresh method: sheet.refresh()

sw = ezsheets.upload('produceSales.xlsx')
sheet = sw[0]
sheet.getRow(1) # The first row is row 1, not row 0.
sheet.getRow(2)
# //the car game
# command = ''
# started = False
# while True:
#     command = input('> ').lower()
#     if command == 'start':
#         if started:
#             print('the car is already started...')
#         else:
#             started = True
#             print('the car start...')
#     elif command == 'stop':
#         if not started:
#             print('the car is already stopped...')
#         else:
#             started = False
#             print('the car stop...')
#     elif command == 'help':
#         print("""
#         start - to start the car
#         stop - to stop the car
#         quit - to quit
#         """)
#     elif command == 'quit':
#         break
#     else:
#         print("sorry, I don't understand the command")


# calculate the price in the list



# import openpyxl as xl
# from openpyxl.chart import PieChart, Reference
#
# def process_wb(filename):
#     wb = xl.load_workbook(filename)
#     sheet = wb['Sheet1']
#
#     for row in range(2, sheet.max_row + 1):
#         cell = sheet.cell(row, 3)
#         corrected_price = cell.value * 0.9
#         corrected_price_cell = sheet.cell(row, 4)
#         corrected_price_cell.value = corrected_price
#
#     values = Reference(sheet, min_row = 2,
#               max_row = sheet.max_row,
#               min_col = 4,
#               max_col = 4)
#
#     chart = PieChart()
#     chart.add_data(values)
#     sheet.add_chart(chart, 'e2')
#     wb.save(filename)
#
# process_wb('transactions.xlsx')
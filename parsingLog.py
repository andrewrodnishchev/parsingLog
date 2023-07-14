import openpyxl


book = openpyxl.open("logFile.xlsx", read_only = True)
sheet = book.active

for row in range(2,sheet.max_row+1):
        ip_address = sheet[row][0].value
        path = sheet[row][1].value
        response_code = sheet[row][2].value
        request_time_in_milliseconds = sheet[row][3].value

        print(ip_address+'----'+path+'----'+str(response_code)+'----'+str(request_time_in_milliseconds))

print('')
successful_requests = 0
total_response = 0
for row in range (2,sheet.max_row+1):
        response_code = sheet[row][2].value
        total_response += 1
        if 200 <= response_code <= 300:
                successful_requests += 1
                #print(response_code)
successful_persent = (successful_requests / total_response) * 100
print("Процент успешных запросов: " + str(round(successful_persent)) + " %")
# opens the um-server-01.txt file
log_file = open("um-server-01.txt")

# function called sales_reports with log_file bing passed in as an arg
def sales_reports(log_file):
    # loop thru ;og_file
    for line in log_file:
        # strips each line of excess text
        line = line.rstrip()
        # tells code which lines to target in file
        day = line[0:3]
        # prints data if day is monday
        if day == "Mon":
            print(line)

# runs sales_report function passing in log_file
sales_reports(log_file)

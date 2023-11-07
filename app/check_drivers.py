import pyodbc

# Get list of ODBC drivers
drivers = [driver for driver in pyodbc.drivers()]

# Print the drivers
for driver in drivers:
    print(driver)
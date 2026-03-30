# Nepali Calendar Utilities

# Mapping of Nepali months to corresponding English months
nepali_months = {
    1: 'Baisakh',
    2: 'Jestha',
    3: 'Ashadh',
    4: 'Shrawan',
    5: 'Bhadra',
    6: 'Ashwin',
    7: 'Kartik',
    8: 'Mangsir',
    9: 'Poush',
    10: 'Magh',
    11: 'Falgun',
    12: 'Chaitra'
}

# Function to get the Nepali month name

def get_nepali_month(month_number):
    return nepali_months.get(month_number, 'Invalid month')

# Example Usage
if __name__ == '__main__':
    for month in range(1, 13):
        print(f'Month {month}: {get_nepali_month(month)}')

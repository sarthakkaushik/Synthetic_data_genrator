import random
import datetime
import pandas as pd

def generate_random_string(length):
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=length))

def generate_random_date():
    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date(2024, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + datetime.timedelta(days=random_number_of_days)

def generate_synthetic_data(num_rows):
    countries_data = {
        'Chile': {'currency': 'CLP', 'region': 'LATAM'},
        'Australia': {'currency': 'AUD', 'region': 'AAA'},
        'Russia': {'currency': 'RUB', 'region': 'Russia'},
        'Belarus': {'currency': 'USD', 'region': 'CISR'},
        'United States': {'currency': 'USD', 'region': 'North America'},
        'Canada': {'currency': 'CAD', 'region': 'North America'},
        'United Kingdom': {'currency': 'GBP', 'region': 'Europe'},
        'Germany': {'currency': 'EUR', 'region': 'Europe'},
        'France': {'currency': 'EUR', 'region': 'Europe'},
        'Japan': {'currency': 'JPY', 'region': 'Asia'},
        'China': {'currency': 'CNY', 'region': 'Asia'},
        'India': {'currency': 'INR', 'region': 'Asia'},
        'Brazil': {'currency': 'BRL', 'region': 'LATAM'},
        'Mexico': {'currency': 'MXN', 'region': 'LATAM'},
        'South Africa': {'currency': 'ZAR', 'region': 'Africa'},
        'Nigeria': {'currency': 'NGN', 'region': 'Africa'},
        'Saudi Arabia': {'currency': 'SAR', 'region': 'Middle East'},
        'UAE': {'currency': 'AED', 'region': 'Middle East'},
        'New Zealand': {'currency': 'NZD', 'region': 'AAA'},
        'Singapore': {'currency': 'SGD', 'region': 'Asia'}
    }

    columns = [
        'DAILY_SALES_ID', 'BU_ID', 'MOLECULE', 'PTM', 'PLI', 'MWP', 'COUNTRY_ID',
        'ACTUAL_PLANNED_GROSS_SALES', 'FLAG', 'FLAG_DESCRIPTION', 'PRODUCT_ID',
        'PROD_ID', 'PLANT', 'CUSTOMER_CODE', 'DATE', 'CREATED_ON', 'COMPANY_CODE',
        'SALES_ORG', 'SUB_COUNTRY', 'COUNTRY', 'REGION', 'SAP_COUNTRY_CODE',
        'SUB_COUNTRY_LC', 'FOREIGN_CURRENCY', 'BASE_CURRENCY', 'BASE_UOM',
        'NET_SALES_QTY', 'ACTUAL_QTY', 'GROSS_SALES_VALUE_LC', 'GROSS_SALES_VALUE_USD',
        'GROSS_SALES_VALUE_INR', 'NET_SALES_VALUE_LC', 'NET_SALES_VALUE_USD',
        'NET_SALES_VALUE_INR', 'GROSS_TO_NET_PERCT', 'EXCHANGE_RATE', 'HEDGE_CURRENCY',
        'HEDGE_AMOUNT', 'SKU_GROSS_PRICE', 'SKU_NET_PRICE', 'NET_PLANNED_RATE_INR',
        'NET_PLANNED_RATE_USD', 'GROSS_PLANNED_RATE_INR', 'GROSS_PLANNED_RATE_USD',
        'LE_QTY_DAYLEVEL', 'LE_VALUE_LC_DAYLEVEL', 'LE_VALUE_USD_DAYLEVEL',
        'LE_VALUE_INR_DAYLEVEL', 'LE_PLANNED_RATE_USD_DAYLEVEL', 'LE_PLANNED_RATE_INR_DAYLEVEL',
        'BUDGET_QTY_DAYLEVEL', 'BUDGET_VALUE_LC_DAYLEVEL', 'BUDGET_VALUE_USD_DAYLEVEL',
        'BUDGET_VALUE_INR_DAYLEVEL', 'ACTUAL_NET_SALES_LC', 'ACTUAL_NET_SALES_USD',
        'ACTUAL_NET_SALES_INR', 'PY_QUANTITY', 'PY_NET_SALES_VAL_LC', 'PY_NET_SALES_VAL_USD',
        'PY_NET_SALES_VAL_INR', 'PY_NET_SALES_VALUE_LC', 'PY_NET_SALES_VALUE_USD',
        'PY_NET_SALES_VALUE_INR', 'INSERTED_DTTM'
    ]

    data = []

    for _ in range(num_rows):
        country = random.choice(list(countries_data.keys()))
        currency = countries_data[country]['currency']
        region = countries_data[country]['region']

        row = [
            random.randint(1000, 20000),  # DAILY_SALES_ID
            'EM',  # BU_ID
            '',  # MOLECULE
            'DUMMY',  # PTM
            'FALSE',  # PLI
            'FALSE',  # MWP
            f"{country}|{country[:2].upper()}|SAP",  # COUNTRY_ID
            '1',  # ACTUAL_PLANNED_GROSS_SALES
            '2',  # FLAG
            'LE',  # FLAG_DESCRIPTION
            f"{country[:3].upper()}{generate_random_string(6)}",  # PRODUCT_ID
            '',  # PROD_ID
            '',  # PLANT
            '',  # CUSTOMER_CODE
            random.randint(45000, 46000),  # DATE
            '',  # CREATED_ON
            '',  # COMPANY_CODE
            '',  # SALES_ORG
            country,  # SUB_COUNTRY
            country,  # COUNTRY
            region,  # REGION
            country[:2].upper(),  # SAP_COUNTRY_CODE
            currency,  # SUB_COUNTRY_LC
            '',  # FOREIGN_CURRENCY
            'INR',  # BASE_CURRENCY
            ''  # BASE_UOM
        ]

        # Generate random numerical values for the remaining columns
        row.extend([random.randint(-500000, 5000000) for _ in range(len(columns) - len(row) - 1)])

        row.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f UTC"))  # INSERTED_DTTM

        data.append(row)

    return pd.DataFrame(data, columns=columns)

# Generate 100 rows of synthetic data
df = generate_synthetic_data(100)

# Display the first few rows of the DataFrame
print(df.head())

# Display information about the DataFrame
print(df.info())

# Optionally, save the DataFrame to a CSV file
# df.to_csv('synthetic_data.csv', index=False)
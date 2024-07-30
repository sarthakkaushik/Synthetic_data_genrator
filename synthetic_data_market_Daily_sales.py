import random
import datetime
import pandas as pd
import numpy as np

def generate_random_string(length):
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=length))

def generate_random_date():
    start_date = datetime.date(2019, 1, 1)
    end_date = datetime.date(2025, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + datetime.timedelta(days=random_number_of_days)

def generate_synthetic_data(num_rows):
    countries = ['Kazakhstan', 'Russia', 'Ukraine', 'Brazil', 'South Africa']
    drug_classes = ['S01E Miotics and antiglaucoma preparations', 'M01A Anti-rheumatics, non-steroidal', 
                    'B02A Antifibrinolytics', 'M05X All other musculoskeletal products', 
                    'G2B0  TOPICAL CONTRACEPTIVES', 'D11A Other dermatological preparations']
    corporations = ['Laboratorio Edol - Productos Farmaceuticos S.A.', 'Dr.Reddy`s Laboratories Ltd.', 
                    'Macleods Pharmaceuticals Ltd', 'Kusum Pharm LLC', 'GUERBET', 'GM PHARMACEUTICALS']
    molecules = ['Brimonadine', 'HYPOSULFUROUS ACID', 'Ketorolac', 'Tranexamic acid', 'SECNIDAZOLUM', 'IOVERSOL']
    dosage_forms = ['Drops eye', 'Tablets', 'Solution for injections', 'PARENT ORD I V AMPOULES', 'MZY OTHER MED.AIDS']
    currencies = {'Kazakhstan': 'KZT', 'Russia': 'RUB', 'Ukraine': 'UAH', 'Brazil': 'BRL', 'South Africa': 'ZAR'}
    segments = ['RX', 'OTC', 'Ã‚Â -']
    channels = ['Retail', 'Drugs', 'Licitacoes', 'Food supplement']
    atc1 = ['S', 'M', 'B', 'G', 'D', 'V', 'J', 'P', 'A']

    data = []

    for _ in range(num_rows):
        country = random.choice(countries)
        currency = currencies[country]
        
        row = {
            'BU': 'EM',
            'COUNTRY': country,
            'DRUG_CLASS': random.choice(drug_classes),
            'CORPORATION': random.choice(corporations),
            'MOLECULE': random.choice(molecules),
            'BRAND': f"{generate_random_string(6)} {random.randint(100, 999)}",
            'DOSAGE_FORM': random.choice(dosage_forms),
            'RPM': random.choice(drug_classes),
            'ERPM': '',
            'REPORTING_MONTH': random.randint(43000, 46000),
            'SALES_VALUE_LC': round(random.uniform(1000000, 1000000000), 2),
            'SALES_VALUE_USD': round(random.uniform(100000, 1000000000), 2),
            'SALES_VALUE_INR': round(random.uniform(1000000, 1000000000), 2),
            'SALES_QUANTITY': round(random.uniform(100000, 10000000), 4),
            'CURRENCY': currency,
            'PACK': f"{generate_random_string(3)} {random.randint(1, 100)}",
            'STRENGTH': f"{random.randint(1, 1000)}MG",
            'LAUNCH_MONTH': random.randint(37000, 44000),
            'MANUFACTURER': random.choice(corporations),
            'SKU': f"{generate_random_string(8)}, {random.choice(corporations)}, {generate_random_string(20)}",
            'SEGMENT': random.choice(segments),
            'CHANNEL': random.choice(channels),
            'INNOVATOR_NON_INNOVATOR': '',
            'ROUTE_OF_ADMINISTRATION': '',
            'DRUG_FORM': '',
            'ATC1': random.choice(atc1),
            'ATC2': f"{random.choice(atc1)}{random.randint(1, 99)}",
            'ATC3': random.choice(drug_classes),
            'ATC4': '',
            'COMPANY': random.choice(corporations),
            'FY_YEAR': f"FY {random.randint(2019, 2025)}",
            'FY_MONTH_SHORT': random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']),
            'FY_QTR': f"Q{random.randint(1, 4)}",
            'SUB_REGION': f"{generate_random_string(8)} region",
            'MOLECULE_DESC': '',
            'INSERTED_DTTM': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f UTC")
        }
        
        data.append(row)

    return pd.DataFrame(data)

# Generate 100 rows of synthetic data
df = generate_synthetic_data(100)

# Display the first few rows of the DataFrame
print(df.head())

# Display information about the DataFrame
print(df.info())

# Optionally, save the DataFrame to a CSV file
# df.to_csv('synthetic_pharma_data.csv', index=False)
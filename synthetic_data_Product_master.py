import random
import pandas as pd

def generate_random_string(length):
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=length))

def generate_synthetic_data(num_rows):
    countries = {
        'KZ': 'KAZAKHSTAN',
        'RU': 'RUSSIA',
        'UA': 'UKRAINE',
        'BR': 'BRAZIL',
        'ZA': 'SOUTH AFRICA',
        'AU': 'AUSTRALIA',
        'BY': 'BELARUS',
        'US': 'UNITED STATES',
        'CA': 'CANADA',
        'GB': 'UNITED KINGDOM',
        'DE': 'GERMANY',
        'FR': 'FRANCE',
        'JP': 'JAPAN',
        'CN': 'CHINA',
        'IN': 'INDIA',
        'MX': 'MEXICO',
        'NG': 'NIGERIA',
        'SA': 'SAUDI ARABIA',
        'AE': 'UAE',
        'NZ': 'NEW ZEALAND'
    }

    product_types = [
        'Cream', 'Syrup', 'Tablet', 'Injection', 'Spray', 'Sachet', 'Nasal Spray',
        'Capsule', 'Ointment', 'Solution', 'Suspension', 'Gel', 'Powder', 'Inhaler'
    ]

    brands = [
        'Carboprost', 'Ezmitop', 'Fredulex', 'Becozinc', 'Bion', 'Admera', 'Cartilox',
        'Cisplatin', 'Docetere', 'Momate Rino', 'Glenspray', 'Nise', 'Omez', 'Mitotax',
        'Paracetamol', 'Ibuprofen', 'Aspirin', 'Amoxicillin', 'Loratadine', 'Metformin'
    ]

    data = []

    for _ in range(num_rows):
        country_code, country = random.choice(list(countries.items()))
        brand = random.choice(brands)
        product_type = random.choice(product_types)
        
        pk_sku_id = f"{country_code}300{random.randint(100000, 999999)}"
        material_code = pk_sku_id[3:]
        
        description = f"{brand} {product_type} {random.randint(10, 500)}"
        if random.choice([True, False]):
            description += f"{random.choice(['mg', 'mcg', 'ml'])} "
        description += f"{random.randint(1, 120)}s {country}"

        row = {
            'PK_SKU_ID': pk_sku_id,
            'Filing_Country': country_code,
            'Country_Code': country_code,
            'Material_Code': material_code,
            'Description': description
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
# df.to_csv('synthetic_product_master_data.csv', index=False)
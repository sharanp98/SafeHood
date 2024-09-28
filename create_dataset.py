import csv
import random

# List of provided zip codes
zipcodes = [
    '85003', '85004', '85006', '85007', '85008', '85009', '85012', '85013', '85014', '85015',
    '85016', '85017', '85018', '85019', '85020', '85021', '85022', '85023', '85024', '85027',
    '85028', '85029', '85031', '85032', '85033', '85034', '85035', '85037', '85040', '85041',
    '85042', '85043', '85044', '85045', '85048', '85050', '85051', '85053', '85054', '85083',
    '85085', '85086', '85087', '85201', '85202', '85203', '85204', '85205', '85210', '85213',
    '85224', '85225', '85226', '85233', '85250', '85251', '85253', '85254', '85255', '85256',
    '85257', '85258', '85259', '85260', '85262', '85263', '85266', '85268', '85281', '85282',
    '85283', '85284', '85301', '85302', '85303', '85304', '85305', '85306', '85307', '85308',
    '85309', '85310', '85323', '85331', '85335', '85338', '85339', '85340', '85345', '85351',
    '85353', '85355', '85363', '85373', '85374', '85375', '85377', '85379', '85381', '85382',
    '85383', '85387', '85388', '85392', '85395'
]

# Generate 150 random records
def generate_neighborhood_safety_data():
    records = []
    for _ in range(150):
        zipcode = random.choice(zipcodes)
        violent_crime_rate = random.randint(100, 1000)
        property_crime_rate = random.randint(500, 2500)
        feel_safe_day = round(random.uniform(5.0, 9.5), 1)
        feel_safe_night = round(random.uniform(3.0, 8.5), 1)
        median_income = random.randint(30000, 150000)
        median_home_value = random.randint(150000, 1000000)
        population_density = random.randint(1000, 15000)
        pct_diversity = round(random.uniform(0.2, 0.9), 2)
        environmental_issues = random.choice(['Yes', 'No'])
        community_engagement_score = round(random.uniform(4.0, 9.0), 1)
        police_presence = random.randint(5, 40)

        records.append([
            zipcode, violent_crime_rate, property_crime_rate, feel_safe_day, feel_safe_night,
            median_income, median_home_value, population_density, pct_diversity,
            environmental_issues, community_engagement_score, police_presence
        ])
    
    return records

# Write records to CSV
def write_to_csv(filename, records):
    header = ['zipcode', 'violent_crime_rate', 'property_crime_rate', 'feel_safe_day', 
              'feel_safe_night', 'median_income', 'median_home_value', 'population_density', 
              'pct_diversity', 'environmental_issues', 'community_engagement_score', 
              'police_presence']

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(records)

# Generate records and write to CSV
filename = 'neighborhood_safety_data_phoenix_area.csv'
data = generate_neighborhood_safety_data()
write_to_csv(filename, data)

print(f"{filename} created with 150 records.")

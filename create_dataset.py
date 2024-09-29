import csv
import random

# Mapping of ZIP codes to area names
zipcode_area_mapping = {
    '85003': 'Downtown Phoenix',
    '85004': 'Central City',
    '85006': 'Coronado',
    '85007': 'South Phoenix',
    '85008': 'East Phoenix',
    '85009': 'Phoenix Sky Harbor Airport',
    '85012': 'Encanto',
    '85013': 'Alhambra',
    '85014': 'North Mountain',
    '85015': 'Westwood',
    '85016': 'Biltmore',
    '85017': 'Maryvale',
    '85018': 'Arcadia',
    '85019': 'Cave Creek',
    '85020': 'North Phoenix',
    '85021': 'Windsor Square',
    '85022': 'Paradise Valley',
    '85023': 'Moon Valley',
    '85024': 'Phoenix',
    '85027': 'Deer Valley',
    '85028': 'North Valley',
    '85029': 'Desert View',
    '85031': 'West Phoenix',
    '85032': 'Paradise Valley',
    '85033': 'Maryvale',
    '85034': 'Phoenix',
    '85035': 'South Phoenix',
    '85037': 'Phoenix',
    '85040': 'Phoenix',
    '85041': 'Laveen',
    '85042': 'Phoenix',
    '85043': 'Phoenix',
    '85044': 'Ahwatukee Foothills',
    '85045': 'Phoenix',
    '85048': 'Ahwatukee Foothills',
    '85050': 'Desert Ridge',
    '85051': 'Phoenix',
    '85053': 'Phoenix',
    '85054': 'North Phoenix',
    '85083': 'Phoenix',
    '85085': 'Phoenix',
    '85086': 'Anthem',
    '85087': 'New River',
    '85201': 'Mesa',
    '85202': 'Mesa',
    '85203': 'Mesa',
    '85204': 'Mesa',
    '85205': 'Mesa',
    '85210': 'Tempe',
    '85213': 'Mesa',
    '85224': 'Chandler',
    '85225': 'Chandler',
    '85226': 'Chandler',
    '85233': 'Gilbert',
    '85250': 'Scottsdale',
    '85251': 'Scottsdale',
    '85253': 'Scottsdale',
    '85254': 'Scottsdale',
    '85255': 'Scottsdale',
    '85256': 'Scottsdale',
    '85257': 'Scottsdale',
    '85258': 'Scottsdale',
    '85259': 'Scottsdale',
    '85260': 'Scottsdale',
    '85262': 'Scottsdale',
    '85263': 'Scottsdale',
    '85266': 'Scottsdale',
    '85268': 'Fountain Hills',
    '85281': 'Tempe',
    '85282': 'Tempe',
    '85283': 'Tempe',
    '85284': 'Tempe',
    '85301': 'Phoenix',
    '85302': 'Glendale',
    '85303': 'Glendale',
    '85304': 'Glendale',
    '85305': 'Glendale',
    '85306': 'Phoenix',
    '85307': 'Phoenix',
    '85308': 'Peoria',
    '85309': 'Phoenix',
    '85310': 'Phoenix',
    '85323': 'Avondale',
    '85331': 'Cave Creek',
    '85335': 'Sun City',
    '85338': 'Goodyear',
    '85339': 'Phoenix',
    '85340': 'Glendale',
    '85345': 'Phoenix',
    '85351': 'Phoenix',
    '85353': 'Phoenix',
    '85355': 'Phoenix',
    '85363': 'Wittmann',
    '85373': 'Surprise',
    '85374': 'Surprise',
    '85375': 'Surprise',
    '85377': 'Carefree',
    '85379': 'Surprise',
    '85381': 'El Mirage',
    '85382': 'Peoria',
    '85383': 'Peoria',
    '85387': 'Surprise',
    '85388': 'Phoenix',
    '85392': 'Goodyear',
    '85395': 'Goodyear'
}

# Generate neighborhood safety data
def generate_neighborhood_safety_data():
    records = []
    
    # First, include all unique area names
    unique_zipcodes = list(zipcode_area_mapping.keys())
    for zipcode in unique_zipcodes:
        area_name = zipcode_area_mapping[zipcode]  # Get the corresponding area name
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

        records.append([zipcode, area_name, violent_crime_rate, property_crime_rate, feel_safe_day, feel_safe_night,
                        median_income, median_home_value, population_density, pct_diversity,
                        environmental_issues, community_engagement_score, police_presence])
    
    # Add more records to reach 150 total, ensuring random selection of zip codes
    while len(records) < 150:
        zipcode = random.choice(unique_zipcodes)
        area_name = zipcode_area_mapping[zipcode]
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

        records.append([zipcode, area_name, violent_crime_rate, property_crime_rate, feel_safe_day, feel_safe_night,
                        median_income, median_home_value, population_density, pct_diversity,
                        environmental_issues, community_engagement_score, police_presence])

    return records

# Write records to CSV
def write_to_csv(filename, records):
    header = ['zipcode', 'area_name', 'violent_crime_rate', 'property_crime_rate', 'feel_safe_day', 
              'feel_safe_night', 'median_income', 'median_home_value', 'population_density', 
              'pct_diversity', 'environmental_issues', 'community_engagement_score', 
              'police_presence']

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(records)

# Generate records and write to CSV
filename = 'neighborhood_data.csv'
data = generate_neighborhood_safety_data()
write_to_csv(filename, data)

print(f"{filename} created with {len(data)} records.")

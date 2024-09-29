import os
import csv
import json
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment variable
api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

def get_neighborhood_safety(zipcode):
    """Fetch neighborhood data and categorize it based on the given zipcode."""
    
    # Extract the row of neighborhood data based on the given zipcode
    with open('neighborhood_data.csv', mode='r') as file:
        reader = csv.reader(file)
        header = next(reader, None)  # Skip the header if there is one
        
        for row in reader:
            if row[0] == zipcode:  # Check if the first column matches the zipcode
                return categorize_neighborhood(row)  # Return the JSON response
    
    return json.dumps({"error": "No data found for the provided zipcode."})  # JSON error response

def categorize_neighborhood(data_row):
    # Parse the input data
    (
        zipcode,
        area_name,
        violent_crime_rate,
        property_crime_rate,
        feel_safe_day,
        feel_safe_night,
        median_income,
        median_home_value,
        population_density,
        pct_diversity,
        environmental_issues,
        community_engagement_score,
        police_presence
    ) = data_row

    # Construct the prompt for the OpenAI API
    prompt = (
        f"Based on the following neighborhood data:\n"
        f"Zipcode: {zipcode}\n"
        f"Area Name: {area_name}\n"
        f"Violent Crime Rate: {violent_crime_rate}\n"
        f"Property Crime Rate: {property_crime_rate}\n"
        f"Feel Safe During Day (1-10): {feel_safe_day}\n"
        f"Feel Safe During Night (1-10): {feel_safe_night}\n"
        f"Median Income: {median_income}\n"
        f"Median Home Value: {median_home_value}\n"
        f"Population Density: {population_density}\n"
        f"Percentage of Diversity: {pct_diversity}\n"
        f"Environmental Issues: {environmental_issues}\n"
        f"Community Engagement Score: {community_engagement_score}\n"
        f"Police Presence: {police_presence}\n\n"
        f"Please categorize this neighborhood based on safety as a percentage (0-100%) and provide a concise reasoning for your classification in JSON format. "
        f'Example: {{"areaName": "Tempe", "reasoning": "The neighborhood in Tempe has a moderate safety rating of 45%. While the violent crime rate is relatively high, the property crime rate is also above average. Residents feel somewhat safe during the day but less safe at night. The presence of environmental issues may impact safety perceptions, and the community engagement score is average. The median income and home value are relatively high, reflecting a well-off community. However, the population density is also high, which may contribute to higher crime rates. Overall, this neighborhood falls in the middle in terms of safety.", "safetyPercentage": 45}}'
        f"The output should include the area name but not impact the safety rating."
    )

    # Create a chat completion request
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # Get the response and return it as JSON
    response = completion.choices[0].message.content.strip()
    return json.loads(response)  # Assuming the response is already in JSON format

# Example usage when the script is executed directly (for testing)
if __name__ == "__main__":
    zipcode = "85282"
    result = get_neighborhood_safety(zipcode)
    print(result)

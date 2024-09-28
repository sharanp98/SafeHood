import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment variable
api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

def categorize_neighborhood(data_row):
    # Parse the input data
    (
        zipcode,
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
    ) = data_row.split(',')

    # Construct the prompt for the OpenAI API
    prompt = (
        f"Based on the following neighborhood data:\n"
        f"Zipcode: {zipcode}\n"
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
        f"Please categorize this neighborhood based on safety as a percentage (0-100%) and provide a concise reasoning for your classification in JSON format. Do not include any information outside the json "
        f"like this: {{'safety_percentage': '75%', 'reasoning': 'Moderate crime rates but good community engagement.'}}."
    )

    # Create a chat completion request
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Update to the correct model you want to use
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # Get the response and return the categorization
    return completion.choices[0].message.content.strip()

# Example usage
data_row = "85308,813,2415,5.5,6.9,39846,269878,10935,0.55,Yes,7.5,13"
result = categorize_neighborhood(data_row)
print(f"{result}")

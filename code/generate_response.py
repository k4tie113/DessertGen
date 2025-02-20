# generate_response.py: generates a response by making a call to my fine-tuned model

import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Initialize OpenAI client
client = openai.OpenAI(api_key=API_KEY)

# Define the prompt
prompt = "[ingredients: apple, butter, sugar, watermelon, flour, salt, ice, vanilla extract, egg][appliances: oven, microwave, blender, food processor][time: 90 minutes]"

# Make the API call
response = client.chat.completions.create(
    model="ft:gpt-3.5-turbo-0125:personal::B2tRnXUX",  # Your fine-tuned model ID
    messages=[
        {"role": "system", "content": "You are a helpful assistant that generates a dessert recipe from the dataset."},
        {"role": "user", "content": prompt}
    ]
)

# Print the model's response
print(response.choices[0].message.content)  # Corrected for new API format

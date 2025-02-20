#finetune.py: main script for fine tuning.
import openai
import openai
import os
from dotenv import load_dotenv
# OpenAI client
load_dotenv()
API_KEY = os.getenv("API_KEY")
client = openai.OpenAI(api_key=API_KEY)

# Start fine-tuning using the uploaded file ID
fine_tune = client.fine_tuning.jobs.create(
    training_file="file-VJuHVLJqpCPwcMDh9UCWSz",
    model="gpt-3.5-turbo"
)

# Print the fine-tuning job ID 
#Job ID: ftjob-EDsjG3AEoPDEunWLywfRML79
print(f"Fine-tuning started! Job ID: {fine_tune.id}")

""" COMPLETED AS OF 2/19 - GENERATED FILE ID FOR FINE TUNING DATASET: file-VJuHVLJqpCPwcMDh9UCWSz
# Upload the fine-tuning dataset
file = client.files.create(
    file=open("../data/recipes_finetune.jsonl", "rb"),
    purpose="fine-tune"
)

# Get the uploaded file ID
file_id = file.id
print(f"Uploaded file ID: {file_id}")
"""


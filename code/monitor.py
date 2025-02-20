
#monitor.py: check up on the fine tuning status from the openAI
import openai
import os
from dotenv import load_dotenv
# OpenAI client
load_dotenv()
API_KEY = os.getenv("API_KEY")
client = openai.OpenAI(api_key=API_KEY)

# Job ID from fine-tuning start
job_id = "ftjob-EDsjG3AEoPDEunWLywfRML79"

# Get job status
job_status = client.fine_tuning.jobs.retrieve(job_id)
print(f"Fine-tuning status: {job_status.status}")


# If fine-tuning is complete, print the model ID
if job_status.status == "succeeded":
    print(f"Your fine-tuned model ID: {job_status.fine_tuned_model}")
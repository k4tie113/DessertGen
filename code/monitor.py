#monitor.py: check up on the fine tuning status from the openAI servers
import openai

# OpenAI client
client = openai.OpenAI(api_key="")

# Job ID from fine-tuning start
job_id = "ftjob-reHvBKPoHYb4a3MkcGeHDcfs"

# Get job status
job_status = client.fine_tuning.jobs.retrieve(job_id)
print(f"Fine-tuning status: {job_status.status}")


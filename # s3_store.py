# s3_store.py
import boto3
import json
from datetime import datetime

s3 = boto3.client('s3')
bucket_name = "soc-ticket-logs-bucket"

def upload_log(ticket_data):
    key = f"logs/ticket_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
    s3.put_object(
        Bucket=bucket_name,
        Key=key,
        Body=json.dumps(ticket_data),
        ContentType='application/json'
    )
    print(f"Ticket log uploaded to s3://{bucket_name}/{key}")

# eventbridge_schedule.py
import boto3
from datetime import datetime, timedelta

# Create EventBridge client
eventbridge = boto3.client('events')

rule_name = "SOC_Ticket_Generator"

# Schedule to run every 5 minutes
response = eventbridge.put_rule(
    Name=rule_name,
    ScheduleExpression='rate(5 minutes)',
    State='ENABLED',
    Description='Trigger SOC ticket generation'
)

rule_arn = response['RuleArn']

# Target: Lambda or EC2 endpoint
# Example: sending to an EC2 endpoint via EventBridge target
target = {
    'Id': 'EC2Target',
    'Arn': 'arn:aws:events:us-east-1:123456789012:rule/SOC_Ticket_Generator',  # Replace with your EC2 target or Lambda
    'Input': '{"action":"generate_ticket"}'
}

eventbridge.put_targets(Rule=rule_name, Targets=[target])
print("EventBridge scheduled successfully!")

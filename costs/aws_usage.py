import os
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from dotenv import load_dotenv


def fetch_aws_usage():
    load_dotenv()
    try:
        # Create a session using your AWS credentials
        session = boto3.Session(
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name='us-east-2'  # or your preferred region
        )

        # Create a Cost Explorer client
        client = session.client('ce')

        # Define the time period for which you want to fetch the usage data
        time_period = {
            "Start": "2022-01-01",  # replace with your start date
            "End": "2022-12-31"  # replace with your end date
        }

        free_tier_filter = {
            "And": [
                {
                    "Dimensions": {
                        "Key": "USAGE_TYPE_GROUP",
                        "Values": ["Free tier"]
                    }
                }
            ]
        }

        # Fetch the usage data
        response = client.get_cost_and_usage(
            TimePeriod=time_period,
            Granularity='MONTHLY',
            Metrics=['UsageQuantity'],
            Filter=free_tier_filter
        )

        return response

    except (BotoCoreError, ClientError) as error:
        print(f"An error occurred: {error}")
        return None


def __main():
    response = fetch_aws_usage()
    print(response)
    return response


if __name__ == '__main__':
    __main()

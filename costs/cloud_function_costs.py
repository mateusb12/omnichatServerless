import datetime
import os

from dotenv import load_dotenv
from google.cloud import functions_v1, billing_v1, monitoring_v3
from google.cloud.functions_v1.services.cloud_functions_service import CloudFunctionsServiceClient
from google.cloud.functions_v1.types import ListFunctionsRequest
from google.protobuf import timestamp_pb2
from google.cloud import storage


class CloudFunctionCosts:
    def __init__(self):
        load_dotenv()
        self.project_id = os.getenv('SDK_PROJECT_ID')
        self.billing_account_name = os.getenv("GOOGLE_BILLING_ACCOUNT_ID")
        self.DAYS_IN_THE_PAST = 30
        self.functions_client = CloudFunctionsServiceClient()
        self.billing_client = billing_v1.CloudBillingClient()
        self.monitoring_client = monitoring_v3.MetricServiceClient()
        self.interval = self.__initialize_interval()
        self.functions = self.__get_all_deployed_functions()
        self.storage_client = storage.Client()

    def __initialize_interval(self):
        now = datetime.datetime.utcnow()
        start_time_seconds = int((now - datetime.timedelta(days=self.DAYS_IN_THE_PAST)).timestamp())
        end_time_seconds = int(now.timestamp())
        interval = monitoring_v3.TimeInterval(
            start_time=timestamp_pb2.Timestamp(seconds=start_time_seconds),
            end_time=timestamp_pb2.Timestamp(seconds=end_time_seconds)
        )
        return interval

    def __get_all_deployed_functions(self):
        request = ListFunctionsRequest(parent=f"projects/{self.project_id}/locations/-")
        return self.functions_client.list_functions(request=request)

    def __search_through_functions(self, functions):
        for function in functions:
            # Assuming each function's name has the structure: projects/*/locations/*/functions/*
            function_name = function.name.split('/')[-1]

            # Construct filter for the Cloud Monitoring API request
            filter_str = f'resource.type="cloud_function" AND resource.labels.function_name="{function_name}" AND metric.type="cloudfunctions.googleapis.com/function/execution_count"'

            results = self.monitoring_client.list_time_series(name=f"projects/{self.project_id}",
                                                              filter=filter_str,
                                                              interval=self.interval,
                                                              view=monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL)
            invocations = 0
            for result in results:
                for point in result.points:
                    invocations += point.value.int64_value

            # Calculate cost based on number of invocations and any other metrics you want
            cost_per_invocation = 0.0000004  # Sample rate; adjust as per your actual pricing
            total_cost = invocations * cost_per_invocation

            print(f"Function {function_name} has been invoked {invocations} times. Estimated cost: ${total_cost:.6f}")
            print("-------------------------------")

    def __get_bucket_size(self, bucket_name):
        bucket = self.storage_client.get_bucket(bucket_name)
        size = 0
        for blob in bucket.list_blobs():
            size += blob.size
        return size

    def __estimate_storage_costs(self):
        buckets = self.storage_client.list_buckets()
        for bucket in buckets:
            size_in_gb = self.__get_bucket_size(bucket.name) / (1024 * 1024 * 1024)
            # Assuming a cost of $0.02 per GB per month
            cost = size_in_gb * 0.02
            print(f"Bucket {bucket.name} size: {size_in_gb:.2f} GB. Estimated cost: ${cost:.2f} per month")

    def run(self):
        # functions = self.__get_all_deployed_functions()
        # self.__search_through_functions(functions)
        self.__estimate_storage_costs()


def __main():
    cfc = CloudFunctionCosts()
    cfc.run()


if __name__ == "__main__":
    __main()

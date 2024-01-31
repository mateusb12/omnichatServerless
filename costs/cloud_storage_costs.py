import os
import time

from google.cloud import monitoring_v3

from costs.load_cloud_credentials import load_cloud_credentials


def get_costs_by_label(project_id, label_key, label_value):
    client = monitoring_v3.MetricServiceClient()
    interval = monitoring_v3.TimeInterval(
        {
            "end_time": {"seconds": int(time.time())},
            "start_time": {"seconds": int(time.time() - 60 * 60 * 24 * 30)},  # Last 30 days
        }
    )
    results = client.list_time_series(
        name=f"projects/{project_id}",
        filter=f'metric.type="billing.googleapis.com/account/cost_amount"',
        interval=interval,
        view=monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL,
    )
    for result in results:
        for point in result.points:
            print(f"Cost: ${point.value.double_value}")


def __main():
    load_cloud_credentials()
    project_id = os.getenv('SDK_PROJECT_ID')
    label_key = 'bucket'
    label_value = 'analysis'
    get_costs_by_label(project_id, label_key, label_value)


if __name__ == "__main__":
    __main()

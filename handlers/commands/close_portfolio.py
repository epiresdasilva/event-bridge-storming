import json
import boto3


client = boto3.client('events')


def main(event, context):
    event_response = client.put_events(
        Entries=[
            {
                'Source': 'PortfolioClosed',
                'DetailType': 'Portfolio Closed',
                'Detail': event["body"],
                'EventBusName': 'tdc-event-bridge-bus'
            },
        ]
    )

    print("Event was sent: ", event["body"])

    response = {
        "statusCode": 200,
        "body": json.dumps(event_response)
    }

    return response

import json
import boto3


client = boto3.client('events')


def main(event, context):
    event_response = client.put_events(
        Entries=[
            {
                'Source': 'OrderPlaced',
                'DetailType': 'Order Placed',
                'Detail': event["body"],
                'EventBusName': 'tdc-event-bridge-bus'
            },
            {
                'Source': 'SharesDebited',
                'DetailType': 'Shares Debited',
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

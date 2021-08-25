def main(event, context):
    print("Shares was debited: ", str(event))

    return {
        "message": "Shares was debited",
        "event": event
    }

def main(event, context):
    print("A portfolio was closed: ", str(event))

    return {
        "message": "A portfolio was closed",
        "event": event
    }

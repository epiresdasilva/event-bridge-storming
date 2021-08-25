def main(event, context):
    print("An order was placed: ", str(event))

    return {
        "message": "An order was placed",
        "event": event
    }

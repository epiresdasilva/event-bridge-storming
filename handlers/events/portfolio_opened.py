def main(event, context):
    print("A portfolio was opened: ", str(event))

    return {
        "message": "A portfolio was opened",
        "event": event
    }

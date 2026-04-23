import time
from azure.servicebus import ServiceBusClient
import os

LISTEN_CONNECTION_STR = os.getenv("SERVICEBUS_LISTEN")
QUEUE_NAME = "mikitamalafei"

def listen_queue():
    with ServiceBusClient.from_connection_string(LISTEN_CONNECTION_STR) as client:
        receiver = client.get_queue_receiver(queue_name=QUEUE_NAME)

        with receiver:
            while True:
                messages = receiver.receive_messages(max_message_count=5, max_wait_time=5)

                for msg in messages:
                    print("Received:", b"".join(msg.body).decode())
                    receiver.complete_message(msg)

                time.sleep(5)
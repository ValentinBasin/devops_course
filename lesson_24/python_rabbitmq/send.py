import pika
import sys

credentials = pika.PlainCredentials("user", "Qwerty123")
connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost", credentials=credentials)
)
chanell = connection.channel()
chanell.queue_declare(queue="Hello")

if len(sys.argv[1]) > 1:
    message = "".join(sys.argv[1:])
else:
    message = "Default message"
chanell.basic_publish(exchange="", routing_key="Hello", body=message)
connection.close()

import pika
import sys

credentials = pika.PlainCredentials("user", "Qwerty123")
connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost", credentials=credentials)
)
chanell = connection.channel()
chanell.exchange_declare(exchange="errors-direct", exchange_type="direct")
severity = sys.argv[1] if len(sys.argv[1]) > 1 else "info"
message = "".join(sys.argv[2:]) or "Hello"

chanell.basic_publish(exchange="errors-direct", routing_key=severity, body=message)
connection.close()

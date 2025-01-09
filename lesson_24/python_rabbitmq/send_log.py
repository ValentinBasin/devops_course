import pika


credentials = pika.PlainCredentials("user", "Qwerty123")
connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost", credentials=credentials)
)
channel = connection.channel()
channel.exchange_declare(exchange="logs", exchange_type="fanout")
with open("test.log", "r") as f:
    for line in f:
        channel.basic_publish(exchange="logs", routing_key="", body=line)
connection.close()

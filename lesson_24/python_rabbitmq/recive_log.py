import pika
import sys
import os


def main():
    credentials = pika.PlainCredentials("user", "Qwerty123")
    connection = pika.BlockingConnection(
        pika.ConnectionParameters("localhost", credentials=credentials)
    )
    chanell = connection.channel()
    queue = chanell.queue_declare(queue="", exclusive=True)
    chanell.queue_bind(exchange="logs", queue=queue.method.queue)

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    chanell.basic_consume(
        queue=queue.method.queue, on_message_callback=callback, auto_ack=True
    )

    chanell.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    main()

import pika
import sys

url = "amqp://tafzfptx:lRrZ2PMfADB1Rq7zUHIs7J4dzkpTXQ1x@otter.rmq.cloudamqp.com/tafzfptx" ;
params = pika.URLParameters(url);
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print(" [x] Sent %r" % message)
connection.close()
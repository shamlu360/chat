import pika
import sys

url = "amqp://tafzfptx:lRrZ2PMfADB1Rq7zUHIs7J4dzkpTXQ1x@otter.rmq.cloudamqp.com/tafzfptx" ;
params = pika.URLParameters(url);
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()
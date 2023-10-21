from faker import Faker
import pika

from models import Contact


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='email_queue')

fake = Faker()

def generate_contacts(count):
    fake_contacts = []
    for i in range(count):
        name = fake.name()
        email = fake.email()
        contact = Contact(full_name=name, email=email)
        contact.save()
        fake_contacts.append(contact)
    return fake_contacts


def send_contact(contact):
    channel.basic_publish(exchange='', routing_key='email_queue', body=str(contact.id).encode())
    print(f"{contact.full_name} id: {contact.id} sent to the queue")

if __name__ == '__main__':
    
    num_contacts = 5 
    fake_contacts = generate_contacts(num_contacts)
    
    for contact in fake_contacts:
        send_contact(contact)
    connection.close()
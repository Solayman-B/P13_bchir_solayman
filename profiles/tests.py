from django.test import Client
client = Client()

def test_index(client):
	response = client.get('/')
	data = response.data.decode()
	assert 'Welcome' in data
import logging
from websocket_server import WebsocketServer


def newMess(m):
	print("mmmm")
	logging.info(m)
def new_client(client, server):
	client.send_message("video","video")
	server.send_message_to_all("Hey all, a new client has joined us")
def sendVideo(client,server):
	print("jaayaay")

server = WebsocketServer(host='127.0.0.1', port=13254, loglevel=logging.INFO)
server.set_fn_new_client(new_client)
server.set_fn_message_received(newMess)

server.run_forever()
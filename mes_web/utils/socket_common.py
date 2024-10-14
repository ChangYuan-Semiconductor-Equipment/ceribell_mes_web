import json
import socket


def client_send(data) -> dict:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.settimeout(0.5)
    server_address = ("127.0.0.1", 8000)
    try:
        sock.connect(server_address)
        sock.sendall(data.encode("UTF-8"))
        response_str = sock.recv(1024).decode("UTF-8")
        response_dict = json.loads(response_str)
        response_dict.update({"state": 1})
    except Exception as e:
        response_dict = {
            "state": -1,
            "message": str(e)
        }
    finally:
        sock.close()

    return response_dict

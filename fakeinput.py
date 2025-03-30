#!/usr/bin/env python3

import socket
import sys
import time

HOST = "0.0.0.0"
PORT = 4953
BUFFER_SIZE = 65536  # 64KB

def log(msg):
    print(f"[faker] {msg}", file=sys.stderr)

def handle_client(conn):
    try:
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            sys.stdout.buffer.write(data)
            sys.stdout.buffer.flush()
    except Exception as e:
        log(f"Stream error: {e}")
    finally:
        conn.close()
        log("Client disconnected")

def main():
    log(f"Listening on port {PORT}")
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
                server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                server.bind((HOST, PORT))
                server.listen(1)
                conn, addr = server.accept()
                log(f"Connected from {addr}")
                handle_client(conn)
        except Exception as e:
            log(f"Server error: {e}")
            time.sleep(1)  # wait before retrying

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import socket
import re

BASE_SRC_PORT = 30000
MAX_WINDOW_SIZE = 65535
MAX_URGENT_PTR = 65535
message_buffer = []

def decode_packet(src_port, payload_data):
    try:
        parts = payload_data.split('|')
        if len(parts) != 4:
            return None

        seq_num = int(parts[0])
        window_size = int(parts[1])
        urgent_ptr = int(parts[2])
        letter = parts[3]

        letter_code = seq_num // 16777216
        letter_from_seq = chr(letter_code)

        if letter == letter_from_seq:
            confidence = "HIGH"
        else:
            confidence = "LOW"

        return {
            'letter': letter,
            'confidence': confidence,
            'seq_letter': letter_from_seq,
            'src_port': src_port
        }
    except Exception as e:
        print(f"Error decoding packet: {e}")
        return None

def start_server(host="127.0.0.1", port=9999):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Listening for covert messages on {host}:{port}...")

    while True:
        conn, addr = server_socket.accept()
        with conn:
            src_port = conn.getpeername()[1]
            data = conn.recv(1024).decode()
            
            if data:
                result = decode_packet(src_port, data)
                if result:
                    message_buffer.append(result['letter'])
                    print(f"Received: {result['letter']} (Confidence: {result['confidence']})")
                    print(f"Current Message: {''.join(message_buffer)}")
                else:
                    print("Decoding failed.")

if __name__ == "__main__":
    start_server()

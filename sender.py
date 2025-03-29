import socket
import sys
import time

irrationals = [
    "3141592653589793",  # pi
    "1618033988749895",  # golden ratio
    "1414213562373095",  # sqrt(2)
    "2718281828459045",  # e
]
pointers = [0, 0, 0, 0]

base_payload = "0123456789"

def resolve_hostname(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        print(f"ERROR: Could not resolve hostname: {hostname}.")
        sys.exit(1)

def generate_payload(letter, letter_index):
    global pointers
    irr_index = letter_index % 4
    irr_str = irrationals[irr_index]
    ptr = pointers[irr_index]
    digit = int(irr_str[ptr])
    pointers[irr_index] = (ptr + 1) % len(irr_str)  
    pos = digit % len(base_payload)  
    payload_list = list(base_payload)
    payload_list[pos] = letter
    sequence_payload = "".join(payload_list)
    return sequence_payload, pos  

def send_covert_message(message, target_hostname, target_port):
    target_ip = resolve_hostname(target_hostname)
    print(f"Sending covert message to {target_ip}:{target_port}")

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)  
        sock.connect((target_ip, target_port))

        for i, letter in enumerate(message):
            seq_payload, pos = generate_payload(letter, i)
            msg_line = f"{i:02d}|{seq_payload}\n"
            sock.sendall(msg_line.encode())
            print(f"Sent letter '{letter}' (index {i}) inserted at position {pos} in payload: {seq_payload}")
            time.sleep(0.2)  

        print("Message transmission complete.")
        sock.close()
    except (socket.error, ConnectionResetError) as e:
        print(f"Connection error: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    message = sys.argv[1] if len(sys.argv) > 1 else "HELLO"
    target_hostname = sys.argv[2] if len(sys.argv) > 2 else "127.0.0.1"
    target_port = int(sys.argv[3]) if len(sys.argv) > 3 else 9999
    send_covert_message(message, target_hostname, target_port)

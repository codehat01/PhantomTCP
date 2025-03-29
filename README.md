# PhantomTCP: An Irrational Number-Based Covert Communication Protocol

## Introduction
PhantomTCP is a covert communication protocol designed to overcome the vulnerabilities of modern secure communication methods. It achieves high detection resistance, efficient throughput, and minimal latency overhead by leveraging irrational number-based transformations. PhantomTCP allows for stealthy data transmission, making it ideal for environments where security and anonymity are paramount.

---

## How It Works
PhantomTCP operates in three main phases:
1. **Carrier Selection**: Identifies suitable packets from network traffic for embedding covert messages.
2. **Message Encoding**: Encodes the message using irrational number-based transformations (π, √2, φ) and modular arithmetic to ensure checksum preservation.
3. **Traffic Injection**: Reintegrates the encoded packets back into the network traffic seamlessly.

The protocol utilizes Scapy for packet manipulation and Flask for implementing a proof-of-concept Tor overlay. With CAIDA dataset analysis, PhantomTCP ensures optimal carrier packet selection and natural traffic flow characteristics.

---

## Features
- **Detection Resistance**: Stealthy encoding avoids detection by Deep Packet Inspection (DPI) and machine learning-based systems.
- **Efficiency**: Maintains up to 89.2% of baseline TCP throughput with only 12.7ms additional latency.
- **Cross-Protocol Compatibility**: Compatible with modern routing infrastructures and adaptable to different network protocols.

---

## Installation
### Prerequisites
- Python 3.x
- Required libraries: Scapy, Flask

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/codehat01/PhantomTCP.git
   ```
2. Navigate to the project directory:
   ```bash
   cd phantomtcp
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
### Sender Script (`sender.py`)
The `sender.py` script encodes a covert message into network traffic:
```bash
python sender.py
```
- **Options**:
  - `-m`: Message to encode.
  - `-i`: Interface for network traffic (optional).

### Receiver Script (`receiver.py`)
The `receiver.py` script decodes the message from network traffic:
```bash
python receiver.py
```
- **Options**:
  - `-i`: Network interface to monitor for covert messages.

### Example
1. Run `receiver.py` on the target machine to start listening.
2. Execute `sender.py` on the sender machine to transmit the covert message.
3. The decoded message will appear on the receiver side.

---

## Testing
1. Use the included test script to verify functionality:
   ```bash
   python test_phantomtcp.py
   ```
2. Evaluate detection resistance and throughput under different network conditions.

---

## Future Enhancements
- **Adaptive Encoding**: Implement dynamic algorithms to adapt to real-time traffic.
- **GAN Integration**: Counteract machine learning-based detection systems.
- **Protocol Expansion**: Extend compatibility to QUIC and HTTP/3 protocols.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
- CAIDA Anonymized Internet Trace Dataset 2022
- Scapy and Flask development communities

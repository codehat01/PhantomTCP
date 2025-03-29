# PhantomTCP: An Irrational Number-Based Covert Communication Protocol

## Introduction
PhantomTCP is a covert communication protocol designed to overcome the vulnerabilities of modern secure communication methods. It achieves high detection resistance, efficient throughput, and minimal latency overhead by leveraging irrational number-based transformations. PhantomTCP allows for stealthy data transmission, making it ideal for environments where security and anonymity are paramount.

---

## How It Works
PhantomTCP operates in three main phases:
1. **Carrier Selection**: Identifies suitable packets from network traffic for embedding covert messages.
2. **Message Encoding**: Encodes the message using irrational number-based transformations (π, √2, φ) and modular arithmetic to ensure checksum preservation.
3. **Traffic Injection**: Reintegrates the encoded packets back into the network traffic seamlessly.
4. **Tor Integration**: Includes a Tor relay server for enhanced anonymity and secure routing.

The protocol utilizes Scapy for packet manipulation and Flask for implementing a proof-of-concept Tor overlay. With CAIDA dataset analysis, PhantomTCP ensures optimal carrier packet selection and natural traffic flow characteristics.

---

## Features
- **Detection Resistance**: Stealthy encoding avoids detection by Deep Packet Inspection (DPI) and machine learning-based systems.
- **Efficiency**: Maintains up to 89.2% of baseline TCP throughput with only 12.7ms additional latency.
- **Cross-Protocol Compatibility**: Compatible with modern routing infrastructures and adaptable to different network protocols.
- **Tor Integration**: Includes integration with Tor for enhanced anonymity and secure routing.

---

## Installation
### Prerequisites
- Python 3.x
- Required libraries: Scapy, Flask
- Tor installed and configured locally

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/codehat01/PhantomTCP.git
   ```
2. Navigate to the project directory:
   ```bash
   cd PhantomTCP
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Install and configure Tor:
   ```bash
   sudo apt install tor -y
   sudo nano /etc/tor/torrc
   ```
   - Uncomment the `SocksPort` line and modify it if necessary.
   - Save and exit the file.
5. Start the Tor service:
   ```bash
   sudo -u debian-tor tor
   ```

---

## Usage
### Sender Script (`sender.py`)
The `sender.py` script encodes a covert message into network traffic:
```bash
python sender.py
```


### Receiver Script (`receiver.py`)
The `receiver.py` script decodes the message from network traffic:
```bash
python receiver.py
```


### Example
1. Configure and start the Tor service as described in the installation steps.
2. Run `receiver.py` on the target machine to start listening.
3. Execute `sender.py` on the sender machine to transmit the covert message.
4. The decoded message will appear on the receiver side, routed securely through the Tor network.


## Future Enhancements
- **Adaptive Encoding**: Implement dynamic algorithms to adapt to real-time traffic.
- **GAN Integration**: Counteract machine learning-based detection systems.
- **Protocol Expansion**: Extend compatibility to QUIC and HTTP/3 protocols.



## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
- CAIDA Anonymized Internet Trace Dataset 2022
- Scapy and Flask development communities
- Tor Project for secure routing solutions


.
# Attack is the best defense

- [Network basics](#network-basics)
- [What is an IP address](#What-is-an-IP-address)
- [TCP/IP protocol](#What-is-TCP-IP)
- [Network sniffing](#Network-sniffing)
- [ARP spoofing](#ARP-spoofing)

# Network basics

## What is a protocol

A network protocol is a set of rules and conventions for communication between network devices, including computers, servers, routers and virtual machines.
These protocols define how data is formatted, transmitted, and processed, ensuring that devices from different manufacturers and with different configurations can communicate effectively.
The OSI (Open Systems Interconnection) model is a conceptual framework used to understand and implement network protocols in seven distinct layers. Each layer serves a specific function and communicates with the layers directly above and below it.Here’s a breakdown of how the OSI model works:
1. ### Physical Layer
**- Function**: Transmits raw bit streams over a physical medium.
**- Protocols and Devices**: Cables, switches, NICs (Network Interface Cards).
**- Examples**: Ethernet cables, fiber optics.
2. ### Data Link Layer
**- Function**: Provides node-to-node data transfer and handles error correction from the physical layer.
**- Protocols and Devices**: MAC (Media Access Control), ARP (Address Resolution Protocol), switches.
**- Examples**: Ethernet, PPP (Point-to-Point Protocol).
3. ### Network Layer
**- Function**: Determines the best physical path for data to reach its destination.
**- Protocols and Devices**: IP (Internet Protocol), routers.
**- Examples**: IPv4, IPv6.
4. ### Transport Layer
**- Function**: Provides reliable data transfer services to the upper layers.
**- Protocols and Devices**: TCP (Transmission Control Protocol), UDP (User Datagram Protocol).
**- Examples**: TCP, UDP.
5. ### Session Layer
**- Function**: Manages sessions between applications. It establishes, manages, and terminates connections.
**- Protocols and Devices**: APIs, sockets.
**- Examples**: NetBIOS, PPTP (Point-to-Point Tunneling Protocol).
6. ### Presentation Layer
**- Function**: Translates data between the application layer and the network format. It handles data encryption - and decryption, compression, and translation.
**- Protocols and Devices**: SSL/TLS (Secure Sockets Layer/Transport Layer Security).
**- Examples**: JPEG, ASCII, EBCDIC.
7. ### Application Layer
**- Function**: Provides network services directly to applications.
**- Protocols and Devices**: HTTP, FTP, SMTP, DNS.
**- Examples**: Web browsers, email clients.

## How the OSI Model Works
**1. Data Encapsulation**: As data moves down from the application layer to the physical layer, each layer adds its own header (and sometimes trailer) to the data. This process is known as encapsulation.
**2. Data Transmission****: At the physical layer, the data is transmitted over the physical medium to the receiving device.
**3. Data Decapsulation****: As data moves up from the physical layer to the application layer in the receiving device, each layer removes its corresponding header (and trailer) to process the data.

### Example of Data Transmission
Sending an Email:

**- Application Layer**: The email application (e.g., Outlook) sends the message using SMTP.
**- Presentation Layer**: The message is encoded to ASCII text.
**- Session Layer**: A session is established between the sending and receiving email servers.
**- Transport Layer**: The message is broken into segments and sent using TCP for reliable delivery.
**- Network Layer**: Each segment is encapsulated into packets with IP addresses.
**- Data Link Layer**: Packets are encapsulated into frames for transmission over Ethernet.
**- Physical Layer**: Frames are converted to electrical signals and transmitted over the network.

Receiving an Email:

**- Physical Layer**: The receiving device gets the electrical signals and converts them into frames.
**- Data Link Layer**: Frames are checked for errors and converted back into packets.
**- Network Layer**: Packets are routed to the appropriate IP address.
**- Transport Layer**: Packets are reassembled into segments and sent to the session layer.
**- Session Layer**: The session is maintained and data is sent to the presentation layer.
**- Presentation Layer**: The data is decoded from ASCII text.
**- Application Layer**: The email application displays the received message.

[other ressource:](https://www.techtarget.com/searchnetworking/definition/protocol)

# What is an IP address

An IP address (Internet Protocol address) is a unique identifier assigned to each device connected to a computer network that uses the Internet Protocol for communication. It serves two main purposes: identifying the host or network interface and providing the location of the host in the network. There are two versions of IP addresses in use: IPv4 and IPv6.

#### IPv4 Address

**- Format**: Consists of four sets of numbers (octets) separated by periods (e.g., 192.168.1.1).
**- Size**: 32 bits, allowing for approximately 4.3 billion unique addresses.
**- Example**: 192.168.0.1
#### IPv6 Address
- **Format**: Consists of eight groups of four hexadecimal digits separated by colons (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334).
**- Size**: 128 bits, allowing for a virtually unlimited number of unique addresses.
**- Example**: 2001:0db8:85a3:0000:0000:8a2e:0370:7334

### Types of IP Addresses
**- Private IP Address**: Used within a private network and not routable on the internet. Examples include 192.168.x.x, 10.x.x.x, and 172.16.x.x to 172.31.x.x.
**- Public IP Address**: Assigned to devices directly connected to the internet and is globally unique.
**- Static IP Address**: Permanently assigned to a device and does not change.
**- Dynamic IP Address**: Temporarily assigned to a device by a DHCP (Dynamic Host Configuration Protocol) server and can change over time.

### IP Address Classes (IPv4)
**- Class A**: 1.0.0.0 to 126.0.0.0 (supports large networks).
**- Class B**: 128.0.0.0 to 191.255.0.0 (supports medium-sized networks).
**- Class C**: 192.0.0.0 to 223.255.255.0 (supports small networks).
**- Class D**: 224.0.0.0 to 239.255.255.255 (reserved for multicast groups).
**- Class E**: 240.0.0.0 to 255.255.255.255 (reserved for future use and research).

### Subnetting
Subnetting is the practice of dividing a network into smaller, more manageable sub-networks (subnets). It helps improve network performance and security. A subnet mask is used to determine the network and host portions of an IP address.
[subnet mask](subnet_mask.png)

### Example: IP Address Breakdown
**- IP Address**: 192.168.1.10
**- Subnet Mask**: 255.255.255.0
**- Network Portion**: 192.168.1.0
**- Host Portion**: 10

### How IP Addresses Work
When a device wants to communicate with another device over the internet or a network:

**1. Address Resolution**: The device uses DNS (Domain Name System) to resolve the domain name (e.g., www.example.com) into an IP address.
**2. Routing**: The data is routed through various intermediate devices (routers) based on the destination IP address.
**3. Packet Delivery**: The data is broken into packets, each containing the source and destination IP addresses. These packets travel independently and may take different paths to reach the destination.
**4. Reassembly**: At the destination, the packets are reassembled into the original message or data.

IP addresses are crucial for the functioning of the internet and computer networks, enabling the identification and location of devices, and ensuring the proper routing and delivery of data.

# what-is-TCP-IP

TCP/IP stands for Transmission Control Protocol/Internet Protocol. TCP/IP is a set of standardized rules that allow computers to communicate on a network such as the internet.  It specifies how data should be packetized, addressed, transmitted, routed, and received. TCP/IP is the foundational protocol suite of the internet and most local area networks (LANs).

## Components of TCP/IP

1. ### Internet Protocol (IP)
**- Function**: Responsible for addressing and routing packets of data so that they can travel across networks and arrive at the correct destination.
**- Versions**: IPv4 and IPv6.
### Key Concepts:
**- IP Address**: A unique identifier for each device on a network.
**- Subnetting**: Dividing a network into smaller sub-networks.
**- Routing**: Determining the best path for data to travel from source to destination.

2. ### Transmission Control Protocol (TCP)
**- Function**: Provides reliable, ordered, and error-checked delivery of data between applications running on hosts communicating via an IP network.
### Key Features:
**- Connection-oriented**: Establishes a connection before transmitting data.
**- Reliable**: Ensures data is delivered accurately and in order.
**- Flow Control**: Manages data transmission rate between sender and receiver.
**- Error Correction**: Detects and retransmits lost or corrupted data.

## Layers of the TCP/IP Model
The TCP/IP model consists of four layers, which correspond closely to layers in the OSI model:

**1.Network Interface Layer (Link Layer):**

**- Equivalent OSI Layers**: Physical and Data Link layers.
**- Function**: Handles the physical transmission of data over a network and includes protocols such as Ethernet and Wi-Fi.

**2. Internet Layer:**

**- Equivalent OSI Layer**: Network layer.
**- Function**: Responsible for addressing, routing, and packaging data for transfer between networks. Key protocols include IP, ICMP (Internet Control Message Protocol), and ARP (Address Resolution Protocol).

**3. Transport Layer:**

**- Equivalent OSI Layer**: Transport layer.
- Function: Provides end-to-end communication services for applications. Key protocols include TCP and UDP (User Datagram Protocol).

4. Application Layer:

**- Equivalent OSI Layers**: Session, Presentation, and Application layers.
**- Function**: Provides network services directly to applications. Protocols include HTTP, FTP, SMTP, and DNS.

## How TCP/IP Works
**1. Application Layer**: An application (e.g., web browser) sends a request to the network.
**2. Transport Layer**: TCP divides the request into packets, adds sequencing and error-checking information, and establishes a connection with the destination.
**3. Internet Layer**: IP handles addressing and routing, ensuring each packet is sent to the correct destination.
**4. Network Interface Layer**: The packets are transmitted over the physical network (e.g., Ethernet cable, Wi-Fi).

On the receiving end:

**1. Network Interface Layer**: Receives the packets from the network.
**2. Internet Layer**: IP checks the addressing and routes the packets to the appropriate destination.
**3. Transport Layer**: TCP reassembles the packets in the correct order and checks for errors.
**4. Application Layer**: The application processes the data and presents it to the user.

## Example of TCP/IP in Action
**- Web Browsing**: When you enter a URL in a web browser:
**1. HTTP (Application Layer)**: The browser sends an HTTP request.
**2. TCP (Transport Layer)**: TCP divides the HTTP request into segments and establishes a connection with the web server.
**3. IP (Internet Layer)**: IP addresses and routes the segments to the web server.
**4. Ethernet/Wi-Fi (Network Interface Layer)**: The segments are transmitted over the internet.
**5. Reverse Process**: The web server processes the request, sends the response back, and the browser displays the webpage.

TCP/IP is essential for internet and network communications, providing a reliable and standardized way for devices to exchange data.

# Network-sniffing

## Definition
**1.** Wireshark is an open-source application that captures and displays data traveling back and forth on a network.
**2.** Network sniffing, also known as packet sniffing, is a technique used to monitor and capture data packets traveling over a network. This can be done for legitimate purposes such as network troubleshooting and performance monitoring, or for malicious activities like eavesdropping on communications to steal sensitive information.

Key points about network sniffing include:

**1. Tools:** There are various software tools available for sniffing, such as [Wireshark](https://www.lifewire.com/wireshark-tutorial-4143298), tcpdump, and Ettercap.
**2. Promiscuous Mode:** Network interface cards (NICs) are often set to promiscuous mode to capture all packets on the network segment, not just those addressed to the NIC.
**3. Legitimate Uses:** Network administrators use sniffers to diagnose network problems, ensure network security, and monitor network performance.
**4. Malicious Uses:** Attackers can use sniffers to capture sensitive information like usernames, passwords, and credit card numbers from network traffic.
**5. Detection:** Detecting sniffers on a network can be challenging but not impossible. Methods include sending non-broadcast packets and monitoring for network interface cards in promiscuous mode.

## How Network Sniffing Works

Network sniffing involves placing a network interface card [(NIC)](https://www.lifewire.com/definition-of-nic-817866) into promiscuous mode, which allows it to capture all packets on the network segment, regardless of their intended destination. Specialized software tools, such as Wireshark, tcpdump, and Ettercap, are then used to collect and analyze these packets. 

To prevent unauthorized sniffing, network administrators should implement encryption protocols (e.g., SSL/TLS), use secure authentication methods, and regularly monitor network traffic for anomalies.

Understanding network sniffing is essential for maintaining the security and integrity of network communications, whether for protecting against threats or ensuring smooth network operations.

# ARP-spoofing

## Introduction
ARP (Address Resolution Protocol) spoofing, also known as ARP poisoning, is a type of attack in which a malicious actor sends falsified ARP messages over a local area network. This results in the attacker’s MAC address being associated with the IP address of another device (e.g., the default gateway), causing any traffic meant for that IP address to be sent to the attacker instead. This enables the attacker to intercept, modify, or block communication between devices on the network.

## How ARP Spoofing Works

[ARP Spoofing](arp_spoofing.png)

**1. ARP Basics:** ARP is a protocol used for mapping an IP address to a physical machine (MAC) address in a local network. When a device wants to communicate with another device on the same network, it uses ARP to find the MAC address associated with the destination IP address.
**2. Spoofing Process:**
    **Step 1:** The attacker sends ARP reply packets containing fake MAC addresses to the target devices on the network. These packets claim that the attacker's MAC address should be associated with the IP address of a legitimate device (e.g., the default gateway or another target device).
    **Step 2:** The target devices update their ARP cache with the incorrect information, causing them to send traffic intended for the legitimate device to the attacker's machine instead.


## Effects and Risks
The effects of ARP spoofing attacks can have serious implications for enterprises. In their most basic application, ARP spoofing attacks are used to steal sensitive information. Beyond this, ARP spoofing attacks are often used to facilitate other attacks such as:
**- Man-in-the-Middle Attacks:** The attacker can intercept and potentially modify the data passing between two devices. This can include sensitive information such as login credentials, credit card numbers, and personal communications.
**- Denial of Service (DoS):** By associating their MAC address with multiple IP addresses, an attacker can disrupt the normal traffic flow in the network, effectively causing a DoS.
**- Session Hijacking:** The attacker can take over an active session by intercepting session cookies and tokens.

## Detection and Prevention
**- Static ARP Entries:** Configure static ARP entries for critical devices on the network to prevent ARP spoofing attacks.
**- ARP Inspection:** Implement Dynamic ARP Inspection (DAI) on network switches to validate ARP packets.
Encryption: Use encrypted communication protocols (e.g., HTTPS, SSH) to protect data even if it is intercepted.
**- Monitoring Tools:** Employ network monitoring tools to detect unusual ARP traffic and changes in MAC address mappings.

ARP spoofing is a serious security threat that can compromise the confidentiality and integrity of network communications. By understanding how it works and implementing appropriate countermeasures, network administrators can protect their networks from such attacks.


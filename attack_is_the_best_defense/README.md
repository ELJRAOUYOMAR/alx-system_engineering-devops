.
# Attack is the best defense

- [Network basics](#network-basics)
- [What is an IP address](#What-is-an-IP-address)
# Network basics

## What is a protocol

A network protocol is a set of rules and conventions for communication between network devices, including computers, servers, routers and virtual machines.
These protocols define how data is formatted, transmitted, and processed, ensuring that devices from different manufacturers and with different configurations can communicate effectively.
The OSI (Open Systems Interconnection) model is a conceptual framework used to understand and implement network protocols in seven distinct layers. Each layer serves a specific function and communicates with the layers directly above and below it.Here’s a breakdown of how the OSI model works:
1. ### Physical Layer
- Function: Transmits raw bit streams over a physical medium.
- Protocols and Devices: Cables, switches, NICs (Network Interface Cards).
- Examples: Ethernet cables, fiber optics.
2. ### Data Link Layer
- Function: Provides node-to-node data transfer and handles error correction from the physical layer.
- Protocols and Devices: MAC (Media Access Control), ARP (Address Resolution Protocol), switches.
- Examples: Ethernet, PPP (Point-to-Point Protocol).
3. ### Network Layer
- Function: Determines the best physical path for data to reach its destination.
- Protocols and Devices: IP (Internet Protocol), routers.
- Examples: IPv4, IPv6.
4. ### Transport Layer
- Function: Provides reliable data transfer services to the upper layers.
- Protocols and Devices: TCP (Transmission Control Protocol), UDP (User Datagram Protocol).
- Examples: TCP, UDP.
5. ### Session Layer
- Function: Manages sessions between applications. It establishes, manages, and terminates connections.
- Protocols and Devices: APIs, sockets.
- Examples: NetBIOS, PPTP (Point-to-Point Tunneling Protocol).
6. ### Presentation Layer
- Function: Translates data between the application layer and the network format. It handles data encryption - and decryption, compression, and translation.
- Protocols and Devices: SSL/TLS (Secure Sockets Layer/Transport Layer Security).
- Examples: JPEG, ASCII, EBCDIC.
7. ### Application Layer
- Function: Provides network services directly to applications.
- Protocols and Devices: HTTP, FTP, SMTP, DNS.
- Examples: Web browsers, email clients.

## How the OSI Model Works
1. Data Encapsulation: As data moves down from the application layer to the physical layer, each layer adds its own header (and sometimes trailer) to the data. This process is known as encapsulation.
2. Data Transmission: At the physical layer, the data is transmitted over the physical medium to the receiving device.
3. Data Decapsulation: As data moves up from the physical layer to the application layer in the receiving device, each layer removes its corresponding header (and trailer) to process the data.

### Example of Data Transmission
Sending an Email:

- Application Layer: The email application (e.g., Outlook) sends the message using SMTP.
- Presentation Layer: The message is encoded to ASCII text.
- Session Layer: A session is established between the sending and receiving email servers.
- Transport Layer: The message is broken into segments and sent using TCP for reliable delivery.
- Network Layer: Each segment is encapsulated into packets with IP addresses.
- Data Link Layer: Packets are encapsulated into frames for transmission over Ethernet.
- Physical Layer: Frames are converted to electrical signals and transmitted over the network.

Receiving an Email:

- Physical Layer: The receiving device gets the electrical signals and converts them into frames.
- Data Link Layer: Frames are checked for errors and converted back into packets.
- Network Layer: Packets are routed to the appropriate IP address.
- Transport Layer: Packets are reassembled into segments and sent to the session layer.
- Session Layer: The session is maintained and data is sent to the presentation layer.
- Presentation Layer: The data is decoded from ASCII text.
- Application Layer: The email application displays the received message.

[other ressource:](https://www.techtarget.com/searchnetworking/definition/protocol)

# What is an IP address

An IP address (Internet Protocol address) is a unique identifier assigned to each device connected to a computer network that uses the Internet Protocol for communication. It serves two main purposes: identifying the host or network interface and providing the location of the host in the network. There are two versions of IP addresses in use: IPv4 and IPv6.

#### IPv4 Address

- Format: Consists of four sets of numbers (octets) separated by periods (e.g., 192.168.1.1).
- Size: 32 bits, allowing for approximately 4.3 billion unique addresses.
- Example: 192.168.0.1
#### IPv6 Address
- Format: Consists of eight groups of four hexadecimal digits separated by colons (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334).
- Size: 128 bits, allowing for a virtually unlimited number of unique addresses.
- Example: 2001:0db8:85a3:0000:0000:8a2e:0370:7334

### Types of IP Addresses
- Private IP Address: Used within a private network and not routable on the internet. Examples include 192.168.x.x, 10.x.x.x, and 172.16.x.x to 172.31.x.x.
- Public IP Address: Assigned to devices directly connected to the internet and is globally unique.
- Static IP Address: Permanently assigned to a device and does not change.
- Dynamic IP Address: Temporarily assigned to a device by a DHCP (Dynamic Host Configuration Protocol) server and can change over time.

### IP Address Classes (IPv4)
- Class A: 1.0.0.0 to 126.0.0.0 (supports large networks).
- Class B: 128.0.0.0 to 191.255.0.0 (supports medium-sized networks).
- Class C: 192.0.0.0 to 223.255.255.0 (supports small networks).
- Class D: 224.0.0.0 to 239.255.255.255 (reserved for multicast groups).
- Class E: 240.0.0.0 to 255.255.255.255 (reserved for future use and research).

### Subnetting
Subnetting is the practice of dividing a network into smaller, more manageable sub-networks (subnets). It helps improve network performance and security. A subnet mask is used to determine the network and host portions of an IP address.

### Example: IP Address Breakdown
- IP Address: 192.168.1.10
- Subnet Mask: 255.255.255.0
- Network Portion: 192.168.1.0
- Host Portion: 10

### How IP Addresses Work
When a device wants to communicate with another device over the internet or a network:

1. Address Resolution: The device uses DNS (Domain Name System) to resolve the domain name (e.g., www.example.com) into an IP address.
2. Routing: The data is routed through various intermediate devices (routers) based on the destination IP address.
3. Packet Delivery: The data is broken into packets, each containing the source and destination IP addresses. These packets travel independently and may take different paths to reach the destination.
4. Reassembly: At the destination, the packets are reassembled into the original message or data.

IP addresses are crucial for the functioning of the internet and computer networks, enabling the identification and location of devices, and ensuring the proper routing and delivery of data.



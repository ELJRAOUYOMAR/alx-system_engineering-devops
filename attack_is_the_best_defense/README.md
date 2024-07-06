.
# Attack is the best defense

- [Network basics](#network-basics)

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
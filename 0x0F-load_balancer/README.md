# Load balancer.

- [Load balancing](#load-balancing)
-   [Introduction to load balancing](#introduction-to-load-balancing)
-   [Key Benefits of Load Balancing](#Key-Benefits-of-Load-Balancing)
-   [Types of Load Balancing Algorithms](#Types-of-Load-Balancing-Algorithms)
-   [Hardware and software load balancers](https://www.thegeekstuff.com/2016/01/load-balancer-intro/)
-   [Setting Up HAProxy](#Setting-Up-HAProxy)
- [HAProxy](#HAProxy)
-   [Introduction](#introduction)
-   [Key Features of HAProxy][#Key-Features-of-HAProxy]
-   [Basic HAProxy Configuration](#Basic-HAProxy-Configuration)
-   [HAProxy Terminology](#HAProxy-Terminology)

# load-balancing

## introduction to load balancing

![load balancing concept](imgs/load_balancer.png)
Load balancing is a technique used to distribute incoming network traffic across multiple servers to ensure no single server becomes overwhelmed with too much traffic. This improves the responsiveness and availability of applications, websites, and databases.

## Key Benefits of Load Balancing
**1. Increased Availability and Reliability:** By distributing the traffic, the load balancer ensures that if one server fails, the others can take over.
**2. Scalability:** Load balancers can handle increased traffic by adding more servers.
**3. Efficient Resource Utilization:** Traffic is evenly distributed, preventing server overload and ensuring resources are used effectively.
**4. Improved Performance:** Balancing the load can reduce response times and increase throughput.

## Types of Load Balancing Algorithms
**1. Round Robin:** Distributes requests sequentially to each server.
This algorithm is used when servers are of equal specification and there not much persistent connections.
```sh
Client 1 -> Server A
Client 2 -> Server B
Client 3 -> Server C
Client 4 -> Server A
```
![round robin 1](imgs/round_robin.png)

**2. Least Connections:** Sends requests to the server with the fewest active connections.
```sh Server A: 2 connections
Server B: 3 connections
Client -> Server A
```
![least connection 1](imgs/least_connection.png)
![least connection 2](imgs/Least-Connections-2.gif)

**3. IP Hash:** Uses the client’s IP address to determine which server will receive the request
```sh
Client IP 192.168.1.1 -> Server A
Client IP 192.168.1.2 -> Server B
```
![IP Hash](imgs/IP-Hash.gif)

**4. Weighted Round Robin:** Assigns weights to each server based on their capacity and directs more traffic to higher-capacity servers.
```sh
Server A (weight 2): 2 requests
Server B (weight 1): 1 request
```
![round robin 2](imgs/round_robin_1.gif)

there is hardware and software load balancer, chack here [hardware load balancer and software load balancer](https://www.thegeekstuff.com/2016/01/load-balancer-intro/)

# HAProxy 

## introduction
HAProxy (High Availability Proxy) is a free, open-source software that provides a high availability load balancer and proxy server for TCP and HTTP-based applications. It's known for its performance, reliability, and advanced features.

```sh
                Client Requests
                        |
                        v
                +---------------------+
                |     HAProxy         |
                | +-----------------+ |
                | | Frontend (Port) | |
                | +--------+--------+ |
                |          |          |
                | +--------+--------+ |
                | | Backend (Servers)| |
                | +---+-------+---+---+ |
                |     |       |       |
                +-----|-------|-------+
                    |       |       |
                +-----+-----+ +-----+-----+
                |  Server 1  | |  Server 2  |
                +------------+ +------------+
```

## Key Features of HAProxy
**1. Load Balancing:** Supports various algorithms, including round robin, least connections, and more.
**2. High Availability:** Monitors server health and can automatically reroute traffic if a server fails.
**3. SSL Termination:** Can handle SSL/TLS encryption and decryption.
**4. Compression:** Supports HTTP compression to reduce the size of transmitted data.
**5. Security:** Provides features like rate limiting, access control lists (ACLs), and DoS attack mitigation.
**6. Logging and Monitoring:** Detailed logging and metrics for monitoring traffic and server health.

# HAProxy Terminology
There are many terms and concepts that are important when discussing load balancing and proxying. You’ll go over commonly used terms in the following subsections.
Before you get into the basic types of load balancing, you should begin with a review of ACLs, backends, and frontends.
### Access Control List (ACL)
Access Control Lists (ACLs) in HAProxy are used to define rules for controlling traffic based on various criteria. ACLs allow you to inspect, filter, and route traffic based on different attributes of the requests, such as source IP address, URL path, HTTP headers, and more.

```sh
            Client Requests
                        |
                        v
                    +------------+
                    |   HAProxy  |
                    |  +--------+|
                    |  |  ACL   ||
                    |  +----+---+|
                    |       |    |
            +-------+-------+------+--------+
            | Match Criteria 1  |  Match Criteria 2 |
            +-------+-------+------+--------+
                    |                      |
            Action (Allow, Deny, Redirect)  Action (Allow, Deny, Redirect)
```

#### Basic ACL Syntax 
```sh
acl <name> <condition>
```

#### Example 1: Allowing Traffic from Specific IPs
```sh
frontend http_front
    bind *:80

    acl allowed_ips src 192.168.1.0/24
    acl allowed_ips src 10.0.0.0/8

    http-request deny if !allowed_ips

    default_backend http_back
```
In this example:

- acl allowed_ips src 192.168.1.0/24 and acl allowed_ips src 10.0.0.0/8 define two ACLs that match requests coming from specific IP ranges.
- http-request deny if !allowed_ips denies requests that do not match the allowed_ips ACLs.

#### Example 2: Redirecting Based on URL Path
```sh
frontend http_front
    bind *:80

    acl is_admin_path path_beg /admin
    acl is_user_path path_beg /user

    use_backend admin_back if is_admin_path
    use_backend user_back if is_user_path

    default_backend http_back
```

In this example:

- acl is_admin_path path_beg /admin defines an ACL that matches requests with URLs starting with /admin.
- acl is_user_path path_beg /user defines an ACL that matches requests with URLs starting with /user.
- use_backend admin_back if is_admin_path routes requests matching the is_admin_path ACL to the admin_back backend.
- use_backend user_back if is_user_path routes requests matching the is_user_path ACL to the user_back backend.

#### Example 3: Restricting Access Based on HTTP Method
```sh
frontend http_front
    bind *:80

    acl is_post_method method POST
    acl is_put_method method PUT

    http-request deny if is_post_method
    http-request deny if is_put_method

    default_backend http_back
```
In this example:

- acl is_post_method method POST defines an ACL that matches requests using the POST method.
- acl is_put_method method PUT defines an ACL that matches requests using the PUT method.
- http-request deny if is_post_method denies requests matching the is_post_method ACL.
- http-request deny if is_put_method denies requests matching the is_put_method ACL.

ACLs in HAProxy provide a powerful mechanism to control and filter traffic based on various criteria. By using ACLs, you can create complex traffic routing and filtering rules to meet your specific needs, improving security, performance, and flexibility in handling requests.

### backend









## Basic HAProxy Configuration

A simple HAProxy configuration might look like this:
```sh
global
    log /dev/log local0
    log /dev/log local1 notice
    chroot /var/lib/haproxy
    stats socket /run/haproxy/admin.sock mode 660 level admin
    stats timeout 30s
    user haproxy
    group haproxy
    daemon

defaults
    log     global
    mode    http
    option  httplog
    option  dontlognull
    timeout connect 5000
    timeout client  50000
    timeout server  50000

frontend http_front
    bind *:80
    default_backend http_back

backend http_back
    balance roundrobin
    server server1 192.168.1.1:80 check
    server server2 192.168.1.2:80 check
```

## Setting Up HAProxy

1. Install HAProxy:
```sh
sudo apt-get update
sudo apt-get install haproxy
```
2. Configure HAProxy:
Edit the HAProxy configuration file (/etc/haproxy/haproxy.cfg) with the desired settings.
3. Start HAProxy:
sudo systemctl start haproxy
sudo systemctl enable haproxy
4. Check Status:
```sh
sudo systemctl status haproxy
```
HAProxy is a powerful tool for managing traffic, ensuring high availability, and enhancing the performance of web applications. It is widely used in production environments due to its robustness and extensive feature set.


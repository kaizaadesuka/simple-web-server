# Computer Networks (CII2J4) Final Project: Simple Web Server

Group members:

- Kaisar Kertarajasa

- Satya Rayyis Baruna

- Nadim Rafli Hamzah

## Introduction

In this project, we are making a simple web server written in Python, running on a FreeBSD virtual machine. Here, we are going to demonstrate a network communication between two hosts (Linux desktop and a FreeBSD guest VM) using TCP connection. The Linux desktop acts as a client while the FreeBSD guest VM acts as the server to handle client's request.

## Why FreeBSD

There are several reason why do we choose FreeBSD as our server operating system:

- FreeBSD is a free and open source operating system, which complies to our project requirement that insist for the usage of free and open-source technologies

- FreeBSD is a lightweight operating system so that it does not utilize too much system resources so it can run smoothly in our virtual machine without giving excessive load to the host system

- FreeBSD is a stable, mature, and robust operating system which makes it suitable for a server operating system with good performance and security.

- FreeBSD is well documented. The documentation can be read on the <a href='https://docs.freebsd.org/en/books/handbook/'>FreeBSD handbook</a>.

For more information about FreeBSD, please refer to <a href='https://www.freebsd.org/'>its official website</a>. 

## Python for Server Programming

Python is used to program the server as its ease of learning and compatibility on multiple platforms. Python has a plethora of library and frameworks, including a `socket` library to make TCP connection between client and server possible. Using Python, a consise, lightweight, simple web server program can be made.

## Preparation

1. First, we have to install FreeBSD in a virtual machine. This time, we are using VirtualBox to do this task.

2. Install the operating system. In this documentation, we are not going to discuss FreeBSD installation in depth. Make sure to follow every step of installation. If you are on doubt, you may choose the default option, or please refer to installation guide.
    
    note: Make sure IPv4 and DHCP connection is enabled for the system.
    
3. To establish connection between host machine to the guest VM, 

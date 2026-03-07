# SnapCast

Gesture-based screenshot sharing between Macs over a local network.

SnapCast is a prototype that explores gesture-driven device interaction inspired by seamless sharing features such as Huawei Share. The project demonstrates how computer vision and peer-to-peer networking can be combined to create a simple gesture-controlled screenshot sharing workflow between devices on the same LAN.

---

## Demo


https://github.com/user-attachments/assets/2e30fcbc-63f4-4dbf-a5ab-3322e07c8b25


---

## Overview

SnapCast enables gesture-triggered screenshot sharing without relying on cloud services. Using computer vision for gesture detection and a lightweight peer-to-peer networking architecture, the system allows one device to capture and broadcast a screenshot while another device retrieves it using a corresponding gesture.

---

## Features

- Gesture-triggered screenshot capture  
- Local network device discovery using UDP broadcast  
- Peer-to-peer file transfer using TCP sockets  
- Computer vision based gesture detection using MediaPipe and OpenCV  
- No external servers or cloud services required  

---

## Architecture

SnapCast follows a simple peer-to-peer communication model.

Sender (Mac A):

1. Detect grab gesture  
2. Capture screenshot  
3. Broadcast screenshot metadata over LAN  
4. Start TCP file server  

Receiver (Mac B):

1. Listen for broadcast messages  
2. Store screenshot metadata  
3. Detect receive gesture  
4. Connect to sender and download screenshot  

---

## Installation

Clone the repository:

```bash
git clone https://github.com/zeeshan2k2/SnapCast.git
cd SnapCast
```

Create a virtual environment:

```bash
python3.11 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Start the receiver on one machine:

```bash
python listener.py
```

Start the sender on the other machine:

```bash
python main.py
```

Workflow:

1. Perform a **grab gesture** on the sender device to capture a screenshot.
2. Perform a **receive gesture** on the receiver device.
3. The screenshot will be downloaded automatically.

---

## Requirements

- Python 3.11
- OpenCV
- MediaPipe
- Two devices connected to the same local network

# SDLockV0.1 [Prototype]
---
## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [System Design](#system-design)
6. [Model Architecture](#model-architecture)
7. [Dataset](#dataset)
8. [Results and Evaluation](#results-and-evaluation)
9. [Future Work](#future-work)
10. [Contributing](#contributing)
11. [License](#license)
12. [Contact](#contact)
---
## Introduction
<p align="justify">
This project presents a smart door lock system based on facial recognition. It uses MTCNN for face detection and InceptionResNetV1 for feature embedding. A custom anti-spoofing model named DualInputCNN enhances security by verifying face authenticity using both RGB and LBP image inputs.
</p>

## Features
- Face detection and recognition
- Anti-spoofing with dual-input CNN
- Real-time access control
- Servo motor integration
- Cloud-connected recognition via Google Colab and ngrok

## Installation
- Python 3.7+
- Raspberry Pi OS + Thonny
- Google Colab for model inference
- Dependencies: facenet-pytorch, flask, opencv-python, torch, ngrok, etc.
<p align="justify">
A complete step-by-step setup will be provided for Raspberry Pi and Colab.
</p>

## Usage
- Register face using raspberry_pi_register_face.py
- Run face recognition with raspberry_pi_face_recognition.py
- Server-side face verification runs in Colab via colab_face_recognition.py
- If face is real and matched, servo unlocks the door for 5 seconds

## System Design
<p align="center">
    <img width="1000" src="https://github.com/AlvinOctaH/FRdoorlock-MNV2.3/blob/main/assets/SmartDoorLock.png" alt="result_training_test">
</p>
<p align="justify">
The system consists of three core components: Raspberry Pi (servo + webcam), a cloud-based server (Colab), and a client-server connection via REST API. The camera captures images and sends them to the server, which processes recognition and returns the access status.
</p>

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

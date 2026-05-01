# AI Wildlife Threat Detection Using YOLOv8

## Project Overview

AI Wildlife Threat Detection Using YOLOv8 is a real-time intelligent surveillance solution developed to detect wildlife animals and generate threat-based alerts automatically. The system uses a custom-trained YOLOv8 deep learning object detection model to identify animals such as eagle, tiger, elephant, and snake through live webcam feed.

Depending on the detected animal, the system classifies the threat level into Safe, Warning, or Danger and produces corresponding visual as well as audio alerts. This project aims to reduce human-wildlife conflicts and support environmental safety monitoring through artificial intelligence.

---

## Problem Statement

Conventional wildlife monitoring systems depend heavily on manual observation, which is inefficient and often fails to provide instant alerts during dangerous wildlife encounters. There is a need for an automated computer vision-based system that can identify wildlife species in real time and notify users immediately based on the threat severity.

---

## Proposed Solution

This project implements:

* Custom YOLOv8 object detection model
* Real-time webcam based inference
* Bounding box visualization
* Animal threat categorization
* Automatic warning and danger audio alert generation
* Lightweight deployment on standard systems

---

## Animal Categories and Threat Levels

| Animal   | Threat Level | Alert         |
| -------- | ------------ | ------------- |
| Eagle    | Safe         | No Alert      |
| Tiger    | Warning      | Warning Audio |
| Elephant | Danger       | Danger Audio  |
| Snake    | Danger       | Danger Audio  |

---

## Tech Stack Used

* Python
* OpenCV
* PyTorch
* Ultralytics YOLOv8
* Pygame
* Google Colab
* Roboflow
* Makesense.ai

---

## Project Workflow

1. Dataset Collection using Roboflow
2. Image Annotation using Makesense.ai
3. Custom Dataset Preparation
4. YOLOv8 Model Training on Google Colab
5. Exporting best.pt model
6. Real-time Webcam Detection using OpenCV
7. Audio Alert Generation using Pygame

---

## Model Performance

* Precision : 0.698
* Recall : 0.706
* mAP@0.5 : 0.805
* mAP@0.5:0.95 : 0.449

The model demonstrated high detection performance for elephant and tiger classes and acceptable performance for eagle and snake classes under real-time scenarios.

---

## Future Enhancements

* Mobile App Notification System
* IoT Sensor Integration
* Edge Device Deployment
* Cloud Alert Logging
* Multi Animal Species Expansion

---

## Author

**Bhanu G**
B.Sc Data Science
Maharani Cluster University

---

## Conclusion

This AI-powered wildlife monitoring solution demonstrates how computer vision and deep learning can be leveraged to build real-time environmental safety applications. The project is scalable, efficient, and capable of assisting in early wildlife threat detection.

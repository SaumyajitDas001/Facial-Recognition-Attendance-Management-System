# Facial-Recognition-Attendance-Management-System

A Face Attendance Monitoring System uses LBPH (Local Binary Patterns Histogram) and Haar Cascade algorithms for efficient and accurate face recognition. LBPH is a robust machine learning algorithm that analyzes local patterns in an image, converts them into binary values, and compares histograms for face matching, handling variations in lighting and angles effectively. The Haar Cascade algorithm detects faces by scanning video frames with a cascade of classifiers trained on positive and negative images. Detected face regions are resized, converted to grayscale, and normalized for consistency before being passed to the LBPH recognizer. Matched faces are identified and their attendance is logged with a timestamp in a database. This system is ideal for automated attendance in schools, offices, and secure access systems, providing a fast, contactless, and reliable solution.

A **Face Attendance Monitoring System** using **LBPH (Local Binary Patterns Histogram) Face Recognizer** and the **Haar Cascade Algorithm** typically works as follows:

### Components:
1. **LBPH Face Recognizer**:
   - LBPH is a machine learning algorithm used to recognize faces.
   - It works by analyzing the local patterns in an image, converting it into binary values, and comparing histograms of these patterns for face matching.
   - It is robust for real-time face recognition and handles variations in lighting and angles effectively.

2. **Haar Cascade Algorithm**:
   - A Haar Cascade is an object detection algorithm used to detect faces in an image or video.
   - It uses a cascade of classifiers trained on positive and negative images of faces, scanning frames to detect face regions quickly.

### Workflow:
1. **Face Detection (Using Haar Cascade)**:
   - Video frames are captured using a camera.
   - The Haar Cascade classifier identifies and isolates the face region in each frame.

2. **Face Preprocessing**:
   - Detected face regions are resized, converted to grayscale, and normalized for consistent processing.

3. **Face Recognition (Using LBPH)**:
   - The preprocessed face is passed to the LBPH face recognizer.
   - LBPH compares the extracted features with a trained database of registered faces.
   - If a match is found, the system identifies the individual.

4. **Attendance Marking**:
   - When a face is recognized, the person's attendance is recorded with their ID and timestamp in a database.

5. **Output**:
   - Displays recognized faces in real-time.
   - Updates attendance logs in a file (e.g., CSV, SQL database).

### Applications:
- Automated attendance in schools, colleges, and offices.
- Secure entry systems.
- Visitor management systems.

This system ensures a quick, efficient, and contactless attendance process while maintaining high accuracy.

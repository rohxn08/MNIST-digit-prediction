# MNIST Digit Prediction

This project is a graphical user interface (GUI) application that allows users to draw digits (0-9) on a canvas and uses a Convolutional Neural Network (CNN) to predict the drawn digit.

## Features
- **Interactive Canvas**: Draw digits using your mouse.
- **Real-time Prediction**: Click "Predict Digit" to see the model's classification and confidence score.
- **Clear Functionality**: Easily clear the canvas to draw a new digit.

## Prerequisites
- Python 3.x
- Virtual Environment (recommended)

## Setup and Installation

1.  **Create a Virtual Environment** (if not already created):
    ```bash
    python -m venv venv
    ```

2.  **Activate the Virtual Environment**:
    *   **Windows (PowerShell)**:
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```
    *   **Windows (CMD)**:
        ```cmd
        .\venv\Scripts\activate.bat
        ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *Note: This project requires TensorFlow. Ensure you have sufficient disk space (approx. 1-2 GB free) for the installation.*

## Usage

1.  Run the application:
    ```bash
    python s1.py
    ```
2.  A window titled "Digit Recognition" will appear.
3.  Draw a digit in the white box.
4.  Click **Predict Digit** to see the result.
5.  Click **Clear** to reset the canvas.

## Files
- `s1.py`: The main Python script containing the GUI and prediction logic.
- `model.h5`: The pre-trained Keras/TensorFlow model used for prediction.
- `requirements.txt`: List of Python dependencies.

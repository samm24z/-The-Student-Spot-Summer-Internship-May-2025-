# CNN-based Digit Recognition with Keras and MNIST

This project demonstrates how to build and train a Convolutional Neural Network (CNN) using Keras for handwritten digit classification on the MNIST dataset.

## Table of Contents

* [Introduction](#introduction)
* [Dataset](#dataset)
* [Model Architecture](#model-architecture)
* [Training and Evaluation](#training-and-evaluation)
* [Results](#results)
* [Project Structure](#project-structure)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [Running the Project](#running-the-project)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

## Introduction

Handwritten digit recognition is a foundational task in deep learning and computer vision. This project provides a practical implementation of a Convolutional Neural Network (CNN) using the Keras API (built on TensorFlow) to accurately classify handwritten digits from the well-known MNIST dataset. The CNN architecture is particularly well-suited for image-based tasks, leveraging convolutional layers to learn spatial hierarchies of features.

The objective is to develop a robust model that can take a `28x28` grayscale image of a handwritten digit (0-9) and predict its correct numerical value.

## Dataset

The **MNIST (Modified National Institute of Standards and Technology) database** is a standard benchmark dataset for image classification. It comprises:

* **60,000 training images** and their corresponding labels.
* **10,000 testing images** and their corresponding labels.

Each image is a `28x28` pixel grayscale image, representing a single handwritten digit from 0 to 9. The dataset is conveniently available directly through Keras.

## Model Architecture

The neural network is a Convolutional Neural Network (CNN) defined using Keras's Sequential API. It consists of the following layers:

1.  **Conv2D Layer:**
    * Filters: 28
    * Kernel Size: (3, 3)
    * Activation: `relu`
    * Input Shape: (28, 28, 1) - corresponding to 28x28 pixel grayscale images.
2.  **MaxPooling2D Layer:**
    * Pool Size: (2, 2) - reduces the spatial dimensions of the feature maps.
3.  **Flatten Layer:**
    * Converts the 2D feature maps into a 1D vector, preparing the data for dense layers.
4.  **Dense Layer (Hidden Layer):**
    * Units: 128
    * Activation: `relu`
5.  **Dropout Layer:**
    * Rate: 0.2 - randomly sets a fraction of input units to 0 at each update during training, which helps prevent overfitting.
6.  **Dense Layer (Output Layer):**
    * Units: 10 (one for each digit 0-9)
    * Activation: `softmax` - outputs a probability distribution over the 10 classes.

## Training and Evaluation

The model is compiled with:

* **Optimizer:** `adam` - an efficient stochastic optimization algorithm.
* **Loss Function:** `sparse_categorical_crossentropy` - suitable for multi-class classification when labels are integers (not one-hot encoded).
* **Metrics:** `accuracy` - to monitor the classification accuracy during training and evaluation.

The model was trained for **10 epochs** using the `train_X` and `train_Y` data, with performance monitored on the `test_X` and `test_Y` data for validation.

## Results

The training process showed consistent improvement in accuracy and reduction in loss.

| Epoch | Training Loss | Training Accuracy | Validation Loss | Validation Accuracy |
| :---- | :------------ | :---------------- | :-------------- | :------------------ |
| 1     | 0.5375        | 0.9036            | 0.1201          | 0.9659              |
| 2     | 0.1245        | 0.9634            | 0.0990          | 0.9723              |
| 3     | 0.0962        | 0.9716            | 0.0739          | 0.9779              |
| 4     | 0.0771        | 0.9764            | 0.0893          | 0.9752              |
| 5     | 0.0670        | 0.9802            | 0.0732          | 0.9807              |
| 6     | 0.0552        | 0.9833            | 0.0757          | 0.9797              |
| 7     | 0.0477        | 0.9861            | 0.0831          | 0.9795              |
| 8     | 0.0424        | 0.9870            | 0.0839          | 0.9801              |
| 9     | 0.0379        | 0.9883            | 0.1183          | 0.9813              |
| 10    | 0.0362        | 0.9894            | 0.0974          | 0.9808              |

The final evaluation on the test set yielded an **accuracy of approximately 98.08%**. The included plot in the notebook visualizes the training and validation accuracy over epochs.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Make sure you have the following installed:

* Python 3.7+
* pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/samm24z/The-Student-Spot-Summer-Internship-May-2025/tree/main/Task_4 
    cd The-Student-Spot-Summer-Internship-May-2025 
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```
3.  **Activate the virtual environment:**
    * **On Windows (Command Prompt/PowerShell):**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
4.  **Install the required packages:**
    ```bash
    pip install tensorflow keras numpy matplotlib jupyter
    ```

### Running the Project

1.  **Start Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
2.  **Open `CnnModel_Mnist.ipynb`:**
    In the Jupyter interface that opens in your browser, navigate to and open `CnnModel_Mnist.ipynb`.
3.  **Run all cells:**
    Execute all cells in the notebook sequentially to load the data, build and train the model, and evaluate its performance.


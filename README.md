# kairos-anomaly
Project for *Mobile Robotics* course *@UniVr - A.Y. 2021/2022*

*Author:* Luigi Palladino

*Supervisor:* Prof. Alessandro Farinelli

Thanks to Francesco Trotti for providing data from Kairos robot.

### Brief Description:
- Deep Learning based algorithm for anomaly detection on mobile robot Kairos.
- Data collected are timeseries recorded from ROS topic publication of packages.
- Anomaly Detection system is based on the training and use of a regression encoder-decoder architecture based on LSTM units.
The network is trained on "regular" timeseries and tested on data with anomalies. The trained model is capable of reconstructing the input signal and compute a loss based on MAE to understand if the data in INPUT is different from "usual" data. If a pre-computed treshold in loss value is registered, an anomaly warning is called.
- A more in-depth understanding of causes of anomaly is made exploiting shapley values using explainability library SHAP.
- Analyzed usecase is based on 4 recordings of data where kairos robot navigates in an pre-explored environment where he expects to find a door closed. The door is purposely left open to generate an anomaly state which will be detected by the system.

### Installation:
- Install python 3.7
- Install pip packages from 'requirements.txt'

Creation of a separated venv/conda environment is encouraged.

### Usage:

Run *\*.ipynb* notebooks to replicate results and understand how the code works to deploy in an application:
- *train.ipynb* for training
- *test.ipynb* for results testing
- *kairos_preprocessing.ipynb* to understand how to apply pre-processing from csv files to acquired ROS packages.
- *explainability.ipynb* for investigation of anomalies causes using SHAP.

Refer to 'slides.pptx' for a full report on activities made in this project.

#### Explainability part will be inserted in Luigi Palladino's  final dissertation:
*Increasing trustworthiness of deep learning models in high-risk applications with explainable-AI*

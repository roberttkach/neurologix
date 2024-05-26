# NeuroLogix

NeuroLogix is a comprehensive microservice platform designed to streamline the deployment of machine learning models. The system automatically generates Docker files and deploys them to Kubernetes when new models are added. It also collects metrics using Prometheus and visualizes them with Grafana. Additionally, the MLflow service is used to visualize the performance of neural network models.

## Features

- **Automatic Docker File Creation and Deployment**: Automatically generates Docker files and deploys them to Kubernetes when new models are added.
- **Metric Collection and Visualization**: Uses Prometheus to collect metrics from models and visualizes them in Grafana.
- **MLflow Integration**: Visualizes the performance of neural network models.
- **FastAPI-based API**: Provides endpoints for uploading models and managing deployments.

## Getting Started

### Prerequisites

- Docker
- Kubernetes
- Minikube (or another local Kubernetes cluster)
- Python 3.8 or higher

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/roberttkach/neurologix.git
    cd neurologix.git
    ```

2. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Start Minikube:**

    ```sh
    minikube start
    ```

### Usage

1. **Run the FastAPI server:**

    ```sh
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

2. **Upload a model:**

    Use an API client like Postman or `curl` to upload a model archive (zip, 7z, rar, or tar.gz) to the `/archive` endpoint. The archive should contain a `requirements.txt` and `train.py`.

    Example with `curl`:

    ```sh
    curl -X POST "http://localhost:8000/archive" -F "file=@/path/to/your/model.zip" -F "name=model_name"
    ```


### Configuration

- **Logging**: Logs are stored in the `logs.log` file.
- **Kubernetes Manifests**: Generated Kubernetes manifests are stored in the `containers/` directory.

### FastAPI Endpoints

- `GET /`:
  - Description: Welcome message and instructions.
  - Response: JSON with a welcome message and instructions.

- `POST /archive`:
  - Description: Upload a model archive.
  - Parameters:
    - `file` (UploadFile): The model archive file.
    - `name` (Form): The name for the model container.
  - Response: JSON message indicating success or failure.



- Prometheus for metrics collection
- Grafana for visualization
- MLflow for model performance tracking
- FastAPI for the API framework

For more information, please refer to the official documentation or contact the project maintainers.

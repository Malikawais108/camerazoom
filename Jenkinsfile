pipeline {
    agent any

    environment {
        PYTHON_ENV = 'venv'
    }

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning CameraZoom repository...'
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                echo 'Creating Python virtual environment and installing dependencies...'
                sh '''
                    python3 -m venv $PYTHON_ENV
                    . $PYTHON_ENV/bin/activate && \
                    pip install --upgrade pip && \
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run App') {
            steps {
                echo 'Running CameraZoom...'
                sh '''
                    . $PYTHON_ENV/bin/activate && \
                    python camerazoom.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh '''
                    docker build -t camerazoom:latest .
                '''
            }
        }

        // Optional: Add deployment or push to DockerHub later
    }
}

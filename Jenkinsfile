pipeline {
    agent any

    environment {
        PYTHON_ENV = 'venv'
    }

    stages {
        stage('Clone') {
            steps {
                echo '📥 Cloning CameraZoom repository...'
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                echo '🐍 Creating Python virtual environment and installing dependencies...'
                sh '''
                    python3 -m venv $PYTHON_ENV
                    if [ ! -f "$PYTHON_ENV/bin/activate" ]; then
                        echo "❌ Virtualenv creation failed!"
                        exit 1
                    fi
                    . $PYTHON_ENV/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run App') {
            steps {
                echo '🚀 Running CameraZoom...'
                sh '''
                    if [ ! -f "camerazoom.py" ]; then
                        echo "❌ camerazoom.py not found!"
                        exit 1
                    fi
                    . $PYTHON_ENV/bin/activate
                    python camerazoom.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                sh 'docker build -t camerazoom:latest .'
            }
        }

        stage('Archive Artifacts') {
            steps {
                echo '📦 Archiving build artifacts...'
                archiveArtifacts artifacts: '**/dist/*', fingerprint: true
            }
        }
    }

    post {
        success {
            echo '✅ Build completed successfully!'
        }
        failure {
            echo '❌ Build failed. Check logs for details.'
        }
    }
}

pipeline {
    agent any

    environment {
        PYTHON_ENV = 'venv'
    }

    stages {
        stage('Tag Build') {
            steps {
                script {
                    def commit = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                    currentBuild.displayName = "#${BUILD_NUMBER} - ${commit}"
                }
            }
        }

        stage('Clone') {
            steps {
                echo '📥 Cloning CameraZoom repository...'
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                echo '🐍 Setting up Python environment...'
                sh '''
                    set -e
                    if [ ! -f "requirements.txt" ]; then
                        echo "❌ requirements.txt not found!"
                        exit 1
                    fi

                    python3 -m venv $PYTHON_ENV
                    . $PYTHON_ENV/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running unit tests...'
                sh '''
                    set -e
                    . $PYTHON_ENV/bin/activate
                    pytest tests/ --maxfail=1 --disable-warnings --junitxml=test-results.xml
                '''
            }
        }

        stage('Run App') {
            steps {
                echo '🚀 Executing CameraZoom...'
                sh '''
                    set -e
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
                sh '''
                    set -e
                    if [ ! -f "Dockerfile" ]; then
                        echo "❌ Dockerfile missing!"
                        exit 1
                    fi
                    docker build -t camerazoom:latest .
                '''
            }
        }

        stage('Archive Artifacts') {
            steps {
                echo '📦 Archiving test results and build outputs...'
                archiveArtifacts artifacts: '**/test-results.xml, **/dist/*', fingerprint: true
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
        always {
            echo '🧹 Cleaning up workspace...'
            cleanWs()
        }
    }
}

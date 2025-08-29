pipeline {
    agent any

    environment {
        PYTHON_ENV = 'venv'
    }

    stages {
        stage('Debug Setup') {
            steps {
                echo '🔍 Starting debug setup...'
                sh '''
                    echo "Current directory: $(pwd)"
                    echo "Listing files:"
                    ls -la

                    echo "Creating virtualenv..."
                    python3 -m venv $PYTHON_ENV

                    echo "Checking if activate script exists:"
                    ls -la $PYTHON_ENV/bin/activate || echo "❌ Missing activate script"

                    echo "Activating virtualenv..."
                    . $PYTHON_ENV/bin/activate

                    echo "Python version:"
                    python --version || echo "❌ Python not found"

                    echo "Pip version:"
                    pip --version || echo "❌ Pip not found"

                    echo "Installing dependencies..."
                    pip install -r requirements.txt || echo "❌ requirements.txt failed"
                '''
            }
        }
    }

    post {
        always {
            echo '🧪 Debug stage completed.'
        }
    }
}

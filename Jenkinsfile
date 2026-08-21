pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -c "import app; print(\'Application test passed\')"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment stage reached'
            }
        }
    }
}

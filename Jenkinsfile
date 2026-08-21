pipeline {
    agent any

    stages {

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
                sh './deploy.sh'
            }
        }

    }
}








































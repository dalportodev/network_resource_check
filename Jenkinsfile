Jenkinsfile (Declarative Pipeline)
/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.12.6-alpine3.20' } }
    stages {
        stage('build') {
            steps {
                sh 'C:\Users\csdal\AppData\Local\Programs\Python\Python312\python -m pytest ping_test.py'
            }
        }
    }
}
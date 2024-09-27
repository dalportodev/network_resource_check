/* Requires the Docker Pipeline plugin */
pipeline {
    stages {
        stage('build') {
            steps {
                sh 'python -m pytest ping_test.py'
            }
        }
    }
}
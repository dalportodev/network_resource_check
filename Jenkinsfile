/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                bat 'C:\\Users\\csdal\\AppData\\Local\\Programs\\Python\\Python312\\python -m pytest ping_test.py'
            }
            post {
                always {
                    allure includeProperties:
                     false,
                     jdk: '',
                     results: [[path: '$WORKSPACE/target/allure-results']]
                }
            }
        }
    }
}
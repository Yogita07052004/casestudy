pipeline {
    agent any

    environment {
        IMAGE_NAME = "yogita1232/cs1232:v1"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                git url: 'https://github.com/Yogita07052004/casestudy.git', branch: 'master'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat """
                    docker build -t %IMAGE_NAME% .
                """
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', 
                                                  usernameVariable: 'yogita1232', 
                                                  passwordVariable: 'yogita@2004')]) {
                    bat """
                        echo Logging in to Docker Hub
                        docker logout
                        echo %yogita@2004% | docker login -u %yogita1232% --password-yogita@2004
                    """
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                bat """
                    docker push %IMAGE_NAME%
                """
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploy to Kubernetes logic here"
                // Add your kubectl commands if needed
            }
        }
    }

    post {
        failure {
            echo "Something went wrong. Check the logs."
        }
    }
}

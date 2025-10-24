pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        IMAGE_NAME = "yogita1232/cs1232"
        IMAGE_TAG = "v1"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Yogita07052004/casestudy.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh """
                    kubectl set image deployment/cs1232-deployment cs1232=${IMAGE_NAME}:${IMAGE_TAG} || \
                    kubectl create deployment cs1232-deployment --image=${IMAGE_NAME}:${IMAGE_TAG}
                    kubectl expose deployment cs1232-deployment --type=NodePort --port=5000 --target-port=5000 || true
                    """
                }
            }
        }
    }

    post {
        success {
            echo "Build, Push, and Deployment Successful!"
        }
        failure {
            echo "Something went wrong. Check the logs."
        }
    }
}

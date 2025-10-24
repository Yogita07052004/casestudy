pipeline {
    agent any

    environment {
        IMAGE_NAME = "yogita1232/cs1232"
        IMAGE_TAG = "v1"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'https://github.com/Yogita07052004/casestudy.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
            }
        }

        stage('Login to Docker Hub') {
    steps {
        withCredentials([usernamePassword(
            credentialsId: 'dockerhub-creds',
            usernameVariable: 'yogita1232',
            passwordVariable: 'yogita@2004'
        )]) {
            bat """
            echo %DOCKERHUB_PASS% | docker login -u %DOCKERHUB_USER% --password-stdin
            """
        }
    }
}


        stage('Push Docker Image') {
            steps {
                bat "docker push %IMAGE_NAME%:%IMAGE_TAG%"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat """
                kubectl set image deployment/cs1232-deployment cs1232=%IMAGE_NAME%:%IMAGE_TAG% || \
                kubectl create deployment cs1232-deployment --image=%IMAGE_NAME%:%IMAGE_TAG%
                kubectl expose deployment cs1232-deployment --type=NodePort --port=5000 --target-port=5000 || exit 0
                """
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

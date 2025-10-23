pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Yogita07052004/casestudy.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t your_dockerhub_username/recipe-app:latest .'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-token', variable: 'DOCKER_TOKEN')]) {
                    bat '''
                    echo %DOCKER_TOKEN% | docker login -u your_dockerhub_username --password-stdin
                    docker push your_dockerhub_username/recipe-app:latest
                    '''
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
}

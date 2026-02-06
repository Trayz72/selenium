pipeline {
    agent any

    environment {
        IMAGE_NAME = "trayz72/selenium-app"
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout Source') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                  echo "Building Docker image..."
                  docker build -t $IMAGE_NAME:$IMAGE_TAG .
                '''
            }
        }

        stage('Run Selenium UI Tests') {
            steps {
                sh '''
                  echo "Running Selenium tests inside container..."
                  docker run --rm \
                    $IMAGE_NAME:$IMAGE_TAG \
                    pytest tests/
                '''
            }
        }

        stage('Docker Hub Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                      echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    '''
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                sh '''
                  echo "Pushing image to Docker Hub..."
                  docker push $IMAGE_NAME:$IMAGE_TAG

                  docker tag $IMAGE_NAME:$IMAGE_TAG $IMAGE_NAME:latest
                  docker push $IMAGE_NAME:latest
                '''
            }
        }
    }

    post {
        always {
            sh 'docker logout || true'
        }
        success {
            echo '✅ Docker image built, tested, and pushed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs above.'
        }
    }
}


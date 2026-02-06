pipeline {
    agent any

    environment {
        IMAGE_NAME = "trayz72/selenium-app"
        IMAGE_TAG  = "${BUILD_NUMBER}"
        TEST_IMAGE = "selenium-test:${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout Source') {
            steps {
                checkout scm
            }
        }

        stage('Build Test Image') {
            steps {
                sh '''
                  echo "Building TEST image (with Chrome + Selenium)..."
                  docker build --target test -t $TEST_IMAGE .
                '''
            }
        }

        stage('Run Selenium UI Tests') {
            steps {
                sh '''
                  echo "Running Selenium tests inside TEST image..."
                  docker run --rm $TEST_IMAGE pytest tests/
                '''
            }
        }

        stage('Build Runtime Image') {
            steps {
                sh '''
                  echo "Building RUNTIME image (lightweight)..."
                  docker build --target runtime -t $IMAGE_NAME:$IMAGE_TAG .
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
                  echo "Pushing lightweight runtime image..."
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
            sh 'docker system prune -f || true'
        }
        success {
            echo 'Tests passed and LIGHTWEIGHT image pushed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs above.'
        }
    }
}

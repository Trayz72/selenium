pipeline {
    agent any
    
    stages {
        stage('Setup') {
            steps {
                sh 'python3 -m venv venv'                    
                sh './venv/bin/pip install -r requirements.txt' 
            }
        }
        
        stage('UI Tests') {
            steps {
                sh './venv/bin/python app.py &'  
                sh 'sleep 3'                     
                sh './venv/bin/python tests/test_login.py'  
            }
        }
    }
    
}
pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'whoami'
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install --user -r requirements.txt'
                sh 'python3 main.py dou.ua'
            }
        }
    }
}

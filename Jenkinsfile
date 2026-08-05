pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/katthikrishnaveni-playwright/Ecommerce_Automation.git'
            }
        }

        stage('Install Dependencies') {
            steps {
            bat '"C:\\Users\\ajay\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browsers') {
            steps {
            bat '"C:\\Users\\ajay\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m playwright install'
            }
        }

        stage('Run Tests') {
            steps {
            bat '"C:\\Users\\ajay\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest -v -s --html=reports\\report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/**/*', fingerprint: true
        }

        success {
            echo 'Build Successful!'
        }

        failure {
            echo 'Build Failed!'
        }
    }
}
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
                bat '''
                "C:\\Users\\ajay\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt
                '''
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                bat '''
                "C:\\Users\\ajay\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m playwright install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                "C:\\Users\\ajay\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest -v -s tests --html=reports\\report.html --self-contained-html
                echo Exit Code = %ERRORLEVEL%
                '''
            }
        }
    }

    post {

        always {
            archiveArtifacts artifacts: 'reports/**/*', allowEmptyArchive: true

            publishHTML(target: [
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Pytest HTML Report'
            ])
        }

        success {
            echo '==============================='
            echo 'BUILD SUCCESSFUL'
            echo '==============================='
        }

        failure {
            echo '==============================='
            echo 'BUILD FAILED'
            echo '==============================='
        }
    }
}
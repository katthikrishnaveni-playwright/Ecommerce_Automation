post {

    always {

        archiveArtifacts artifacts: 'reports/**/*',
                         allowEmptyArchive: true

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
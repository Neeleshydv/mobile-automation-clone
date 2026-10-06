pipeline {
    agent any

    triggers {
        pollSCM('H/5 * * * *')
        cron('H 3 * * *')
    }

    stages {
        stage('1. Prepare Python') {
            steps {
                echo 'Installing mobile test dependencies...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('2. Run Android Tests') {
            steps {
                echo 'Executing Android Mobile Test Suite...'
                sh '''
                    . venv/bin/activate
                    PLATFORM=android pytest -m android --html=reports/android_report.html --self-contained-html
                '''
            }
        }

        stage('3. Run iOS Tests') {
            steps {
                echo 'Executing iOS Mobile Test Suite...'
                sh '''
                    . venv/bin/activate
                    PLATFORM=ios pytest -m ios --html=reports/ios_report.html --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'mobile_report.html',
                reportName: 'Mobile Automation Execution Report'
            ])
        }
    }
}

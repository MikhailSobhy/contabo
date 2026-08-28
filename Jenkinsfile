pipeline {
    agent any

    stages {
        stage('Test Permissions') {
            steps {
                sh '''
                    echo "Running as:"
                    whoami

                    echo "Testing write permission..."
                    touch /opt/odoo/custom-addons/jenkins-test

                    echo "File created:"
                    ls -l /opt/odoo/custom-addons/jenkins-test
                '''
            }
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Deploy') {
            steps {
                sh '''
                    echo "Starting deployment..."

                    sudo -u odoo git -C /opt/odoo/custom-addons pull origin main

                    echo "Deployment finished.."
                '''
            }
        }
    }
}

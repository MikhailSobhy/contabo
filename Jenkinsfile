pipeline {
    agent any

    stages {
        stage('Deploy') {
            steps {
                sh '''
                    echo "Starting deployment..."

                    sudo -u odoo /usr/bin/git -C /opt/odoo/custom-addons pull origin main

                    echo "Restarting Odoo..."
                    sudo systemctl restart odoo

                    echo "Deployment finished successfully."
                '''
            }
        }
    }
}

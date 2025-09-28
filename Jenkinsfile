pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // The pipeline will automatically check out the SCM.
                echo 'Repository code has been checked out.'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using the Dockerfile in the repository
                    sh 'docker build -t flask-app-image .'
                }
            }
        }

        stage('Test Application') {
            steps {
                script {
                    echo 'Running tests...'
                    // Create a container and run tests inside it.
                    // This assumes you have tests defined and pytest is in requirements.txt.
                    sh 'docker run --rm flask-app-image pytest'
                }
            }
            post {
                always {
                    // Archive test reports.
                    junit '**/test-reports/results.xml'
                }
            }
        }

        stage('Deploy to Production') {
            when {
                // Optional: Deploy only for the 'main' branch
                branch 'main'
            }
            steps {
                echo 'Deploying application to production...'
                // The deployment step will depend on your target environment.
                // For a simple example, you could use SSH to connect to a server
                // and start the container.
                // Example for a remote server:
                // sh "ssh user@your-server.com 'docker stop my-flask-app || true && docker rm my-flask-app || true && docker run -d --name my-flask-app -p 5000:5000 flask-app-image'"
            }
        }
    }
}

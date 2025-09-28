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
                    echo 'Running tests with volume mount...'
                    // Create the test-results directory in the Jenkins workspace
                    sh 'mkdir -p test-results'
                    
                    // Run the container, mounting the workspace to write reports directly
                    sh 'docker run --rm -v $(pwd)/test-results:/app/test-results -w /app flask-app-image python -m pytest --junitxml=test-results/report.xml'
                }
            }
            post {
                always {
                    // Archive test reports.
                    junit '**/test-results/report.xml'
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

pipeline {
    agent any

    environment {
        VENV_PATH = 'venv'
        FLASK_APP = 'main.py'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from a source control 
                //management system (e.g., Git)
                git url: 'git@github.com:maunnztiger/dexterslab.git', branch: 'main',
                credentialId: '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'

            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                    // Check for the virtual environment, 
                    // create it if it doesn't exist
                    sh 'bash -c "python3 -m virtualenv $VENV_PATH"'
                    // Activate the virtual environment
                    sh 'bash -c "source $VENV_PATH/bin/activate"'
                }
            }
        }
         stage('Install dependencies') {
            steps {
                // Install any dependencies listed in requirements.txt
                 sh 'bash -c "source $VENV_PATH/bin/activate"'
            }
        }

        stage('Test') {
            steps {
                // Run your tests here. This is just a placeholder.
                // For example, if you had tests, you might run: pytest
                echo "Assuming tests are run here."
                sh '''#!/bin/bash 
                        "/home/igor/BDD_SELENIUM_BEHAVE/run_tests.sh"
                '''
                 }
            }

        stage('Deploy') {
            steps {
                script {
                    // Deploy your Flask app
                    // This step greatly depends on where and 
                    // how you're deploying your app
                    // For example, if you're deploying to a server you control,
                    // you might use scp, rsync, or SSH commands
                    // If you're using a PaaS (Platform as a Service), 
                    //you might use a specific CLI tool for that platform
                    echo 'Deploying application...'
                    sh 'cp -ar . /home/igor/dexterslab'
                }
            }
        }
    }

    post {
        always {
            // Clean up after the pipeline runs
            echo 'Cleaning up...'
            sh 'rm -rf ${VIRTUAL_ENV_DIR}'
        }
    }
}

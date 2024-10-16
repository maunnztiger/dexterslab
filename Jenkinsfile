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
                git url: 'https://github.com/maunnztiger/dexterslab.git', branch: 'main'
                
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                     sh '''
                    
                        bash -c 'python3 -m venv $VENV_PATH'
                        bash -c 'source $VENV_PATH/bin/activate && curl https://bootstrap.pypa.io/get-pip.py | python'
                    
                    '''
                }
            }
        }
         stage('Install dependencies') {
            steps {
                // Install any dependencies listed in requirements.txt
                 sh 'bash -c "source $VENV_PATH/bin/activate && pip install -r requirements.txt"'
        }
        }
        stage('Test') {
            steps {
                // Run your tests here. This is just a placeholder.
                // For example, if you had tests, you might run: pytest
                echo "Assuming tests are run here."
                sh 'bash -c "cd /home/igor/dexterslab-robot-testing/ && sudo -u jenkins /home/igor/dexterslab-robot-testing/run_tests.sh"'
        
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
                    sh 'bash -c "sudo -u jenkins cp -rf . /home/igor/dexterslab"'
                    sh 'bash -c "sudo systemctl restart dexterslab-service.service"'
                }
            }
        }
    }

    post {
        always {
            // Clean up after the pipeline runs
            echo 'Cleaning up...'
            sh 'rm -rf ${VENV_PATH}'
           
        }
    }
}

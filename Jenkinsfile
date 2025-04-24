pipeline {
  agent any

  environment {
    DOCKER_BUILDKIT = 1
  }

  stages {
    stage('Checkout') {
      steps {
        checkout([$class: 'GitSCM',
          branches: [[name: '*/main']],
          userRemoteConfigs: [[
            url: 'https://github.com/russjeff22/simple-api-jmeter.git',
            credentialsId: 'git-cred'
          ]]
        ])
      }
    }

    stage('Build API Image') {
      steps {
        dir('simple-api') {
          sh 'docker build -t simple-api:latest .'
        }
      }
    }

    stage('Run API Container') {
      steps {
        script {
          sh 'docker rm -f simple-api || true'
          sh 'docker run -d --name simple-api --restart unless-stopped -p 8000:8000 simple-api:latest'
        }
      }
    }

    stage('Run JMeter Test') {
      steps {
        dir('jmeter') {
          sh 'docker build -t jmeter-test:latest .'
          sh 'docker run --rm jmeter-test:latest'
        }
      }
    }
  }

  post {
    always {
      echo 'Post stage intentionally left blank. No cleanup.'
    }
  }
}

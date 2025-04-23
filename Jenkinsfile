pipeline {
  agent any

  environment {
    DOCKER_BUILDKIT = 1
  }

  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/russjeff22/simple-api-jmeter.git', branch: 'main'
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
        sh 'docker run -d --name simple-api -p 8000:8000 simple-api:latest'
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
      sh 'docker stop simple-api || true'
      sh 'docker rm simple-api || true'
    }
  }
}

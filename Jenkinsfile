pipeline {
  agent none

  stages {
    stage('Checkout') {
      agent any
      steps {
        git branch: 'main', url: 'https://github.com/ikefreet/covid19-vaccine.git'
      }
    }
    stage('Build Docker Image') {
      agent any
      steps {
        sh 'docker image build -t efreet05/wordpress:latest .'
      }
    }
    stage('Tag Docker Image') {
      agent any
      steps {
        sh 'docker image tag efreet05/wordpress:latest efreet05/wordpress:$BUILD_NUMBER'
      }
    }
    stage('Publish Docker Image') {
      agent any
      steps {
        withDockerRegistry(credentialsId: 'docker-hub-token', url: 'https://index.docker.io/v1/') {
          sh 'docker image push efreet05/wordpress:$BUILD_NUMBER'
        }
      }
    }
  }
}




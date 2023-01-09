node {
  
    stage('Checkout') {
        git branch: 'main', url: 'https://github.com/ikefreet/covid19-vaccine.git'
    }
    stage('Login'){
        sh 'echo jyhfpkcs%% | docker login -u efreet05 --password-stdin' // docker hub 로그인
    }
    stage('Build Docker Image') {
        sh 'docker image build -t efreet05/django:latest .'
    }
    stage('Tag Docker Image') {
        sh 'docker image tag efreet05/django:latest efreet05/django:$BUILD_NUMBER'
    }
    stage('Publish Docker Image') {
        withDockerRegistry(credentialsId: 'docker-hub-token', url: 'https://index.docker.io/v1/') {
          sh 'docker image push efreet05/django:$BUILD_NUMBER'
      }
    }
}




pipeline{
    agent any;
    stages{
        stage("code clone"){
            steps{
                git url: "https://github.com/dilnawaj9128/flask-app.git", branch: "main"
            }
        }
        stage("build"){
            steps{
                sh "docker build -t flask-app ."
            }
        }
        stage("test"){
            steps{
                echo "developer /tester test likh ke dega"
            }
        }
        stage("Push to docker hub"){
            steps{
                withCredentials([usernamePassword(
                    credentialsId:"dockerHubCreds",
                passwordVariable:"dockerHubPass",
                usernameVariable:"dockerHubUser"
                )]){
                    sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                    sh "docker image tag flask-app ${env.dockerHubUser}/flask-app"
                    sh "docker push ${env.dockerHubUser}/flak-app:latest"
                }
            }
        }
         stage("Deploy"){
            steps{
                sh "docker-compose down"
                sh "docker-compose up -d --build flask-app"
            }
        }
    }
}

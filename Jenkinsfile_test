pipeline {
    agent {
        label 'zip-job-docker'
        dockerfile {
            filename 'Dockerfile'
            args '-u root:root'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'python zip_job.py'
            }
        }
        stage('Publish') {
            when {
                success
            }
            steps {
                withArtifacts([includePatterns: '*.zip']) {
                    artifactoryPublish (
                        serverId: 'artifactory-xx',
                        repoKey: "store-artifacts/${env.VERSION}",
                        user: 'superman',
                        password: 'P@ssw0rd123$',
                        useSpecs: true,
                        specs: [
                            [file: 'artifactory.json']
                        ]
                    )
                }
            }
        }
        stage('Report') {
            when {
                success
            }
            steps {
                emailext (
                    subject: "Job ${env.JOB_NAME} (${env.BUILD_NUMBER}) status: SUCCESS",
                    to: "requestor@email.com",
                )
            }
        }
        stage('Cleanup') {
            steps {
                deleteDir()
            }
        }
    }
}

# Medical Cost Prediction

## Deployment
1) Check docker image working
2) GitHub Workflows
3) IAM User - with AmazonEC2ContainerRegistryFullAccess and AmazonEC2FullAccess policies attached - and create access keys
4) Create a new ECR repository - URL: 389366992858.dkr.ecr.us-east-1.amazonaws.com/medicalcostprediction
5) Create an EC2 instance with enough disk space
6) Once created, connect to the instance and install the necessary packages for docker:

        sudo apt-get update -y

        sudo apt-get upgrade
        
        curl -fsSL https://get.docker.com -o get-docker.sh
        
        sudo sh get-docker.sh
        
        sudo usermod -aG docker ubuntu
        
        newgrp docker 

7) Initiate Runner setup (Github Repo -> Settings -> Actions (on the LHS) -> Under Actions, click Runners
8) Download and Configure the runner on the EC2 instance using the commands mentioned when you create a new runner (in the above-mentioned path).
9) Create 5 secret keys in GitHub Actions - AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, AWS_ECR_LOGIN_URI, ECR_REPOSITORY_NAME

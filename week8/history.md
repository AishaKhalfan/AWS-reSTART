[ec2-user@ip-10-200-0-167 static-website]$ history
    1  cler
    2  clear
    3  ls
    4  cd sysops-activity-files/
    5  ls
    6  cd ..
    7  aws configure
    8  aws s3api create-bucket --bucket ak56 --region us-west-2 --create-bucket-configuration LocationConstraint=us-west-2
    9  aws iam create-user --user-name awsS3user
   10  aws iam create-login-profile --user-name awsS3user --password Training123!
   11  aws iam list-policies --query "Policies[?contains(PolicyName,'S3')]"
   12  aws iam attach-user-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --user-name awsS3user
   13  aws iam attach-user-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3OutpostsFullAccess --user-name awsS3user
   14  aws iam list-policies --query "Policies[?contains(PolicyName,'S3')]"
   15  aws iam attach-user-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --user-name awsS3user
   16  cd ~/sysops-activity-files
   17  tar xvzf static-website-v2.tar.gz
   18  cd static-website
   19  ls
   20  aws s3 website s3://ak56/ --index-document index.html
   21  aws s3 cp /home/ec2-user/sysops-activity-files/static-website/ s3://ak56/ --recursive --acl public-read
   22  aws s3 ls ak56
   23  aws s3 cp /home/ec2-user/sysops-activity-files/static-website/ s3://ak56/ --recursive --acl public-read
   24  aws s3 cp /home/ec2-user/sysops-activity-files/static-website/ s3://ak56/ --recursive --acl
   25  aws s3 cp /home/ec2-user/sysops-activity-files/static-website/ s3://ak56/ --recursive
   26  aws s3 ls ak56
   27  history

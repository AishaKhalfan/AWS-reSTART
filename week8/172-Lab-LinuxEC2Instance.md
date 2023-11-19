# Amazon EC2 Instances (Challenge)
 

## Lab overview
In this challenge lab, you apply what you have learned so far about Amazon Elastic Compute Cloud (Amazon EC2). You follow some high-level steps to create a web application running on an Amazon Linux EC2 instance.

 

## Objectives
After completing this challenge, you should be able to do the following:

- Configure a virtual network. 

- Place an Amazon Linux EC2 instance into this virtual network.

- Install a web server, and deploy and run a simple application on it.

## Duration
This challenge requires approximately 45 minutes to complete.

 

## Launch Your lab environment
1. At the top of these instructions, choose Start Lab to launch the lab.

  A ``Start Lab`` panel opens displaying the lab status.

2. Wait until the message "Lab status: ready" appears, and then choose X to close the Start Lab panel.

This lab creates a new AWS account for you that you use to create the resources needed to launch an EC2 instance and run a web application.

3. Next to Start Lab, choose AWS to open the AWS Management Console on a new browser tab. The system automatically signs you in.

Tip If a new browser tab does not open, a banner or icon at the top of your browser will indicate that your browser is preventing the site from opening pop-up windows. Choose the banner or icon, and choose Allow pop-ups.

 

## Your challenge
 

4. Create an Amazon Linux EC2 instance to run a web application. The general steps are as follows:

	- Use the AWS Management Console to launch the instance.

	- Use an Amazon Linux Amazon Machine Image (AMI) and a T3 instance type with a size that is smaller than medium.

	- Launch the instance in a new virtual private cloud (VPC) and a new subnet, and auto-assign the instance's public IPv4 address.

	- While you are creating your instance, in the user data, install and start the httpd service as your web server. Give write permission to users to the web server's document root directory (/var/www/html).

	- Use a General Purpose SSD (gp2) volume type for the root volume.

	- Configure the instance, and create the necessary resources so that you can connect to it by using Secure Shell (SSH).

	- Capture a screenshot of the EC2 instance's system log showing that the httpd service was successfully installed.

 

5. To test your web server, deploy the web page in the following steps to your web server.

	- Use EC2 Instance Connect to connect to your EC2 instance.

	- Copy and paste the following HTML code into a text editor:       
```html
<!DOCTYPE html>
<html>
<body>
<h1>YOUR-NAME's re/Start Project Work</h1>
<p>EC2 Instance Challenge Lab</p>
</body>
</html>
```
		 - Replace YOUR-NAME with your name, and save the file as projects.html

	- Place this file in the /var/www/html directory of your EC2 instance.

	- Open a web browser, and navigate to this sample webpage. Capture a screenshot showing that the page was successfully returned and displayed.

	- Submit the screenshots that you captured to your instructor.

## Hints

- You need to create an internet gateway and properly configure the subnet's route table in your VPC before you launch your instance.

- You need to use EC2 Instance Connect to connect over SSH to your EC2 instance by using a web browser.

- Make sure that you have the right security group settings. In particular, you should allow for SSH and HTTP traffic.

- Use the public IPv4 address of the instance to access your webpage.

- You need to elevate to sudo to copy the file to the /var/www/html/ directory.

- Refer to the following labs for additional guidance:

	- Creating Amazon EC2 Instances

# Lab complete
 Congratulations! You have completed this challenge lab.

6. At the top of this page, choose End Lab and then choose Yes to confirm that you want to end the lab.  

A panel appears indicating that "You may close this message box now. Lab resources are terminating."

 

## Additional resources

- [Launch Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html)
- [Connect to Your Linux instance Using EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-eic.html)
- [Amazon EC2 - User Data and Shell Scripts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)
- [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/)

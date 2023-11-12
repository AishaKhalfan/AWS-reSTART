# Using AWS Systems Manager

## Lab overview

AWS Systems Manager is a collection of capabilities that you can use to centralize operational data and automate tasks across your Amazon Web Services (AWS) resources. Systems Manager can configure and manage Amazon Elastic Compute Cloud (Amazon EC2) instances, on-premises servers, virtual machines, and other AWS resources at scale. 

## Objectives
After completing this lab, you should be able to use Systems Manager to do the following:

	- Verify configurations and permissions.
	- Run tasks on multiple servers.
	- Update application settings or configurations.
	- Access the command line on an instance.

## Duration
This activity requires approximately 30 minutes to complete.

## Accessing the AWS Management Console
1. At the top of these instructions, choose Start Lab to launch the lab.

2. Wait until the message "Lab status: ready" appears, and then choose X to close the Start Lab panel.

3. Next to Start Lab, choose AWS to open the AWS Management Console in a new browser tab. The system automatically signs you in.

**Tip** If a new browser tab does not open, a banner or icon at the top of your browser will indicate that your browser is preventing the site from opening pop-up windows. Choose the banner or icon, and choose Allow pop-ups.

4. Arrange the AWS Management Console so that it appears alongside these instructions. 

 Do not change the Region unless instructed to do so.

# Task 1: Generate inventory lists for managed instances
You can use Fleet Manager, a capability of Systems Manager, to collect operating system information, application information, and metadata from EC2 instances, on-premises servers, or virtual machines in a hybrid environment. You can also use Fleet Manager to query metadata to quickly understand which instances are running the software and configurations that your software policy requires and which instances you need update.

In this task, you use Fleet Manager to gather inventory from an EC2 instance.

5. In the AWS Management Console, in the  search box, enter Systems Manager and press Enter. This option takes you to the Systems Manager console page.

6. In the left navigation pane, for Node Management, choose Fleet Manager.

7. Choose the Account management dropdown list, and choose Set up inventory.

8. To create an association that collects information about software and settings for your managed instance, choose the following options:

	- In the Provide inventory details section, for Name, enter Inventory-Association

	- In the Targets section, choose the following options:

		- For Specify targets by, choose Manually selecting instances.
		- Select the row for Managed Instance.
Leave the other options as the default settings.

9. Choose ``Setup Inventory``

A banner with the message "Setup inventory request succeeded" appears on the Fleet Manager page. Inventory, a capability of Systems Manager, now regularly inventories the instance for the selected properties.

10. Choose the ``Node ID link``, which directs you to the Node overview.

11. Choose the ``Inventory tab``.

This tab lists all of the applications in the instance. Take a moment to review the installed applications and other options in the Inventory type dropdown list.

You have successfully created a Systems Manager inventory association for your instance. Using Inventory, you can review and validate software configurations on your instances without needing to connect to each instance by using SSH.

# Task 2: Install a Custom Application using Run Command
In this task, you install a custom web application (Widget Manufacturing Dashboard) by using Run Command, a capability of Systems Manager.
![InstallApplication.png](https://github.com/AishaKhalfan/AWS-reSTART/blob/main/week8/images/InstallApplication.png)

A virtual private cloud (VPC) with an EC2 instance inside. A user outside the AWS Cloud uses Run Command to install a widget manufacturing web application.

*In the preceding diagram, Systems Manager installs an application on an EC2 instance within a virtual private cloud (VPC). It is installed by using Run Command. Run Command will run the "install script" and install the following: Apache web server, PHP, AWS SDK, and the web application. Once everything is installed, it also starts the web server.
*

12. In the upper-left corner, expand the menu icon. For Node Management, choose Run Command.

13. Choose ``Run command``

A list appears of pre-configured documents for running common commands. 

14. Choose the search icon  in the box, and a dropdown box appears. Choose the following options: 

	- Owner
	- Owned by me
A document appears.

**Note:** Do not enter Owner or Owned by me. Entering this text does not return results. 

15. If the document is not already selected, select the button for the document.

16. The following information appears for this document:

	- **Description Install Dashboard App**
	- **Document version: 1 (Default)**
Leave the **Document version** option set to this default. 

17. For **Target selection**, select **Choose instances manually**.

18. In the **Instances** section, select **Managed Instance**.

The **Managed Instance** has the Systems Manager agent installed. The agent has registered the instance to the service, which allows it to be selected for Run Command.

	- It is also possible to identify target instances by using tags. By using tags, you can run a single command on a whole fleet of matching instances.

19. In the **Output options** section, clear **Enable an S3 bucket**.

20. Expand the **AWS command line interface command** section.

	- This section displays the command line interface (CLI) command that initiates Run Command. You can copy this command and use it in the future within a script rather than having to use the AWS Management Console.

21. Choose ``Run``

 A banner with the **Command ID** indicates that it was successfully sent on the Command ID page.

22. After 1–2 minutes, the ``Overall status`` should change to ``Success``. If it doesn't, choose the  refresh icon to update the status.

 You now validate the custom application that was installed.

23. In the Vocareum console, choose the following options: 

	- Choose the Details dropdown list at the top of these instructions.
	- Choose Show
	- Copy the ServerIP value. (This value is the public IP address.)
24. Open a new web browser tab, paste the IP address that you copied, and press Enter.

 The **Widget Manufacturing Dashboard** that you installed appears.

You have successfully used Run Command through Systems Manager to install a custom application onto your instance without needing to remotely access the instance by using SSH.

# Task 3: Use Parameter Store to manage application settings

Parameter Store, a capability of Systems Manager, provides secure, hierarchical storage for configuration data management and secrets management. You can store data such as passwords, database strings, and license codes as parameter values. You can store values as plain text or encrypted data. You can then reference values by using the unique name that you specified when you created the parameter.


In this task, you use Parameter Store to store a parameter that you use to activate a feature in an application.

25. Keep the **Widget Manufacturing Dashboard** browser tab open, and return to the AWS Systems Manager tab.

26. In the left navigation pane, for **Application Management**, choose Parameter Store.

27. Choose ``Create parameter``

28. Choose the following options:

	- For ``Name:``, enter /dashboard/show-beta-features
	- For ``Description:`` , enter Display beta features
	- For ``Tier:``, leave the default option. 
	- For ``Type:``, leave the default option. 
	- For ``Value:``, enter True
29. Choose ``Create parameter``

A banner with the message "Create parameter request succeeded" appears at the top of the page. 

The parameter can be specified as a hierarchical path, such as /dashboard/<option>.

The application that is running on Amazon EC2 automatically checks for this parameter. If it finds this existing parameter, then additional features are displayed.

30. Return to the web browser tab that displays the application, and refresh the web page.

 If you accidentally closed this browser tab, choose the Details dropdown list at the top of these instructions, choose Show and then copy and paste the ServerIP value into a new browser tab. 

Notice that three charts are displayed. The application is now checking Parameter Store to determine whether the additional chart (which is still in beta) should be displayed. It is common to configure applications to display "dark features" that are installed but not yet activated.

**Optional**: Delete the parameter, and then refresh the browser tab with the application. The third chart disappears again.

# Task 4: Use Session Manager to access instances

With Session Manager, a capability of Systems Manager, you can manage your EC2 instances through an interactive one-step browser-based shell or through the AWS Command Line Interface (AWS CLI). Session Manager provides secure and auditable instance management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys. You can also use Session Manager to help comply with corporate policies that require controlled access to instances, strict security practices, and fully auditable logs with instance access details while still providing end users with one-step cross-platform access to your EC2 instances.

When you use Session Manager with Microsoft Windows, Session Manager provides access to a PowerShell console on the instance.

- ![accessInstances](https://github.com/AishaKhalfan/AWS-reSTART/blob/main/week8/images/AccessInstances.png)

A VPC with an EC2 instance inside. A user outside the AWS Cloud uses Systems Manager and Session Manager to access the EC2 instance.

In the preceding diagram, Systems Manager uses Session Manager to access the EC2 instance without having to connect to the instance by using SSH. Session Manager is one of the secure ways to access the instance.

In this task, you access the EC2 instance through Session Manager.

31. In the left navigation pane, for Node Management, choose Session Manager.

32. Choose ``Start session``

33. Select **Managed Instance.**

34. Choose ``Start session``

A new session tab opens in your browser.

35. To activate the cursor, choose anywhere in the session window.

36. Run the following command in the session window:

``ls /var/www/html``
The output lists the application files that were installed on the instance.

37. Run the following command in the session window:

```bash
# Get region
AZ=`curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone`
export AWS_DEFAULT_REGION=${AZ::-1}

# List information about EC2 instances
aws ec2 describe-instances
```

The output lists the EC2 instance details for the Managed Instance in JSON format.

This task demonstrates how you can use Session Manager to log in to an instance without using SSH. You can also verify this capability by confirming that the SSH port is closed for the instance's security group.

You can restrict access to Session Manager through AWS Identity and Access Management (IAM) policies, and AWS CloudTrail logs Session Manager usage. These options provide better security and auditing than traditional SSH access.

# Conclusion
Congratulations! You now have successfully done the following:

- Verified configurations and permissions
- Run tasks on multiple servers
- Updated application settings or configurations
- Accessed the command line on an instance

# Lab complete
38. At the top of this page, choose End Lab and then choose Yes to confirm that you want to end the lab.  

A panel appears indicating that "You may close this message box now. Lab resources are terminating."

39. To close the **End Lab** panel, choose the X in the upper-right corner.

## Additional resources
- [What is AWS Systems Manager?](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)
- [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)

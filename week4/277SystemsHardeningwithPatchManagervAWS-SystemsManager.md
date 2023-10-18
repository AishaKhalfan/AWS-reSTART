Systems Hardening with Patch Manager via AWS Systems Manager
 

Lab overview
In organizations with hundreds and often thousands of workstations, it can be logistically challenging to keep all the operating system (OS) and application software up to date. In most cases, OS updates on workstations can be automatically applied via the network. However, administrators must have a clear security policy and baseline plan to ensure that all workstations are running a certain minimum version of software.

In this lab, you use Patch Manager, a capability of AWS Systems Manager, to create a patch baseline. You then use the patch baseline that you created to scan the Amazon Elastic Compute Cloud (Amazon EC2) instances for Linux and Windows that were pre-created for this lab.

The primary focus of Patch Manager is to install OS security-related updates on managed nodes. 

 

Objectives
After completing this lab, you should be able to:

Create a custom patch baseline

Modify patch groups

Configure patching

Verify patch compliance

Duration
This lab requires approximately 60 minutes to complete.

Lab environment
The current environment has six EC2 instances: three instances with the Linux OS and three with the Windows OS.

All backend components, such as EC2 instances, AWS Identity and Access Management (IAM) roles, and some AWS services, have been built into your lab already. 

 

Accessing the AWS Management Console
At the upper-right corner of these instructions, choose  Start Lab 

Troubleshooting tip: If you get an Access Denied error, close the error box, and choose  Start Lab again.

The following information indicates the lab status: 

A red circle next to AWS  at the upper-left corner of this page indicates that the lab has not been started.

A yellow circle next to AWS  at the upper-left corner of this page indicates that the lab is starting.

A green circle next to AWS  at the upper-left corner of this page indicates that the lab is ready.

Wait for the lab to be ready before proceeding.

At the top of these instructions, choose the green circle next to AWS 

This option opens the AWS Management Console in a new browser tab. The system automatically sign you in.

Tip: If a new browser tab does not open, a banner or icon at the top of your browser might indicate that your browser is preventing the site from opening pop-up windows. Choose the banner or icon, and choose Allow pop-ups.

If you see a dialog prompting you to switch to the new console home, choose Switch to the new Console Home.

Arrange the AWS Management Console tab so that it displays along side these instructions. Ideally, you should be able to see both browser tabs at the same time so that you can follow the lab steps.

 Do not change the lab Region unless specifically instructed to do so.


Task 1: Select patch baselines
In this task, you select a patch baseline to apply to the Linux EC2 instances. You then create a custom patch baseline for the Windows server EC2 instances.

Patch Manager provides predefined patch baselines for each of the operating systems that it supports. You can use these baselines as they are currently configured (you can't customize them), or you can create your own custom patch baselines. You can use custom patch baselines for greater control over which patches are approved or rejected for your environment.

In the AWS Management Console, in the search  box, enter Systems Manager and select it. This option takes you to the Systems Manager console page.

In the left navigation pane, under Node Management, choose Fleet Manager.
Here are the pre-configured EC2 instances. There are three Linux instances and three Windows instances. These EC2 instances have a specific IAM role associated with them that allows you you managed them using Systems Manager, which is why you can view them in the Fleet Manager section. This is also part of the lab setup.

Select the check box next to Linux-1. Then choose the Node actions  dropdown list, and choose View details.
Here you can view details about the specific instance, such as Platform type, Node type, OS name, and the IAM role that allows you to use Systems Manager to manage this instance.

At the top of the page, choose AWS Systems Manager to go back to the Systems Manager homepage.

In the left navigation pane, under Node Management, choose Patch Manager.

Choose Start with an overview (Proceed to next step if this option does not appear).

Choose the Patch baselines tab. This tab includes the default patch baselines that you can select.

In the search bar, enter AWS-AmazonLinux2DefaultPatchBaseline and press Enter. Then select the radio button  next to the baseline that is listed.

Choose the Actions  dropdown list, and choose Modify patch groups.
 You can use a patch group to associate managed nodes with a specific patch baseline in Patch Manager. Patch groups help ensure that you're deploying the appropriate patches based on the associated patch baseline rules to the correct set of nodes.

In the Modify patch groups section under Patch groups, enter LinuxProd and then choose the Add button.

Choose Close.

 

Task 1.1: Tag instances
In this task, you tag your Windows instances. Later in the lab, you create a patch group and associate it with these tags. 

 The Linux instances were pre-configured during lab setup with LinuxProd tags and do not need any added tags.

In the AWS Management Console, in the search  bar, enter EC2 and select it.

Choose Instances, select the check box next to the Windows-1 instance, and then choose the Tags tab. 

Choose the Manage tags button, choose Add new tag, and configure the following options:

Key: Enter Patch Group

Value: Enter WindowsProd

Choose Save.

Repeat the previous steps to tag the Windows-2 and Windows-3 instances with the same tag.

 

Task 1.2: Create a custom patch baseline
Next, you create a custom patch baseline for the Windows instances. Although Windows has default patch baselines that you can use, for this use case, you set up a baseline for Windows security updates.

Return to the Systems Manager console. In the search bar at the top, enter Systems Manager and then select it.

In the left navigation pane, under Node Management, choose Patch Manager.

Choose Start with an overview (Proceed to next step if this option does not appear).

Choose the Patch baselines tab.

Choose the Create patch baseline button. 

For Patch baseline details, configure the following options:

For Name, enter WindowsServerSecurityUpdates

For Description - optional, enter Windows security baseline patch

For Operating system, choose Windows.

Leave the check box for Default patch baseline unselected.

In the Approval rules for operating systems section, configure the following options:

Products: From the dropdown list, choose WindowsServer2019. Also, deselect All so that it no longer appears under Products.

Severity: This option indicates the severity value of the patches that the rule applies to. To ensure that all service packs are included by the rule, choose Critical from the dropdown list.

Classification: From the dropdown list, choose SecurityUpdates.

Auto-approval: Enter 3 days.

Compliance reporting - optional: From the dropdown list, choose Critical.

Choose Add rule to add a second rule to this patch baseline, and configure the following options:

Products: From the dropdown list, choose WindowsServer2019. Also, deselect All so that it no longer appears under Products.

Severity: From the dropdown list, choose Important.

Classification: From the dropdown list, choose SecurityUpdates.

Auto-approval: Enter 3 days.

Compliance reporting - optional: From the dropdown list, choose High.

Choose Create patch baseline.

Next, modify a patch group for the Windows patch baseline that you just created, to associate it with a patch group.

In the Patch baselines section, select the button for the WindowsServerSecurityUpdates patch baseline that you just created.
Note: The patch baseline that you created may be on the second page of the baselines list. You could also use the search bar to locate it and then select it.

Choose the Actions dropdown list, and then choose Modify patch groups.

In the Modify patch groups section under Patch groups, enter WindowsProd 

Choose the Add button, and then choose Close. 

Summary of task 1
In this task, you used a default Linux Amazon patch baseline and modified a patch group for the LinuxProd group. You then tagged your Windows instances so that they could be associated with the WindowsProd patch group. You learned how to create a custom patch baseline for the Windows instances. 

 

Task 2: Configure patching
In this task, you patch the Linux instances using the Patch now feature and by specifying the key/value pair that the Linux instances are all tagged with. You then patch the Windows instances, also based on the tag associated with them.

After configuration, Patch Manager uses the Run Command to call the RunPatchBaseline document to evaluate which patches should be installed on target instances according to each instance's operating system type directly or during the defined schedule (maintenance window).

Task 2.1 Patch the Linux instances
Patch the Linux instances.

From the Patch Manager console page, choose Patch now.

Patching operation:  Scan and install

Reboot option: Reboot if needed

Instances to patch: Patch only the target instances I specify

Target selection: Specify instance tags

Tag key:  Patch Group

Tag value: LinuxProd

Choose Add

Choose Patch now

Observe the status of the patching.

A new page displays. In the AWS-PatchNowAssociation panel, there is a Progress field that will show that three instances will be affected and the progress made.

A Scan/Install operation summary panel also displays the status of the affected EC2 instances visually. Monitor this page until the patch operation on all three instances completes.

 

Task 2.2: Patch the Windows instances
Patch the Windows instances.

Choose Patch Manager and then choose Patch now.

Patching operation:  Scan and install

Reboot option: Reboot if needed

Instances to patch: Patch only the target instances I specify

Target selection: Specify instance tags

Tag key:  Patch Group

Tag value: WindowsProd

Choose Add

Choose Patch now

A new page displays. When it becomes available, choose the link to the Execution ID.

A page in the State Manager part of Systems Manager opens.

Choose the Output link for one of the managed instances that shows a status of InProgress.

A page in the Run Command part of Systems Manager opens.

Expand the Output panel to observe the details.

 Behind the scenes, Patch Manager uses the Run Command to run the PatchBaselineOperations.  If you scroll through the output, you should see the PatchGroup: WindowsProd details.

A Systems Manager document (SSM document) defines the actions that Systems Manager performs on your managed instances.

 

Task 2.2: Verify compliance
In the left navigation pane, under Node Management, choose Patch Manager.

Choose the Dashboard tab. Under Compliance summary, you should now see Compliant: 6, which verifies that all Windows and Linux instances are compliant.

Choose the Compliance reporting tab. 
 This tab provides an overview of all running instances with SSM. You should be able to verify that the Compliance status of all Linux and Windows instances is Compliant.

All six instance (three Linux and three Windows) should show as compliant.

Scroll to the right in the Node patching details panel to find for each instance:

Critical noncompliant count

Security noncompliant count

Other noncompliant count

Last operation date 

Baseline ID 

Choose the Node ID for one of the Windows nodes.

In the Node ID page that opens, choose the Patch tab.

Scroll down and observe what patches were applied to this instance, as well as the Installed Time.

Summary of task 2
In this task, you configured patching and patched instances in both the the LinuxProd group and the WindowsProd group. 

You learned how to scan and install patches instantly and analyze the output from the Run command to see the patch updates. You verified through compliance reporting that all EC2 instances have been scanned and updated and are compliant. 

 

Conclusion
 Congratulations! You now have successfully:

Created a custom patch baseline

Modified two patch groups

Configured patching

Verified patch compliance

 

Lab complete
Choose  End Lab at the top of this page, and then choose Yes to confirm that you want to end the lab.

An Ended AWS Lab Successfully message is briefly displayed indicating that the lab has ended.

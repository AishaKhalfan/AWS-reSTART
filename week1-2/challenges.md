Task 1: Create EventBridge Rule and Stop EC2 instances (AppServer1 and AppServer2)
Possible Points: 32 Clue Penalty: 0 Points Available: 32
Background-
While working on Amazon EC2 instances, your manager asks you to find ways to save cost. You as Cloud Engineer found out simple way to stop the EC2 instances in evening when the servers are not in use and start them back next working day morning. For few days you did this activity on multiple servers perfectly but later on this was becoming very tedious for you to manage and there was fear that you may forget stopping and starting any particular server any day.


Your Task-
You are tasked to simplify this manual and complex process to stop and start the EC2 servers. You decided to implement an automated process to automatically stop and start EC2 servers using Lambda code triggered via EventBridge Rule and configured time schedule in EC2 Tags.


Getting Started-
This Task needs you to add an EC2 Tag on instance AppServer2 and create an EventBridge Rule to stop EC2 instances AppServer1 and AppServer2 (with Tag Key AutoStop Value true) triggered via Lambda execution.
In EC2 instance AppServer1 Tags, for Tag Key AutoStop, add Tag Value true or True or TRUE (case insensitive)
In EC2 instance AppServer2 Tags, add Tag Key AutoStop with Tag Value true or True or TRUE (case insensitive)
Create Amazon EventBridge Rule with name AutoStopEC2 and Rule type as Schedule. You will get to choose either Continue to create rule button or Continue in EventBridge Scheduler button.
Click Continue to create rule button, as creating EventBridge Scheduler is currently not supported in JAM AWS Console
Enter Cron expression in format cron(<MM> <HH> ? * MON-SUN *) in GMT or Local time zone. Specify the cron expression so that it runs in next few minutes after it is setup. (e.g., have the cron expression as current Local time + 2 mins). Attach the Rule to existing Lambda Function AutoStopEC2Instance. Additionally, under Scheduler, for Execution role you can choose existing role LambdaSchedulerStartStopRole.
If your Local timezone and Region timezone is different, it's recommended to use UTC and set time after converting local/region time to UTC when you want to execute the Lambda trigger.
This will stop EC2 instances AppServer1 and AppServer2
Lambda execution status can also be checked in CloudWatch Log group /aws/lambda/AutoStopEC2Instance
Notes:

Currently, for Amazon EventBridge Rule, JAM AWS console supports creating Rule using Continue to create rule button only. EventBridge Scheduler service is not supported to run in JAM environment.
This Rule and cron is one-time change only for JAM testing and practically user will pre-set this cron to stop instances as per business needs.


Inventory-
Amazon EC2
Amazon EventBridge Rules
AWS Lambda


Services You Should Use-
Amazon EC2 Tags
Amazon EventBridge Rules
Amazon CloudWatch Logs


Task Validation-
Once both the EC2 instances (AppServer1 and AppServer2) gets stopped, the Task will automatically get validated and Completed successfully.
In addition, you can always check your progress by pressing the “Check my progress” Button in the challenge details screen.
Clues
Penalty: 3 points
Clue 1:Add Tag in EC2 instances (AppServer1 and AppServer2)
Penalty: 4 points
Clue 2:Create EventBridge Rule Cron
Penalty: 4 points
Clue 3:Add Tag in EC2 instances (AppServer1 and AppServer2) and Create EventBridge Rule


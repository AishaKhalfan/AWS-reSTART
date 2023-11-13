#!/bin/bash
aws s3 cp /home/ec2-user/sysops-activity-files/static-website/ s3://ak56/ --recursive --acl public-read


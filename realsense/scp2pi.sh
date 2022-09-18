#!/bin/bash -x

remote_host=$1
if [ -z "$remote_host" ]
  then
    echo "Usage:"
    echo "$0 <remote hostname or IP address>"
    exit 1
fi
echo remote host: $remote_host

remote_user=ubuntu
remote_dir=/home/ubuntu/cv/realsense

#
# Get the IP address of your RPi from your router web app
# ssh ubuntu@192.168.10.101
# 
# To stop running service
# sudo systemctl stop <>.sservice
# 
# Backup the files in device before scp!
# To shutdown, sudo shutdown -h now
#
# https://serverfault.com/questions/318474/how-to-pass-password-to-scp-command-used-in-bash-script

whereis sshpass
OUT=$?
if [ $OUT -eq 0 ];then
   echo "User account found!"
   read -s -p "Enter ssh password : " PASSWORD_SSH;
   set -v #must not echo password variable
   sshpass="sshpass -p $PASSWORD_SSH"
else
   sshpass=""
fi

$sshpass scp realsense_depth.py $remote_user@$remote_host:$remote_dir
$sshpass scp object_distance.py $remote_user@$remote_host:$remote_dir
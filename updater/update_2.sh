#!/bin/bash 
# second script as a super user
# move the output directory to the http server as root 
echo "removing old static website" 
echo "---------------------------" 
rm -rf  /srv/http/www/output 
sleep 1 
echo "copying new static website" 
echo "---------------------------" 
cp -r /home/dirac/web/venv/dirac.one/output /srv/http/www 
sleep 1 
# Then you'll need to change the ownership to avoid security issues  
echo "changing ownership to the new static website" 
echo "---------------------------" 
chown -R http:http /srv/http/www/output 
chown -R http:http /srv/http/www/output/* 
sleep 1 


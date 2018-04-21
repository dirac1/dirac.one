#!/bin/bash 
# -- first script as a normal user --
. /home/dirac/web/venv/updater/activate_venv.sh
. /home/dirac/web/venv/updater/git_path.sh
echo "Activating virtualenv and entering in the git repository"
echo $PWD
echo "-------------------"
sleep 1
git pull origin master
echo "-------------------"
echo "Deleting old output"
rm -rf $blog_path/dirac.one/output
sleep 1
echo "-------------------"
echo "Making the new output"
make html


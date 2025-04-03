import os
os.system("apt update")
os.system("apt upgrade -y")
os.system("pkg install git -y")
os.system("pkg install python -y")

os.system("rm -rf $HOME/401-Tool")

os.system("git clone https://github.com/401Warrex/401-Tool")

os.system("cd 401-Tool")

import os
os.system("echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt")
os.system("echo "dwc2" | sudo tee -a /etc/modules")
os.system("sudo echo "libcomposite" | sudo tee -a /etc/modules")
print("Done configuring.")

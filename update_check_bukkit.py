import time
import subprocess
import re
import requests
import os.path


def main():
        """Check for update"""
        up_to_date()




def remove_html(text):
        """Filter out versions"""
        pattern = re.compile('(\d+\.\d+\.\d+)')
        return re.findall(pattern, str(text))





def get_vers():
        """Request and return craftbukkit downloads"""
        response = requests.get('https://getbukkit.org/download/craftbukkit')
        return remove_html(response.content)[0]




def get_running_ver():
        """Open or Write version file"""
        p = subprocess.Popen("bash /root/mcscript/AutoUpdate/server_version.sh", stdout=subprocess.PIPE, shell=True)
        time.sleep(5)
        f = open('/root/mcscript/AutoUpdate/server.com', 'r')
        runvers = f.read()
        f.close()
        return runvers.replace('"', '')


def up_to_date():
        """Compare version"""
        if str(get_vers()).split() == str(get_running_ver()).split():
                print("Up-to-date! Version: " + get_vers())
                return True
        else:
                print("Updating from v" + get_running_ver() + " to v" + get_vers())
                update()
                return False



def update():
        """Download current craftbukkit.jar and update vers.txt"""
        p = subprocess.Popen("su - <user> -c '/home/<user>/stop.sh'", stdout=subprocess.PIPE, shell=True)
        print(p.communicate())
        time.sleep(10)
#       os.remove("/home/mcservice/craftbukkit.jar")
        url = "https://download.getbukkit.org/craftbukkit/craftbukkit-" + str(get_vers()) + ".jar"
        p = subprocess.Popen("su - <user> -c 'wget " + url + " -O /home/<user>/craftbukkit.jar'", stdout=subprocess.PIPE, shell=True)
        print(p.communicate)
        time.sleep(15)
        p = subprocess.Popen("/sbin/shutdown -r now", stdout=subprocess.PIPE, shell=True)
        return print("Rebooting...")

main()

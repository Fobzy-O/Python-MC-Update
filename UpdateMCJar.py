import time
import subprocess
import re
import requests
import os.path

def main():
    """Check for update"""
    latest = str(get_vers())
    running = str(get_running_ver())
    print("Latest Available: " + latest)
    print("Running Version: " + running)
    if up_to_date():
        return
    update()




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
    if os.path.exists('vers.txt'):
        f = open('vers.txt', 'r')
        runvers = f.read()
        return runvers
        f.close()
    else:
        f = open('vers.txt', 'w')
        f.write(str(get_vers()))
        f.close()
    return
    




def up_to_date():
    """Compare version"""
    if str(get_running_ver()) == str(get_vers()):
        print("Up-to-date!")
        return True
    else:
        print("Updating...")
        update()
        return False



def update():
    """Download current craftbukkit.jar and update vers.txt"""
    p = subprocess.Popen("bash stop.sh", stdout=subprocess.PIPE, shell=True)
    print(p.communicate())
    time.sleep(20)
    with open("craftbukkit.jar", "wb") as file:
        # get request
        url = "https://download.getbukkit.org/craftbukkit/craftbukkit-" + str(get_vers()) + ".jar"
        fileName = 'craftbukkit.jar'
        req = requests.get(url)
        file = open(fileName, 'wb')
        for chunk in req.iter_content(100000):
            file.write(chunk)
        file.close()
    f = open('vers.txt', 'w')
    with open("vers.txt",'w') as file:
        pass
    f.write(str(get_vers()))
    f.close()
    p = subprocess.Popen("bash start.sh", stdout=subprocess.PIPE, shell=True)
    print(p.communicate())
    return print("Updated")
    

main()

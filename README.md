# Python-MC-Update
Python script that automates the checking and installation of Craftbukkit on Unix systems.


## **Installation requirements:**
 `apt install jq python3 -y`
 ------------------------------------------------------
 
 
 **Cron Job**
 ----------------------------------------------------------
 `crontab -e`
 
 `30 3 * * * python3 /root/mcscript/AutoUpdate/update_check_bukkit.py`  
   
   
   
   
 This runs the update checker every day at 3:30AM
 
 
 
 ## Security
 Please create a low-level user that has access to start the minecraft server. In this instance the user is `mcservice`. The update files should be in the `/root/` directory as it runs the updater script as `mcservice`. 

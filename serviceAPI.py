import os
import re
import json
class Service:
    """
    Module `Services`
    Module which display all services present in current system
    User can start and stop services accordingly.
    `self.dic` Dictionary which stores name and status of all services
    `self.li` List that contains cluster of dictionaries
    `self.cmds` Displays all services 
    """
    def __init__(self):
        self.dic={}
        self.li=[]
        self.cmds=os.popen("service --status-all").read().strip().splitlines()
    def check_services(self):
        """
        To check services present in the current system
        """
        count=0
        for cmd in self.cmds:
            split = re.split('[\s]+',cmd)
            count=count+1
            self.dic["no"]=count
            if split[0] =="":
                if split[2]=="+":
                    self.dic["status"]="running"
                if split[2]=="-":
                    self.dic["status"]="stopped"
                self.dic["service"]=split[4] 
            else:
                if split[1]=="+":
                    self.dic["status"]="running"
                if split[1]=="-":
                    self.dic["status"]="stopped"
                self.dic["service"]=split[3] 
                self.dic["action"]="button"
            self.li.append(self.dic.copy())
        return self.li


    def handle_service(self,command,service_name):
        """
        for starting and stoping services
        """      
        if command=="1": 
            os.system("sudo systemctl start {}".format(service_name))
            return True
        elif command=="2":    
            os.system("sudo systemctl stop {}".format(service_name))
            return True
        elif command=="3":   
            os.system("sudo systemctl restart {}".format(service_name))
            return True

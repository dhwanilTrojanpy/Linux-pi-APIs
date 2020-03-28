import os
import time
import shutil
import shlex
from subprocess import Popen, PIPE, STDOUT

class Filemanager:

      
      def FileSize(self,path):
            try:
                  return os.stat(path).st_size
            except FileNotFoundError:
                  return 'File NoT Found'
            
      def AllDirs(self,path='/home',hidden=True):
            data = {}
            alldata = []
            if hidden:
                  dirs = [f for f in os.listdir(path) if not f.startswith('.')]
                  # print(dirs)
                  return dirs
                         
            else :
                  dirs = os.listdir(path)
                  # print(dirs)
                  return dirs
            
      def GetModifyTime(self,path):
            try:
                  return os.stat(path).st_mtime
            
            except FileNotFoundError:
                  return 'File NoT Found'
      
      def WriteFile(self,data,path):
            status = Popen('sudo echo {} | tee {}'.format(shlex.quote(data),path), shell=True, stdin=PIPE, stdout=PIPE, 
                        stderr=STDOUT, close_fds=True)
            status = status.communicate()[0].decode()
            return True if status=='' else status.strip()

      
      def ReadFile(self, fileName):
            data = Popen('sudo cat {}'.format(fileName), shell=True, stdin=PIPE, stdout=PIPE, 
                        stderr=STDOUT, close_fds=True)
            data = data.communicate()[0].decode()
            return data
      
      
      def DelFile(self,filePath): 
            if type(filePath) is list:       
                  for file in filePath:
                        data = Popen('sudo rm {}'.format(file), shell=True, stdin=PIPE, stdout=PIPE, 
                                    stderr=STDOUT, close_fds=True)
                        data = data.communicate()[0].decode().split(':')
                        data = data[len(data)-1].strip()
            else:
                  data = Popen('sudo rm {}'.format(filePath), shell=True, stdin=PIPE, stdout=PIPE, 
                               stderr=STDOUT, close_fds=True)
                  data = data.communicate()[0].decode().split(':')
                  data = data[len(data)-1].strip()
            return True if data =='' else data


      def DelFolder(self,dirPath):
            if type(dirPath) is list: 
                  for dirs in dirPath:
                        data = Popen('sudo rm -rf {}'.format(dirs), shell=True, stdin=PIPE, stdout=PIPE, 
                                    stderr=STDOUT, close_fds=True)
                        data = data.communicate()[0].decode().split(':')
                        data = data[len(data)-1].strip()
            else:
                  data = Popen('sudo rm -rf {}'.format(dirPath), shell=True, stdin=PIPE, stdout=PIPE, 
                              stderr=STDOUT, close_fds=True)
                  data = data.communicate()[0].decode().split(':')
                  data = data[len(data)-1].strip()
            return True if data =='' else data
      
      def MoveFileDirs(self,oldPath, newPath): 
           data = Popen('sudo mv {} {}'.format(oldPath,newPath), shell=True, stdin=PIPE, stdout=PIPE, 
                                    stderr=STDOUT, close_fds	=True)
           data = data.communicate()[0].decode()
           return True if data =='' else data.strip()
      
      def CreatDirs(self,dirPath ):
            data = Popen('mkdir {}'.format(dirPath), shell=True, stdin=PIPE, stdout=PIPE, 
                        stderr=STDOUT, close_fds=True)
            
            data = data.communicate()[0].decode().split(':')
            data = data = data[len(data)-1].strip()
            return True if data =='' else data.strip()
      
      def CopyFileDirs(self,source,dest):
            status = Popen('sudo cp -f {} {} '.format(source,dest), shell=True, stdin=PIPE, stdout=PIPE, 
                        stderr=STDOUT,close_fds=True)
            status = status.communicate()[0].decode()
            return True if status == '' else status.strip()

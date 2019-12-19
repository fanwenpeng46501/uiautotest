import configparser,os
#项目所在路径，以便进行全局路径读取
from common.share import allpath
def ini(section,option):
    con=configparser.ConfigParser()
    con.read(allpath+"/config/config.ini")
    vaule=con.get(section,option)
    return vaule

print(ini("hupu","appPackage"))


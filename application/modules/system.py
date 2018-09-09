import application.lib.file as file
import json
import re

# 获取cpu信息
def cpuinfo():
    cpuinfoFilePath = "/proc/cpuinfo"
    cpuinfo = file.getFile(cpuinfoFilePath)

    index = 0
    cpuinfo_list = []
    tempDict = {}

    for item in cpuinfo.splitlines():
        tmp = item.split(':')
        if (tmp == ['']) :
            continue

        tmp = [tmp[0].strip(), tmp[1].strip()]
        if (tmp[0] == 'processor' and int(tmp[1]) != index):
            index = tmp[1]
            cpuinfo_list.append(tempDict)
            tempDict = {}
        tempDict[tmp[0]] = tmp[1]
    cpuinfo_list.append(tempDict)

    return cpuinfo_list

# 获取内存信息
def meminfo():
    meminfoFilePath = '/proc/meminfo'
    meminfo = file.getFile(meminfoFilePath)
    meminfo_list = {}

    for item in meminfo.splitlines():
        tmp = item.split(':')
        if (tmp == ['']):
            continue

        tmp = [tmp[0].strip(), tmp[1].strip()]
        meminfo_list[tmp[0]] = tmp[1]

    return meminfo_list

# 获取网络信息 数据已经格式化 正则来自 https://github.com/spoonysonny/pi-dashboard/blob/master/device.php
def netinfo():
    netinfoFilePath = '/proc/net/dev'
    netinfo = file.getFile(netinfoFilePath)
    netinfo = netinfo.split('\n')
    temp = {}
    for item in netinfo:
        if (netinfo.index(item)<=1 or item == ''):
            continue
        index = netinfo.index(item) - 2
        itemContent = re.split("([^\s]+):[\s]{0,}(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)", item)
        tmp = {
            "name": itemContent[1],
            "total_in": itemContent[2],
            "total_out": itemContent[10],
        }
        temp[index] = tmp

    return temp

def diskinfo():
    diskinfoFilePath = ''
from flask import Blueprint
from application.modules.system import cpuinfo,meminfo,netinfo
import json
mod = Blueprint('system', __name__)

@mod.route('/system/cpuinfo')
def sysCpuInfo():
    cpuinfo_res = cpuinfo()
    return json.dumps(cpuinfo_res)

@mod.route('/system/meminfo')
def sysMemInfo():
    meminfo_res = meminfo()
    return json.dumps(meminfo_res)

@mod.route('/system/netinfo')
def sysNetInfo():
    netinfo_res = netinfo()
    return json.dumps(netinfo_res)

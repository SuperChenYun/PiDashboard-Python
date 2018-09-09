from flask import Blueprint, render_template
from application.modules.system import cpuinfo,meminfo,netinfo
import json
mod = Blueprint('index', __name__)

@mod.route('/')

def index():
    return render_template('index.html')

@mod.route('/getinfo')
def getinfo():
    cpuinfo_res = cpuinfo()
    meminfo_res = meminfo()
    netinfo_res = netinfo()

    return_data = {
        'cpuinfo': cpuinfo_res,
        'meminfo': meminfo_res,
        'netinfo': netinfo_res
    }
    return json.dumps(return_data)
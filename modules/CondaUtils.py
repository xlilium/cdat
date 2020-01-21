import os
import sys

from Util import *

def get_conda_dir(workdir):
    conda_dir = os.path.join(workdir, 'miniconda')
    return conda_dir

def install_miniconda(workdir, py_ver):
    if os.path.isdir(workdir) == True:
        print("INFO: {dir} already exists".format(dir=workdir))
    else:
        os.mkdir(workdir)

    conda_dir = get_conda_dir(workdir)

    if os.path.isdir(conda_dir) == True:
        print("INFO: {dir} already exists".format(dir=conda_dir))
        print("Conda is already installed.")
        return(SUCCESS, conda_dir)


    url = "https://repo.continuum.io/miniconda"
    conda_script = os.path.join(workdir, 'miniconda.sh')
    if py_ver.startswith('py2'):
        conda_ver = 'Miniconda2'
    else:
        conda_ver = 'Miniconda3'

    if sys.platform == 'darwin':
        conda_script = "{c}-latest-MacOSX-x86_64.sh".format(c=conda_ver)
        conda_script_full_path = os.path.join(workdir, conda_script)
        source_script = os.path.join(url, conda_script)
        cmd = "curl {src} -o {dest}".format(src=source_script, dest=conda_script_full_path)
    else:
        conda_script = "{c}-latest-Linux-x86_64.sh".format(c=conda_ver)
        conda_script_full_path = os.path.join(workdir, conda_script)
        source_script = os.path.join(url, conda_script)
        cmd = "wget {src} -O {dest}".format(src=source_script, dest=conda_script_full_path)

    print("DEBUG...cmd: {c}".format(c=cmd))

    ret_code = run_cmd(cmd, True, False, True)
    if ret_code != SUCCESS:
        print("FAIL..." + cmd)
        return(ret_code, None)

    cmd = "bash {script} -b -p {dir}".format(script=conda_script_full_path, 
                                             dir=conda_dir)

    # run the command, set verbose=False 
    ret_code = run_cmd(cmd, True, False, True)
    if ret_code != SUCCESS:
        print("FAIL...installing miniconda")
        return(ret_code, None)

    cmds_list = ["conda config --set always_yes yes --set changeps1 no",
                 "conda config --set anaconda_upload no",
                 "conda config --add channels conda-forge",
                 "config --set channel_priority strict"]
    
    ret_code = run_in_conda_env(conda_dir, 'base', cmds_list, True)
    if ret_code != SUCCESS:
        print('FAILED: ' + cmd)
        return(ret_code, None)

    print("DEBUG...install_miniconda() returning conda_dir: {p}".format(p=conda_dir))
    return(ret_code, conda_dir)

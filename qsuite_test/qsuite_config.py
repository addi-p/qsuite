import os

#=========== SIMULATION DETAILS ========
projectname = "project"
basename = "experimentname"

seed = -1
N_measurements = 10 #we want 10 measurements for each parameter combination
save_each_run = False #activate, if your simulation output is large (~ 200 MB)


measurements = range(N_measurements)
Ns = [ 1,10,100 ]
Ls = [ 0.5, 1.0, 2.0 ]
Ts = [ 0.5, 1.0, 2.0 ]
Vs = [ 0.5, 1.0, 2.0 ]
rs = [ 0.1, 0.2, 0.3 ]
runtimes = [ 10.0, 100.0, 1000.0 ]
x0s = [ 0., 0.5, 1.0 ] #in units of L
dts = [ 0.001, 0.01]

#this will have BrownianMotions()'s function parameter names
external_parameters = [
                       ( 'L', Ls   ),
                       ( 'r', rs   ),
                       ( None   , measurements ),
                      ]
internal_parameters = [
                       ('N', Ns),
                       ('V', Vs[1:]),
                       ('T', Ts),
                      ]
standard_parameters = [
                       ( 'dt', dts[1] ),
                       ( 'x0', x0s[0] ),
                       ( 'tmax', runtimes[-1] ),
                      ]

only_save_times = False

#============== QUEUE =============================================
#=============== set queing system used at your server          ===
#=============== queue can be one of ['PBS', 'SGE', 'SLURM']    ===
queue = "SLURM"
memory = "1G"
priority = 0

#============ CLUSTER SETTINGS ============
username = "adpe649f"
server = "login1.barnard.hpc.tu-dresden.de"
useratserver = username + u'@' + server
# below the project id of the SynoSys starter project,
# if the computation is part of another project (p_replicatordyn, p_epoch_data), PLEASE specify here
project_id = "p_s_synosys"

shell = "/bin/bash"
pythonpath = "/data/horse/ws/adpe649f-adrians-workspace/my_env/bin/python"
name = basename + "_NMEAS_" + str(N_measurements) + "_ONLYSAVETIME_" + str(only_save_times)
serverpath = "/home/"+username +"/"+ projectname + "/" + name
resultpath = serverpath + "/results"

#============ CLUSTER PREPARATION ==================================================
#======  bash code loading modules to enable python:                      ==========
#======  e.g. "ml purge; ml +development/24.04 +GCCcore/13.3.0 +Python"   ==========
server_cmds = "ml release/24.10 GCCcore/13.2.0 libffi/3.4.4 bzip2/1.0.8 Python/3.11.5"


#============== LOCAL SETTINGS ============
localpath = os.path.join(os.getcwd(),"results_"+name)
n_local_cpus = 1

#============= GIT SETTINGS     ============
# git_repos = [
#                 ( "/path/", server_cmds + "; " + pythonpath + " -m pip install -e . --user" )
#             ]

git_repos = [
               ( "/home/"+username+"/brownian-motion", 
                server_cmds + "; " + pythonpath + " setup.py install --user",
                "https://github.com/PaPeK/qsuite.git" )
            ]
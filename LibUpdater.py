import pkg_resources as pkgres
from subprocess import call

packages = [distribution.project_name for distribution in pkgres.working_set]
call("pip install --upgrade " + ' '.join(packages), shell=True)
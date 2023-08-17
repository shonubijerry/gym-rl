Created at 2023-07-26T1406

Jobs can be submitted either using the launcher script, e.g. type the following then press <enter> key 

 ./StartJupyter-cpu-2023-07-26

Or by using the batch job directly, e.g.

 sbatch /home/706472/jupyter-scripts-2023-07-26/batch-cpu-2023-07-26.job

Viper is a shared resource and at times there may be a other people using the resource. This could mean you will have to wait for resource to become available four your task to start. The launcher script will attempt to return an expected time when the job will begin.

Once your task has started and your Jupyter notebook is available, you should receive an email with connection details which include how to set up your SSH tunnel to allow a local (your PC) browser to connect and the URL to connect to.

If you have any issues, please raise a ticket on the support portal at https://support.hull.ac.uk and search for Viper, if you have a job ID (typically a 7 digit number) please include this.

The following have been created:
Python Virtual Environment:
  If not present already, created the Jupyter enabled Anaconda Python Virtual Environment jupyter-2023-07-26
Launchers - these are wrapper scripts which submit a job using the appropriate batch scripts:
  StartJupyter-cpu-2023-07-26 - Launcher for standerd CPU only tasks
  StartJupyter-gpu-2023-07-26 - Launcher for tasks that require GPU processing
  StartJupyter-highmem-2023-07-26 - Launcher for tasks that require large amounts of memory (over 128GB up to 1TB)
Batch scripts - these are the batch scripts or recipe files that tell Viper what needs to be done. They are effectively a short recipe for how your task should run:
  /home/706472/jupyter-scripts-2023-07-26/batch-cpu-2023-07-26.job - batch script called by launcher for standerd CPU only tasks
  /home/706472/jupyter-scripts-2023-07-26/batch-gpu-2023-07-26.job - batch script used by launcher for GPU tasks
  /home/706472/jupyter-scripts-2023-07-26/batch-highmem-2023-07-26.job - batch script used by launcher for large memory tasks
Supporting file:
  /home/706472/jupyter-scripts-2023-07-26/jupyter-email.sh - a script which sends email with connection details for your notebook
Log file folder - the folder where job logs will be placed:
  /home/706472/jupyter-logs-2023-07-26 
  
Jupyter Creation Tool, v0.1 2022-07-22

import os
from IPython.lib import passwd

c.NotebookApp.ip = '10.214.143.19'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False
#c.MultiKernelManager.default_kernel_name = 'python2'

# sets a password if PASSWORD is set in the environment
if 'PASSWORD' in os.environ:
    c.NotebookApp.password = passwd(os.environ['PASSWORD'])
    del os.environ['PASSWORD']

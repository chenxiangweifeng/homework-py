# -*- coding: utf-8 -*-
import os
import time

cmd1 = "ls -a"
cmd2 = "free -h"
for i in range(1, 20, 1):
    time.sleep(0.1)
    os.system(cmd2)

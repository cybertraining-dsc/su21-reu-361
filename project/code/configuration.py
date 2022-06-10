import os
import yaml
import textwrap
from cloudmesh.common.util import readfile
from cloudmesh.common.FlatDict import FlatDict

def read_config(filename):
    if os.path.exists(filename):
        d = readfile(filename)
    else:
        d = textwrap.dedent("""
        debug: True
        user: "gregor"
        host: "5090X-RTX3090"
        experiments:
            epoch: [1,2,10,20]
            gpu: ["K80","A100","V100","P100"]
        """).strip()
    _config = yaml.safe_load(d)
    config = FlatDict(_config, sep=".")
    return config

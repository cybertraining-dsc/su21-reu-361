---
date: 2021-07-16
title: Tutorial on Using venv in PyCharm
linkTitle: PyCharm venv
tags: ["project", "reu", "tutorial", "venv", "pycharm"]
description: "Setting ENV3 in PyCharm so you will do no harm"
author: Jacques, Fleischer
github_url: https://github.com/cybertraining-dsc/su21-reu-361/edit/main/tutorials/pycharm/pycharm-venv.md
resources:
- src: "**.{png,jpg}"
  title: "Image #:counter"
---


{{% pageinfo %}}

## Abstract

This tutorial teaches how to set PyCharm to use a venv.

Contents

{{< table_of_contents >}}

{{% /pageinfo %}}

**Keywords:** venv


## Windows

Please ensure that you have Git (Git Bash), Python, and PyCharm. If you do not have those, look for the tutorials to install them.

Click the following image to be redirected to a YouTube video tutorial for setting venv in PyCharm. You should skip to timestamp 8:19 unless you do not have Git or a venv, in which case you should watch the entire video.

{{% youtube HCotEx_xCfA %}}

1. Open PyCharm. If this is your first time opening PyCharm, then it will say `Welcome to PyCharm`. Click New Project. If you have used PyCharm before, your previous project should open. Click `File` and `New Project`.
   1. If you would like to change a preexisting project so that it uses a venv, you can open an `.ipynb` or `.py` file, click the box in the top-right that has the Python logo and the name of your current configuration, and click `Edit Configurations...` Note: if it is hard to find this box, it should be next to the green Play button.
    
2. If you followed the tutorial on how to create a venv through Git Bash, you can select `Previously configured interpreter`, click the three dots next to `<No interpreter>`, click the three dots next to `<No interpreter>` again, and then look for the venv. It should be in the C: folder, in the Users directory, in your username directory, in ENV3, Scripts, and then select `python.exe`. Click `OK`.
   1. If you have not created a venv in Git Bash, you can follow the tutorial on how to do that, or you can select the `New environment using Virtualenv` option.
   2. If you are trying to change the settings of a preexisting Python project, try creating a venv in Git Bash so that you can change the Python interpreter to the venv (under the Environment section when you click `Edit Configurations...`)
    
3. Click `OK` after selecting the venv Interpreter, and then click `Create` (if creating a new project). After the project loads, try clicking `Terminal` at the bottom. If it says (ENV3), congratulations!

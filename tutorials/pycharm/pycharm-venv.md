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

This tutorial was created with the REU program in mind, where the students are provided with a GitHub repository. If you are not in REU, then you can create a new repository on GitHub and clone that instead.

Click the following image to be redirected to a YouTube video tutorial for setting venv in PyCharm. Please keep in mind that this video follows directions that are somewhat different from the written instructions below. REU students should follow the written instructions over the video. Otherwise, in the video, you should skip to timestamp 8:19 unless you do not have Git or a venv, in which case you should watch the entire video.

{{% youtube HCotEx_xCfA %}}

1. If you have not already cloned your reu repository, you need to follow a separate tutorial which involves setting up your SSH key on GitHub, which can be found [here](https://github.com/cybertraining-dsc/su21-reu-361/blob/main/tutorials/github/ssh.md).

2. Open PyCharm. If this is your first time opening PyCharm, then it will say `Welcome to PyCharm`. You should have cloned your repo to a particular location on your computer; click `Open` and then locate your reu folder. Once you have found it, click on it so it is highlighted in blue and then click `OK`. Alternatively, if you have used PyCharm before, your previous project should open, in which case you should click `File` and `Open...` to open your repo (if it is not already open).
    
3. Please ensure that you have already configured a venv through Git Bash. If you have not, then read and follow [this tutorial](https://github.com/cybertraining-dsc/su21-reu-361/blob/main/tutorials/python/venv.md).
    
4. In the top-right of PyCharm, click on the button that reads `Add Configuration...`. Click `Add new...` on the left underneath `No run configurations added.` and then scroll and click `Python`. Give this a name; you can just type `Python venv`. Next to `Python interpreter`, choose `Python x.x (ENV3)`. The `x.x` will depend on which version of Python you have. Then click `OK`.
   1. The button might not read `Add Configuration...`. If you have configured a run configuration previously, then you can create a new one. Click the button right next to the green play button in the top-right of PyCharm. Then, it should say `Edit Configurations...` which you must click on. Change the Python interpreter to be the `ENV3` one, as outlined in Step #4.

5. You also have to click `Python x.x` in the bottom-right of PyCharm, next to `main`. From there, choose `Python x.x (ENV3)`. To verify that your virtual environment is working, click on `Terminal` in the bottom-left of PyCharm. Click the `+` (plus) icon next to Local to start a new terminal. It should say `(ENV3)` next to your current working directory. Congratulations!

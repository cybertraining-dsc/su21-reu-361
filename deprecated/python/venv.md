---
date: 2021-07-16
title: Tutorial on Creating a Virtual Python Environment (venv)
linkTitle: Create venv
tags: ["project", "reu", "tutorial", "venv"]
description: "ENV3 is the way to be."
author: Jacques, Fleischer
github_url: https://github.com/cybertraining-dsc/su21-reu-361/edit/main/tutorials/python/venv.md
resources:
- src: "**.{png,jpg}"
  title: "Image #:counter"
---


{{% pageinfo %}}

## Abstract

This tutorial teaches how to create a virtual Python environment so that you can organize your installed pip modules depending on your needs (or on your project).
It is a good idea to always install new modules in a venv instead of using the default system Python.

Contents

{{< table_of_contents >}}

{{% /pageinfo %}}

**Keywords:** venv


## Windows

Please ensure that you have Git (Git Bash) and Python. If you do not have those, look for the tutorials to install them.

Click the following image to be redirected to a YouTube video tutorial for creating a venv (virtual environment). You should skip to timestamp 4:37 unless you do not have Git, in which case you should watch the entire video.

{{% youtube HCotEx_xCfA %}}

1. Open Git Bash by pressing the Windows key, typing `git bash`, and pressing `Enter`.

2. Type `which python` and press `Enter` to ensure that you have Python. It should output the directory where Python is located.
   1. Typing `python --version` and pressing `Enter` should also tell you your Python version.

3. Type `python -m venv ~/ENV3` and press `Enter`. It might take a few seconds to create the virtual environment. It will be called `ENV3`.

4. Once you see the blinking cursor again which tells you that the last command has finished executing, type `source ~/ENV3/Scripts/activate` and press `Enter`. It should say `(ENV3)` which lets you know that the venv has been successfully initialized. Congratulations! Consider reading/watching the tutorials on how to activate the venv in PyCharm or VSCode.


  

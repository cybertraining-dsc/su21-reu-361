---
date: 2021-06-16
title: Tutorial on Installing Python
linkTitle: install Python
tags: ["project", "reu"]
description: "Time for Python"
author: Jacques, Fleischer
github_url: https://github.com/cybertraining-dsc/su21-reu-361/edit/main/tutorials/python/index.md
resources:
- src: "**.{png,jpg}"
  title: "Image #:counter"
---


{{% pageinfo %}}

## Abstract

This tutorial teaches how to install Python on Windows 10.

Contents

{{< table_of_contents >}}

{{% /pageinfo %}}

**Keywords:** python


# Steps

Click the image below to be redirected to a YouTube walkthrough.
<div align="left">
  <a href="https://www.youtube.com/watch?v=T6UYyu5XVMc"><img src="https://img.youtube.com/vi/T6UYyu5XVMc/0.jpg" alt="IMAGE ALT TEXT"></a>
</div>



1. First, open up any web browser. This tutorial utilizes Google Chrome, but any other browser should work as long as it is not a 1990s version of Netscape. (Do not worry— you probably don't have this.) The browser of choice can be Microsoft Edge, Firefox, Opera— as long as it can perform a search on a search engine, access a webpage, and download a file.

2. Click the search box in the bottom left of your screen, where it says "Type here to search". Then, type "google chrome" (or whatever is the name of the browser you use) and click it once it appears.
  - The "Type here to search" box could be missing if you have customized your taskbar (the taskbar is the long box typically located on the bottom of your screen which has icons). In this case, just click the Windows logo in the bottom left and type your browser name.
  - This is just one way to open your browser. You can even click a shortcut to your web browser on your taskbar, on your Desktop, or your Start Menu. In computing, there is typically many ways to accomplish the same end objective.

3. Once your browser has loaded, search for "python" on Google or any search engine. Click the result that reads "Downloads" from the website "python.org".

4. As of mid-2021, the latest version of Python is `3.9.5`. You may see a different number. As long as you click the button under "Download the latest version for Windows", this will work. Try it now.

5. Once the download has completed, open the file by clicking on it in your Downloads pane.
  - If you are utilizing a school-issued computer, you may be prevented from opening this .exe file because you are not the administrator. Please email or otherwise get in contact with your instructor, professor, or head of IT to discuss installing Python.

6. Be sure to check the box that reads "Add Python x.x to PATH". This will allow you to run commands from the terminal/command prompt.

7. Click "Install Now". The default options that entail this selection are appropriate for this experiment's intents and purposes; choosing "Customize installation" may create reproducibility issues down the road, so please select "Install Now" instead.
  - The UAC prompt will pop up. UAC stands for "User Account Control" and exists so that the computer will not have unauthorized changes performed on it. Click "Yes" because Python is safe. School-issued computers may ask for an administrator password, so refer to step 4's sidenote.

8. Sit back and watch the green progress bar, whose speed will depend on the power of the computer.

9. If the setup was successful, then it will say so. Click "Close".

10. Click the "Type here to search" box in the bottom-left of the screen, type "cmd", and press Enter.
  - An alternative method is to press the Windows key and the "R" key at the same time, type "cmd", and press Enter. This is convenient for those who like to use the keyboard.

11. Type `python --version` and the output should read "Python x.x.x"; as long as it is the latest version from the website, congratulations. Python is installed on the computer.

# Troubleshooting

## Incorrect Python Version on Command Prompt

If the computer has installed an older version of Python, running `python --version` on Command Prompt may output an older version. Typing `python3 --version` may output the correct, latest version.




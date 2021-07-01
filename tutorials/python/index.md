---
date: 2021-06-24
title: Tutorial on Installing Python
linkTitle: Install Python
tags: ["project", "reu", "tutorial"]
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


## Windows

Click the following image to be redirected to a 2 minute YouTube walkthrough.
<div align="left">
  <a href="https://www.youtube.com/watch?v=T6UYyu5XVMc"><img src="https://img.youtube.com/vi/T6UYyu5XVMc/0.jpg" alt="IMAGE ALT TEXT"></a>
</div>

{{% youtube T6UYyu5XVMc %}}

1. First, open up any web browser. This tutorial utilizes Google Chrome, but any other browser should work as long as it is not a 1990s version of Netscape. (Do not worry— you probably don't have this.) The browser of choice can be Microsoft Edge, Firefox, Opera— as long as it can perform a search on a search engine, access a webpage, and download a file.
\
&nbsp;

2. Open your browser by clicking the search box in the bottom left of your screen, where it says "Type here to search". Then, type "google chrome" (or whatever is the name of the browser you use) and click it once it appears.
   1. The "Type here to search" box could be missing if you have customized your taskbar (the taskbar is the long box typically located on the bottom of your screen which has icons). In this case, just click the Windows logo in the bottom left and type your browser name.
   2. This is just one way to open your browser. You can even click a shortcut to your web browser on your taskbar, on your Desktop, or your Start Menu. In computing, there is typically many ways to accomplish the same end objective.
 \
&nbsp;

3. Once your browser has loaded, search for "python" on Google or any search engine. Click the result that reads "Downloads" from the website "python.org".
 \
&nbsp;

4. As of June 2021, the latest version of Python is `3.9.5`. You may see a different number. As long as you click the button under "Download the latest version for Windows", this will work. Try it now.
 \
&nbsp;

5. Once the download has completed, open the file by clicking on it in your Downloads pane.
   1. If you are utilizing a school-issued computer, you may be prevented from opening this .exe file because you are not the administrator. Please email or otherwise get in contact with your instructor, professor, or head of IT to discuss installing Python.
 \
&nbsp;

6. Be sure to check the box that reads "Add Python x.x to PATH". This will allow you to run commands from the terminal/command prompt.
 \
&nbsp;

7. Click "Install Now". The default options that entail this selection are appropriate for this experiment's intents and purposes; choosing "Customize installation" may create reproducibility issues down the road, so please select "Install Now" instead.
   1. The UAC prompt will pop up. UAC stands for "User Account Control" and exists so that the computer will not have unauthorized changes performed on it. Click "Yes" because Python is safe. School-issued computers may ask for an administrator password, so refer to step 5's sidenote.
 \
&nbsp;

8. Sit back and watch the green progress bar, whose speed will depend on the power of the computer.
 \
&nbsp;

9. If the setup was successful, then it will say so. Click "Close".
 \
&nbsp;

10. Click the "Type here to search" box in the bottom-left of the screen, type "cmd", and press Enter.
    1. An alternative method is to press the Windows key and the "R" key at the same time, type "cmd", and press Enter. This is convenient for those who like to use the keyboard.
 \
&nbsp;

11. Type `python --version` and the output should read "Python x.x.x"; as long as it is the latest version from the website, congratulations. Python is installed on the computer.


## Mac

Click the following image to be redirected to a 5 minute YouTube walkthrough. (Yes, Mac's video is a little longer, but do not fret!
You can skip to the 1:00 minute mark if you are in a hurry.)

{{% youtube TttmzM-EDmk %}}


1. Open a web browser that is able to search and download a file. This tutorial uses Google Chrome for Mac.


2. Type in `python` in the address bar and press enter. It should perform a search on your default search engine.


3. Look for the result that is from `python.org`. Click on the subresult that says `Downloads`.


4. Underneath `Download the latest version for Mac OS X`, there should be a yellow button that reads `Download Python x.x.x`. Click on it, and the download should commence.


5. Once the download finishes, open it by clicking on it. The installer will open. Click `Continue`, click `Continue` again, click `Continue` again, oh my goodness!


6. Click `Agree`. 
   1. If you want to check how much free storage you have on your computer, click the Apple icon in the top left of your computer. Click
    `About This Mac` and then click on `Storage`. As of July 2021, Python takes ~120 MB of space. Remember that 1 GB = 1000 MB.
      

7. Click `Install`. Enter your password and press Enter. Watch the blue progress bar crawl like a turtle... or blast off at the speed of sound! This depends on your computer speed.


8. A Finder window will open. You can close it as it is unnecessary. Click `Close` in the bottom-right of the installer. Click `Move to Trash` because you do not need the installer anymore.


9. Time to confirm that Python installed correctly. Click the magnifying glass in the top-right of your screen and then type `terminal` into Spotlight Search. Double-click `Terminal`.
   1. The terminal will be used frequently in this experiment. Consider keeping it in the dock for convenience. Click and hold the Terminal in the dock, go to `Options`, and click `Keep in Dock`.
    

10. Type `python3 --version` into the terminal and press Enter. It should output the latest version of Python. Congratulations!


## Troubleshooting

### Incorrect Python Version on Command Prompt

If the computer has installed an older version of Python, running `python --version` on Command Prompt may output an older version. Typing `python3 --version` may output the correct, latest version.




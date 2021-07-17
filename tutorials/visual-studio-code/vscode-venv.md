---
date: 2021-07-16
title: Tutorial on Using venv in VSCode
linkTitle: VSCode venv
tags: ["project", "reu", "tutorial", "venv", "vscode"]
description: "Setting ENV3 in VSCode to go down the best road"
author: Jacques, Fleischer
github_url: https://github.com/cybertraining-dsc/su21-reu-361/edit/main/tutorials/visual-studio-code/vscode-venv.md
resources:
- src: "**.{png,jpg}"
  title: "Image #:counter"
---


{{% pageinfo %}}

## Abstract

This tutorial teaches how to set VSCode to use a venv.

Contents

{{< table_of_contents >}}

{{% /pageinfo %}}

**Keywords:** venv


## Windows

Please ensure that you have Git (Git Bash), Python, and Visual Studio Code. If you do not have those, look for the tutorials to install them.

Click the following image to be redirected to a YouTube video tutorial for setting venv in VSCode. You should skip to timestamp 10:56 unless you do not have Git or a venv, in which case you should watch the entire video.

{{% youtube HCotEx_xCfA %}}

1. You MUST have created a venv in Git Bash before proceeding. Please look for the tutorial on how to create one called `ENV3`.

2. Open Visual Studio Code. Then, press these keys at the same time: `Ctrl + Shift + P`. Type `interpreter` and click on `Python: Select Interpreter`.

3. Select the one that has the path `~\ENV3\Scripts\python.exe`. After clicking that one, it should now say ('ENV3':venv) at the bottom left of the window.

4. We must edit the settings so that the terminal is cmd, not PowerShell (because PowerShell cannot use venv). Press `Ctrl + Shift + P` at the same time again and type `open settings`. Click `Preferences: Open Settings (JSON)`.

5. Scroll down until you see the last curly brace at the very end `}`. Press enter right before that, after the last bracket `]`. On the new line, type `"terminal.integrated.defaultProfile.windows": "Command Prompt"`. Ensure that this line is on the same indentation level as the previous bracket `]` immediately before. Also, add a comma immediately before this bracket so that it reads `],`.
   1. To clarify, the end of the file should look something like this:
    ```      "typescriptreact",
             "yaml",
             "yml",
             "jupyter"
          ],
          "python.venvFolders": [
             "ENV3"
          ],
          "terminal.integrated.defaultProfile.windows": "Command Prompt"
       )
   ```
   It is fine if the end of the file does not read exactly the same. Just make sure that there is the comma after the last bracket and that the indentations check out.

6. Click `File` and click `Save`. Then, close `settings.json` by clicking the `x` on the tab.

7. Open a new terminal by clicking `Terminal` at the top left and click `New Terminal`. It should read (ENV3) in the terminal. Congratulations! 
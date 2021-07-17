---
date: 2021-07-17
title: Tutorial on Adding SSH Key for GitHub Repo 
linkTitle: SSH Key for Repo
tags: ["project", "reu", "tutorial", "ssh", "github"]
description: "Scary SSH Keys are Now a Breeze"
author: Jacques, Fleischer
github_url: https://github.com/cybertraining-dsc/su21-reu-361/edit/main/tutorials/github/ssh.md
resources:
- src: "**.{png,jpg}"
  title: "Image #:counter"
---


{{% pageinfo %}}

## Abstract

This tutorial teaches how to configure an SSH Key on GitHub so that you can clone, commit, pull, and push to repositories (repos).

Contents

{{< table_of_contents >}}

{{% /pageinfo %}}

**Keywords:** ssh


## Windows

Please ensure that you have Git (Git Bash) and a repository on GitHub. This tutorial was created with the REU program in mind, where the students are provided with a GitHub repository. If you are not in REU, then you can create a new repository on GitHub and clone that instead.

1. Open Git Bash by pressing the Windows key, typing `git bash`, and pressing Enter.

2. Then, go on GitHub, click on your profile icon in the top right, click `Settings`, and click `SSH and GPG keys` on the left hand side. Confirm that there are no SSH keys associated with your account. If there are keys, then perhaps you have made some already. This tutorial focuses on creating a new one.

3. Go back to Git Bash and type `ssh-keygen`. Press `Enter`. Press `Enter` again when it asks you the file in which to save the key (it should say `Enter file in which to save the key (/c/Users/USERNAME/.ssh/id_rsa):`.
   1. If you have already created a key here, it will ask you if you would like to overwrite the file. Type `y` and press `Enter`.

4. Enter a password that you will remember for your SSH key. It will not appear as you type it, so make sure you get it right the first time. Press `Enter` after typing the password that you come up with.

5. After seeing the randomart image associated with your SSH, you should be able to type a new command. Type `cat ~/.ssh/id_rsa.pub` and press `Enter`. Your key will appear— remember that this should not be shared with others. The key begins with `ssh-rsa` and it may end with your username. Copy this entire key by clicking and dragging over it, right-clicking, and clicking `Copy`.

6. Return to your web browser which is on the GitHub SSH key settings page. Click the green button that reads `New SSH Key` and type a Title for this key. You should name it something memorable and distinct; for example, if you just generated the key on your desktop computer, a suitable name is `Desktop`. If generated on your laptop, name it `Laptop`, or if you have numerous laptops, differentiate them with distinct names, and so on.
   1. If you only have one computer and you have preexisting keys on this page, maybe some which you do not remember the password to or have fallen out of use, consider deleting them (as long as you are sure this will not break anything).

7. Paste the key into the key box. You should have copied it from Git Bash in Step #5. Then, click the green button that reads `Add SSH key`. Congratulations— you have successfully configured your SSH key. Now we will try cloning your REU repository.

8. Navigate to your repository. It should be in the cybertraining-dsc directory with a name format of `xxxx-reu-xxx`. Once you are on that page, click the green button that reads `Code` with a download symbol. Click the `SSH` option and click on the clipboard next to the link so that you copy it. It should say `Copied!` after you click on it.

9. Decide where you want your repository folder to be stored. This tutorial will clone the repo into the Documents folder. Go back to Git Bash and type `cd ~/Documents` and press `Enter`. It is a good idea to create a folder titled `reu` for organization. Type `mkdir reu` and press `Enter`. Type `cd reu` and press `Enter`. Finally, type `git clone`, and after you put a space after clone, paste the copied link from GitHub. For example, your command should look like this:

```git clone git@github.com:cybertraining-dsc/su21-reu-361.git```

Then, press `Enter`.
   1. The shortcut `Ctrl + V` does not work in Git Bash for pasting. Instead, you can press `Shift + Insert` to paste.

10. Type in your password for your SSH key and press `Enter`. The repo should clone with no issue. You can now type `code .` and press `Enter` to open VSCode in this directory. Click `Yes, I trust the authors` if prompted in VSCode. If you use PyCharm instead of VSCode, you can open it from Windows search; inside of PyCharm, click `File`, `Open...` and then navigate to `C:`, `Users`, your username, `Documents`, and then click on `reu` so it is highlighted in blue and then click `OK`. If PyCharm asks, you can choose to open it in `This Window` or a `New Window`.



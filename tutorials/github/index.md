---
date: 2021-06-29
title: Tutorial on Getting Raw Images on GitHub
linkTitle: Raw Images GitHub
tags: ["project", "reu", "tutorial"]
description: "We need raw images"
author: Jacques Fleischer
github_url: https://github.com/cybertraining-dsc/su21-reu-361/edit/main/tutorials/github/index.md
resources:
- src: "**.{png,jpg}"
  title: "Image #:counter"
---


{{% pageinfo %}}

## Abstract

This tutorial teaches how to get raw images on GitHub to post on your index.md repo (without any errors).

Contents

{{< table_of_contents >}}

{{% /pageinfo %}}

**Keywords:** github


## Steps

1. Upload your image to GitHub in the images directory

2. Once you navigate to the images directory by clicking on it in GitHub, click on the name of the image to view it and then right click the Download button

3. Click `Copy Link` and paste the copied link into your index.md report in this format:

```
![Figure 1](https://github.com/cybertraining-dsc/su21-reu-361/raw/main/project/images/eos-price.png)

**Figure 1:** Type a description of Figure 1 here
```

Make sure that you replace the link by clicking and dragging over the template placeholder link by pasting the link you just copied:

```
![Figure 1](paste-the-link-here)

**Figure 1:** Type a description of Figure 1 here
```

---
date: 2021-07-21
title: Tutorial on Uploading Files to Google Colab
linkTitle: Upload Files Colab
tags: ["project", "reu", "tutorial"]
description: "Google Drive File upload for Google Colab"
author: Jacques Fleischer
github_url: https://github.com/cybertraining-dsc/su21-reu-361/edit/main/tutorials/colab/index.md
resources:
- src: "**.{png,jpg}"
  title: "Image #:counter"
---


{{% pageinfo %}}

## Abstract

This tutorial teaches how to import csv's into a Google Colab .ipynb.

Contents

{{< table_of_contents >}}

{{% /pageinfo %}}

**Keywords:** colab


## Note

There are two different methods on uploading files to Google Colab Jupyter notebooks. One way is to
have the user upload the file to the user's Google Drive before running the notebook. Another way
is to have the notebook ask the user to upload a file from the user's computer directly into the notebook. 
This tutorial outlines both ways.

The notebook code with both methods can be found [here](https://colab.research.google.com/drive/1nUMmLYpz_4fILf6xrJMDWs9_vFFUrZQ6?usp=sharing)

## Read File from Drive

The first cell contains import statements, some of which are not used because the code was taken from an
REU student's code. Nonetheless, it should not be a problem to run the code on Google Colab which
automatically imports such modules.

Cell 1:
```angular2html
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
```

This code will read a csv file using pandas. Before running Cell 2 which immediately follows this paragraph, the user
should upload the csv to the Google Drive of the same Google account which is running the notebook in Colab. The
csv in Cell 2 is titled `kag_risk_factors_cervical_cancer` but please rename it accordingly to match the file
that you would like to upload.

Cell 2:
```angular2html
from google.colab import drive 
drive.mount("/content/gdrive", force_remount=True)
# The next line of code will tell Colab to read kag_risk_factors_cervical_cancer.csv in your Drive (not in any subfolders)
# so you should alter the code to match whichever .csv you would like to upload.
df=pd.read_csv('gdrive/My Drive/kag_risk_factors_cervical_cancer.csv')
# The next two lines of code convert question marks to NaN and converts values to numeric type, consider 
# removing the next two lines if not necessary.
df = df.replace('?', np.nan) 
df=df.apply(pd.to_numeric)
# If this cell successfully runs then it should output the first five rows, as requested in the next line of code
df.head(5)
```

Colab will ask you to click on a blue link and to sign in with your account. Once done, the user must copy a code
and paste it into the box on Colab for authentication purposes. Press `Enter` after pasting it into the box.

If it outputs an error along the lines of "unknown directory" then try rerunning the two cells and ensuring that
your csv is not in any folders inside of Drive. You can also alter the code to point it to a subdirectory, if needed.


## Read File from Direct Upload

Credit to Carlos Theran for creating this code and troubleshooting

Cell 1:
```angular2html
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
```

Cell 2:
```angular2html
from google.colab import files
df = files.upload()
```

After running Cell 2, the user will be prompted to click `Browse...` and to find the file on the user's local
computer to upload. Sometimes trying to upload the file will give this error:

`MessageError: RangeError: Maximum call stack size exceeded.`

... in which case, the user should click the folder icon on the left side of Google Colab window, then the paper
with an arrow icon (to upload a file), then upload the csv you wish to use. Then rerunning Cell 2 is not
necessary, simply proceed to Cell 3. If this still does not work, see [this stackoverflow page](https://stackoverflow.com/questions/53630073/google-colaboratory-import-data-stack-size-exceeded) for further information.

Cell 3:
```angular2html
df=pd.read_csv('kag_risk_factors_cervical_cancer.csv')
# The next two lines of code convert question marks to NaN and converts values to numeric type, consider 
# removing the next two lines if not necessary.
df = df.replace('?', np.nan) 
df=df.apply(pd.to_numeric)
# If this cell successfully runs then it should output the first five rows, as requested in the next line of code
df.head(5)
```

Remember to rename the instances of `kag_risk_factors_cervical_cancer.csv` accordingly so that it matches your file name.

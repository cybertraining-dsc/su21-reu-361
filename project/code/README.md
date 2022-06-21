# Notebook Instructions

To run the prediction program, ensure that you are on a terminal such as Git Bash
with a virtual Python environment already activated.

Then issue the following commands:

```bash
git clone https://github.com/cybertraining-dsc/su21-reu-361.git
cd su21-reu-361/project/code
pip install -r requirements.txt
```

You may create a new config file (ending in `.yaml`) and edit the beginning cells in
`yfinance-lstm-all-figures.ipynb` to use your specific config file. This config file
produces log files, which are necessary to run the next analysis notebook called
`yfinance-lstm-analysis-final.ipynb`. If desired, you may also change the list of
cryptocurrency tickers that are to be predicted.

Issue the following after making your own config file and editing the notebook to
use your config file:

```bash
jupyter nbconvert --to notebook --inplace --execute yfinance-lstm-all-figures.ipynb --ExecutePreprocessor.timeout=600
```

If you would also like to run the analysis script to produce the figures, you must also
change the `filename` variable in the `yfinance-lstm-analysis-final.ipynb` notebook
to use your specific log file. Then issue the following:

```bash
jupyter nbconvert --to notebook --inplace --execute yfinance-lstm-analysis-final.ipynb --ExecutePreprocessor.timeout=600
```

TODO: add requirements.txt, git clone, set up pyenv, make sure the reader knows this
for ease of replication

TODO: add papermill to requirements and create makefile that runs papermill

cp yfinance-lstm.ipynb yfinance-lstm-`hostname`.ipynb
papermill yfinance-lstm-`hostname`.ipynb

This will produce the new notebook with all the results included
An alternative way is to convert the ipynb to python with 
nbconvert ... some options

You can also run this directly in jupyter-lab

jupyter-lab yfinance-lstm-`hostname`.ipynb

Please ensure you have downloaded the code folder. GitHub and git makes this easy
through cloning of the repo. Cloning is impossible without first installing Git.
Alternatively one can download the repository as a ZIP and extract it by clicking
the green Code button on GitHub. Also, an IDE must be installed, such as PyCharm 
or Visual Studio Code.


Once downloaded, open the yfinance-lstm.ipynb in an IDE, preferably in a Python
virtual environment. Tutorials on how to start a virtual environment are in the
tutorials folder of the repo. Then, ensure all the Python modules that are imported
within the first cell of yfinance-lstm.ipynb are installed with pip (preferably
within virtual environment).

Then, click Run All. There will be a prompt to input the ticker of the cryptocurrency.
Enter it, and the program should do the rest.

However, near the end of the program, there is a line that zooms into the axes of
the graph. The parameters should be manually changed so that it zooms into a point
of interest. Because cryptocurrencies have wildly varying prices, this must be
changed on a case-by-case basis.

NOTE: In order to generate the sequential model diagram on Windows, graphviz must
be installed. We recommend that you install graphviz via chocolatey. First install
chocolatey and then run `choco install graphviz`.

---
date: 2021-06-16
title: "Time Series Analysis of Blockchain-Based Cryptocurrency Price Changes"
linkTitle: Time Series Cryptocurrency
tags: ["project", "reu", "blockchain", "investing", "cryptocurrency"]
description: "
This project applies neural networks and Artificial Intelligence (AI) to historical records of high-risk cryptocurrency coins to train a prediction model that guesses their price. The code in this project contains Jupyter notebooks, one of which outputs a timeseries graph of any cryptocurrency price once a csv file of the historical data is inputted into the program. Another Jupyter notebook trains an LSTM, or a long short-term memory model, to predict a cryptocurrency's closing price. The LSTM is fed the open, high, low, adjusted close, and volume of the coin; the close is purposefully excluded because that is what the model is trying to correctly guess. The notebook creates two sets: a training set and a test set to assess the accuracy of the results.

The data is then normalized using manual min-max scaling so that the model does not experience any bias; this also enhances the performance of the model. The original data and the min-max scaled data is plotted as a graph, which should output identical graphs to confirm that the data is not altered— only scaled for the model's convenience. Then, the model is trained using three layers— an LSTM, dropout, and dense layer— minimizing the loss through 50 epochs of training; from this training, an RNN (recurrent neural network) is produced and fitted to the training set. Finally, the notebook plots a line graph of the actual currency price in red and the predicted price in blue."
author: Jacques, Fleischer
github_url: https://github.com/cybertraining-dsc/su21-reu-361/edit/main/project/index.md
resources:
- src: "**.{png,jpg}"
  title: "Image #:counter"
---

[![Check Report](https://github.com/cybertraining-dsc/su21-reu-361/workflows/Check%20Report/badge.svg)](https://github.com/cybertraining-dsc/su21-reu-361/actions)
[![Status](https://github.com/cybertraining-dsc/su21-reu-361/workflows/Status/badge.svg)](https://github.com/cybertraining-dsc/su21-reu-361/actions)
Status: draft, Type: Project


Jacques Fleischer, [su21-reu-361](https://github.com/cybertraining-dsc/su21-reu-361), [Edit](https://github.com/cybertraining-dsc/su21-reu-361/blob/main/project/index.md)

{{% pageinfo %}}

## Abstract

This project applies neural networks and Artificial Intelligence (AI) to historical records of high-risk cryptocurrency coins to train a prediction model that guesses their price. The code in this project contains Jupyter notebooks, one of which outputs a timeseries graph of any cryptocurrency price once a csv file of the historical data is inputted into the program. Another Jupyter notebook trains an LSTM, or a long short-term memory model, to predict a cryptocurrency's closing price. The LSTM is fed the open, high, low, adjusted close, and volume of the coin; the close is purposefully excluded because that is what the model is trying to correctly guess. The notebook creates two sets: a training set and a test set to assess the accuracy of the results.

The data is then normalized using manual min-max scaling so that the model does not experience any bias; this also enhances the performance of the model. The original data and the min-max scaled data is plotted as a graph, which should output identical graphs to confirm that the data is not altered— only scaled for the model's convenience. Then, the model is trained using three layers— an LSTM, dropout, and dense layer— minimizing the loss through 50 epochs of training; from this training, an RNN (recurrent neural network) is produced and fitted to the training set. Finally, the notebook plots a line graph of the actual currency price in red and the predicted price in blue.

Contents

{{< table_of_contents >}}

{{% /pageinfo %}}

**Keywords:** cryptocurrency, investing, business, blockchain. 

## To-do

- [x] My first research on blockchain
- [x] Add blockchain explanation to introduction
- [x] What does blockchain have to do with AI?
- [ ] What codes exist that demonstrate the use of blockchain with AI using Python?
- [ ] What is the code in this project that will be developed?
- [ ] What is the performance of this code?
- [ ] What is my conclusion?
- [ ] Never, ever use the words 'I' or 'my' in a report

## 1. Introduction

Blockchain is *an open, distributed ledger* which records transactions of cryptocurrency. Systems in blockchain are decentralized, which means that these transactions are shared and distributed among all participants on the blockchain for maximum accountability. Furthermore, this new blockchain technology is becoming an increasingly popular alternative to mainstream transactions through traditional banks[^2]. These transactions utilize blockchain-based *cryptocurrency*, which is a popular investment of today's age, particularly in Bitcoin. However, the U.S. Securities and Exchange Commission warns that high-risk accompanies these investments[^1]. 

Artificial Intelligence (AI) can be used to predict the prices' behavior to avoid cryptocurrency coins' severe volatility that can scare away possible investors[^3]. AI and blockchain technology make an ideal partnership in data science; the insights generated from the former and the secure environment ensured by the latter create a goldmine for valuable information. For example, an up-and-coming innovation is the automatic trading of *digital investment assets* by AI, which will hugely outperform trading conducted by humans[^5]. This innovation would not be possible without the construction of a program which can pinpoint the most ideal time to buy and sell. Similarly, AI will be applied in this experiment to predict the future price of cryptocurrencies on a number of different blockchains, including the Electro-Optical System and Ethereum. 

Long short-term memory (LSTM) is a neural network (form of AI) which ingests information and processes data using a *gradient-based learning algorithm*[^6]. This creates an algorithm that improves with additional parameters; the algorithm *learns* as it ingests. LSTM neural networks will be employed to analyze pre-existing price data and to generate the future price in varying timetables, such as ten days, several months, or a year from the last date. This project will provide as a boon for insights into investments with potentially great returns. These findings can contribute to a positive cycle of attracting investors to a coin, which results in a price increase, which repeats.

- [ ] to provide insights for possible investors
- [x] more investors = bigger price/increases. good for investors (a cycle). possible benefits of this project
- [x] explain what LSTM is
- [x] can increase the business and popularity/prosperity of these coins. 
- [ ] it is important bc crypto is up-and-coming, will be mainstream
- [x] end with why the project is good/helpful

## 2. Datasets

This project utilizes yfinance, a Python module which downloads the historical prices of the EOS coin from the first day of its inception on 1 July 2017, to whichever day the program is executed[^4].

![Figure 1](https://raw.githubusercontent.com/cybertraining-dsc/su21-reu-361/main/project/images/eos-price.png)

**Figure 1:** Line graph of EOS price from 1 July 2017 to 22 July 2021. Generated using timeseries_generator.ipynb located in project/code, utilizing price data from Yahoo Finance[^4].

## 3. Architecture

![Figure 2](https://raw.githubusercontent.com/cybertraining-dsc/su21-reu-361/main/project/images/architecture-process.png)

**Figure 2:** The process of producing LSTM timeseries based on cryptocurrency price.

## 4. Implementation

Initially, this project was meant to scrape prices using the BeautifulSoup Python module; however, slight changes in a financial page's website caused the code to break. Thus, the dataset was no longer created within this program but taken from Yahoo Finance, which contained the coins' price from the day to its inception to the present day.

This experiment's code is inspired from Towards Data Science articles by Serafeim Loukas[^7] and Viraf[^11], who explore using LSTM to predict stock timeseries. This program contains adjustments and changes to their code so that cryptocurrency is analyzed instead. This project opts to use LSTM (long short-term memory) to predict the price because it has a memory capacity, which is ideal for a timeseries data set such as cryptocurrency price over time. LSTM can remember historical patterns and use them to inform further predictions; it can also selectively choose which datapoints to use and which to disregard for the model[^8]. For example, this experiment's code excludes the closing price from the model because that is what is predicted; instead, it uses the Open, High, Low, Adj Close, and Volume to guess the closing price.

The model is run through a layer of long short-term memory. Figure 3 showcases the setup of one of these layers.

![Figure 3](https://raw.githubusercontent.com/cybertraining-dsc/su21-reu-361/main/project/images/lstm.png)

**Figure 3:** Visual depiction of one layer of long short-term memory[^9].

When the model was trained, the program generated these line graphs as a result.

![Figure 4](https://raw.githubusercontent.com/cybertraining-dsc/su21-reu-361/main/project/images/prediction-model.png)

**Figure 4:** EOS price overlayed with the latest 200 days predicted by LSTM

![Figure 5](https://raw.githubusercontent.com/cybertraining-dsc/su21-reu-361/main/project/images/prediction-model-zoomed.png)

**Figure 5:** Zoomed-in graph

- [ ] Discuss the transition from beautifulsoup to taking from a kaggle set. Utilizing LSTM neural network to predict future price.
- [ ] have user input a name of a coin like 'eos' or 'bitcoin' and have that stored as a variable so that it is parsed into the url for yahoo finance, python wget's the appropriate corresponding .csv of the inputted coin and analyzes it

## 5. Benchmark

The amount of time it takes to train the 100 epochs for the LSTM is around 2 minutes. A StopWatch module was used from the package cloudmesh-common[^10] to precisely measure the training time.

```
+------------------+--------------------------------------------------------------------------------+
| Attribute        | Value                                                                          |
|------------------+--------------------------------------------------------------------------------|
| cpu              |                                                                                |
| cpu_cores        | 6                                                                              |
| cpu_count        | 12                                                                             |
| cpu_threads      | 12                                                                             |
| frequency        | scpufreq(current=3600.0, min=0.0, max=3600.0)                                  |
| mem.available    | 2.4 GiB                                                                        |
| mem.free         | 2.4 GiB                                                                        |
| mem.percent      | 84.7 %                                                                         |
| mem.total        | 16.0 GiB                                                                       |
| mem.used         | 13.5 GiB                                                                       |
| platform.version | ('10', '10.0.19043', 'SP0', 'Multiprocessor Free')                             |
| python           | 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] |
| python.pip       | 21.1.3                                                                         |
| python.version   | 3.9.5                                                                          |
| sys.platform     | win32                                                                          |
| uname.machine    | AMD64                                                                          |
| uname.node       | Sledgehammer                                                                   |
| uname.processor  | AMD64 Family 23 Model 113 Stepping 0, AuthenticAMD                             |
| uname.release    | 10                                                                             |
| uname.system     | Windows                                                                        |
| uname.version    | 10.0.19043                                                                     |
| user             | Sledgehammer                                                                   |
+------------------+--------------------------------------------------------------------------------+

+-----------------+----------+--------+--------+---------------------+-------+-------+--------------+--------------+---------+----------------------------------------------------+
| Name            | Status   |   Time |    Sum | Start               | tag   | msg   | Node         | User         | OS      | Version                                            |
|-----------------+----------+--------+--------+---------------------+-------+-------+--------------+--------------+---------+----------------------------------------------------|
| Training time   | ok       | 15.924 | 94.377 | 2021-07-22 18:31:57 |       |       | Sledgehammer | Sledgehammer | Windows | ('10', '10.0.19043', 'SP0', 'Multiprocessor Free') |
| Overall time    | ok       | 17.279 | 68.414 | 2021-07-22 18:31:56 |       |       | Sledgehammer | Sledgehammer | Windows | ('10', '10.0.19043', 'SP0', 'Multiprocessor Free') |
| Prediction time | ok       |  0.235 |  1.412 | 2021-07-22 18:32:13 |       |       | Sledgehammer | Sledgehammer | Windows | ('10', '10.0.19043', 'SP0', 'Multiprocessor Free') |
+-----------------+----------+--------+--------+---------------------+-------+-------+--------------+--------------+---------+----------------------------------------------------+
```
 
## 6. Conclusion

At first glance, the results look promising as the predictions have minimal deviation from the true values. However, upon closer look, the values lag by one day, which is a sign that they are only viewing the previous day and mimicking those values. Furthermore, the model cannot go several days or years into the future because there is no data to run on, such as opening price or volume. For future research, tweets can be scraped from Twitter so that a model can guess whether public discussion of a cryptocurrency is favorable or unfavorable (and whether the price will increase as a result).

## 7. Acknowledgments

Thank you to Gregor von Laszewski, Yohn Jairo, and Carlos Theran for their valuable guidance. Furthermore, thank you to Florida A&M University for graciously funding this scientific excursion.

## 8. References

[^1]: Lori Schock, Thinking About Buying the Latest New Cryptocurrency or Token?, [Online resource] 
      <https://www.investor.gov/additional-resources/spotlight/directors-take/thinking-about-buying-latest-new-cryptocurrency-or>


[^2]: Marco Iansiti and Karim R. Lakhani, The Truth About Blockchain, [Online resource] 
      <https://hbr.org/2017/01/the-truth-about-blockchain>


[^3]: Jeremy Swinfen Green, Understanding cryptocurrency market fluctuations, [Online resource] 
      <https://www.telegraph.co.uk/business/business-reporter/cryptocurrency-market-fluctuations/>


[^4]: Yahoo Finance, EOS USD (EOS-USD), [Online resource]
      <https://finance.yahoo.com/quote/EOS-USD/history?p=EOS-USD>


[^5]: Raj Shroff, When Blockchain Meets Artificial Intelligence. [Online resource]
      <https://medium.com/swlh/when-blockchain-meets-artificial-intelligence-e448968d0482>


[^6]: Sepp Hochreiter and Jürgen Schmidhuber, Long Short-Term Memory, [Online resource]
      <https://www.bioinf.jku.at/publications/older/2604.pdf>


[^7]: Serafeim Loukas, Time-Series Forecasting: Predicting Stock Prices Using An LSTM Model, [Online resource]
      <https://towardsdatascience.com/lstm-time-series-forecasting-predicting-stock-prices-using-an-lstm-model-6223e9644a2f>


[^8]: Derk Zomer, Using machine learning to predict future bitcoin prices, [Online resource]
      <https://towardsdatascience.com/using-machine-learning-to-predict-future-bitcoin-prices-6637e7bfa58f>


[^9]: Christopher Olah, Understanding LSTM Networks, [Online resource]
      <https://colah.github.io/posts/2015-08-Understanding-LSTMs/>


[^10]: Gregor von Laszewski, Cloudmesh StopWatch and Benchmark from the Cloudmesh Common Library, [GitHub]
       <https://github.com/cloudmesh/cloudmesh-common>


[^11]: Viraf, How (NOT) To Predict Stock Prices With LSTMs, [Online resource]
       <https://towardsdatascience.com/how-not-to-predict-stock-prices-with-lstms-a51f564ccbca>



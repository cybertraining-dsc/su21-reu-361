---
date: 2021-06-16
title: "Time Series Analysis of Blockchain-Based Cryptocurrency Price Changes"
linkTitle: Time Series Cryptocurrency
tags: ["project", "reu", "blockchain", "investing", "cryptocurrency"]
description: "This project applies neural networks and Artificial Intelligence (AI) to historical records of high-risk cryptocurrency coins to predict future prices; this aims to minimize investment risk."
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

This project applies neural networks and Artificial Intelligence (AI) to historical records of high-risk cryptocurrency coins to predict future prices; this aims to minimize investment risk.

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

## Tutorials

- [x] Install software Visual Studio Code (create video tutorial or written instructions)

## 1. Introduction

Blockchain is *an open, distributed ledger* which records transactions of cryptocurrency. It is decentralized, which means that these transactions are shared and distributed among all participants on the blockchain for maximum accountability. Furthermore, this new *blockchain* technology is becoming an increasingly popular alternative to mainstream transactions through traditional banks[^2]. These transactions utilize blockchain-based *cryptocurrency*, which is a popular investment of today's age, particularly in Bitcoin. However, the U.S. Securities and Exchange Commission warns that high-risk accompanies these investments[^1]. 

Cryptocurrency coins' severe volatility can scare away possible investors[^3], so Artificial Intelligence (AI) can be used to predict the prices' behavior. AI and blockchain technology make an ideal partnership in data science; the insights generated from the former and the secure environment ensured by the latter create a goldmine for valuable information. For example, an up-and-coming innovation is the automatic trading of *digital investment assets* by AI, which will hugely outperform trading conducted by humans[^5]. This would not be possible without the construction of a program which can pinpoint the most ideal time to buy and sell. Similarly, AI will be applied in this experiment to predict the future price of cryptocurrencies on a number of different blockchains, including the Electro-Optical System and Ethereum. 

Long short-term memory is a neural network (form of AI) which ingests information and processes it using a *gradient-based learning algorithm*[^6]. This creates an algorithm that only improves with additional data— it "learns" as it ingests. LSTM neural networks will be employed to analyze pre-existing price data and to generate the future price in varying timetables, such as ten days, several months, or a year from the last date. This project will provide as a boon for insights into investments with potentially great returns. These findings can contribute to a positive cycle of attracting investors to a coin, which results in a price increase, which repeats.

- [ ] to provide insights for possible investors
- [ ] more investors = bigger price/increases. good for investors (a cycle). possible benefits of this project
- [ ] explain what LSTM is
- [ ] can increase the business and popularity/prosperity of these coins. 
- [ ] it is important bc crypto is up-and-coming, will be mainstream
- [ ] end with why the project is good/helpful

## 2. Datasets

This project utilizes a .csv file containing the historical prices of the EOS coin from the first day of its inception on 1 July 2017, to the last scraped day 12 December 2020[^4]. From this data, the project will attempt to predict the prices from the end date until the present day.

## 3. Using Images

![Figure 1](https://raw.githubusercontent.com/cybertraining-dsc/su21-reu-361/main/project/images/eos_price.png)

**Figure 1:** Line graph of EOS price from 1 July 2017 to 12 December 2020. Generated using timeseries_generator.ipynb located in project/code, utilizing price data from a .csv in a Kaggle data set[^4].

## 4. Architecture

- [ ] Discuss the transition from beautifulsoup to taking from a kaggle set. Utilizing LSTM neural network to predict future price.

## 5. Benchmark

Your project must include a benchmark. The easiest is to use cloudmesh-common
 
## 6. Conclusion

A convincing but not fake conclusion should summarize what the conclusion of the project is.

## 7. Acknowledgments

Thank you to Gregor von Laszewski, Yohn Jairo, and Carlos Theran for their valuable guidance. Furthermore, thank you to Florida A&M University for graciously funding this scientific excursion.

## 8. References

[^1]: Lori Schock, Thinking About Buying the Latest New Cryptocurrency or Token?, [Online resource] 
      <https://www.investor.gov/additional-resources/spotlight/directors-take/thinking-about-buying-latest-new-cryptocurrency-or>


[^2]: Marco Iansiti and Karim R. Lakhani, The Truth About Blockchain, [Online resource] 
      <https://hbr.org/2017/01/the-truth-about-blockchain>


[^3]: Jeremy Swinfen Green, Understanding cryptocurrency market fluctuations, [Online resource] 
      <https://www.telegraph.co.uk/business/business-reporter/cryptocurrency-market-fluctuations/>


[^4]: Mehmet Tarik Akcay, Historical Data for Top 20 Coins by Market Cap, [Online resource]
      <https://www.kaggle.com/mtakcy/historical-data-for-top-20-coins-by-market-cap?select=eos.csv>
      
      
[^5]: Raj Shroff, When Blockchain Meets Artificial Intelligence. [Online resource]
      <https://medium.com/swlh/when-blockchain-meets-artificial-intelligence-e448968d0482>
      
      
[^6]: Sepp Hochreiter and Jürgen Schmidhuber, Long Short-Term Memory, [Online resource]
      <https://www.bioinf.jku.at/publications/older/2604.pdf>




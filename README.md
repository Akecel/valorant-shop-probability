# Valorant Shop Probability Simulator 🚀
Algorithm simulating the number of days it takes for the skin you want to appear in the game store

## Configuration
First of all, there are several variables to configure in order to use this simulator

- **purchasableSkins**: Here you can specify the **amount of skins** available for purchase in the Valorant store. (Do not count agent skin or battlepass skins)

- **ownedSkins**: Also, you can specify **how many of them you already own** (shouldn't include the ones you got from the battle pass or agent one, because they can't be bought in the shop).

- **averageDayBetweenPurchase**: Average number of days between each skin purchase on your part (if you buy an average of 1 skin per month, then this number will be 30 (30 days).

- **numberOfTests**: You can also specify the **number of tests** you want to run. As an output you will have an average of days to get what you want.
(10k+ will probably take a few minutes to run).


```python
purchasableSkins = 347
ownedSkins = 20
averageDayBetweenPurchase
numberOfTests = 1000
```

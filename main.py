import random
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

purchasableSkins = 347 # Ammount of valorant skins that are purchasable from the store.
ownedSkins = 20 # Owned skins.
averageDayBetweenPurchase = 30 # Average number of days between each skin purchase.
numberOfTests = 1000 # Number of times you want to test the algorithm (an avarage value of days will be calculated).

bestCase = float('inf')
worstCase = float('-inf')

avarage = 0
daysArray = []
playerArray = []

for controle in range(numberOfTests):
  validPurchaasableSkins = purchasableSkins - ownedSkins # Actual purchasable skins
  wantedSkin = random.randint(1,validPurchaasableSkins) # Randomly choose wanted skin
  daysCounter = 0
  foundAnySkin = False

  playerArray.append(controle)

  while not foundAnySkin:

    daysCounter = daysCounter+1

    if daysCounter % 15 == 0:
      validPurchaasableSkins = validPurchaasableSkins+5 # Add five new skins every 15 days

    if daysCounter % averageDayBetweenPurchase == 0:
      validPurchaasableSkins = validPurchaasableSkins-1 # Buy 1 new skins every *validPurchaasableSkins* days

    skinsOfTheDay = []
    for i in range(4):
      aux = random.randint(1,validPurchaasableSkins)
      while (aux in skinsOfTheDay): # If the skin is already selected for today store,
        aux = random.randint(1,validPurchaasableSkins) # Randomly choose another, because Valorant doesn't show up the same skin twice in the same day
      skinsOfTheDay.append(aux)
    if wantedSkin in skinsOfTheDay:
      foundAnySkin = True
  if daysCounter < bestCase: # Find best case
    bestCase = daysCounter
  if daysCounter > worstCase: # Find worst case
    worstCase = daysCounter
  daysArray.append(daysCounter)
  avarage = avarage + daysCounter # Avarage calculation (1)

avarage = avarage/numberOfTests # Avarage calculation (2)

print("Ammount of tests X Time to get the skin")
print("Ammount of tests executed : ", numberOfTests)

print("For the selected number of tests the avarage in day(s) to get ANY of the skins you want is: ", round(avarage), " days.")
print("\nIn the BEST case, it took ", bestCase, " day(s) to find any of the desired skins.")
print("In the WORST case, it took ", worstCase, " day(s) to find any of the desired skins.")

df = pd.DataFrame({ 'Player_ID': playerArray, 'Days': daysArray })
df.head()

print("Total Tests: ", controle+1, "\n")

fiveDays = df['Days'][df['Days'] <= 5].count()
print(fiveDays, " test(s) - 5 days or less")

tenDays = df['Days'][df['Days'] <= 10].count()
print(tenDays, " test(s) - 10 days or less")

OneMonth = df['Days'][df['Days'] <= 31].count()
print(OneMonth, " test(s) - 1 month or less")

twoMonths = df['Days'][df['Days'] <= 60].count()
print(twoMonths, " test(s) - 2 months or less")

threeMonths = df['Days'][df['Days'] <= 90].count()
print(threeMonths, " test(s) - 3 months or less\n")

oneToThreeMonths = df['Days'][df['Days'] <= 90][df['Days'] >= 30].count()
print(oneToThreeMonths, " test(s) - 1 to 3 months")

threeToSixMonths = df['Days'][df['Days'] <= 180][df['Days'] >= 90].count()
print(threeToSixMonths, " test(s) - 3 to 6 months\n")

moreThanSixMonths = df['Days'][df['Days'] > 180].count()
print(moreThanSixMonths, " test(s) - more than 6 months")

oneYear = df['Days'][df['Days'] >= 365].count()
print(oneYear, " test(s) - at least 1 year\n")

plt.figure()
plt.title('Time (Days) To Get Skin X Ammount of tests')
plt.hist(daysArray, orientation='horizontal')
plt.ylabel('Days')
plt.xlabel('Tests')
plt.grid()
plt.figure()

plt.plot(daysArray, playerArray)
plt.title('Player ID X Days To Find')
plt.xlabel('Days')
plt.ylabel('Player')
plt.show()

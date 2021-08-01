import pandas as pd

data = pd.read_csv("data_adult.csv")
data.head()
print(data)
# 1. Сколько мужчин и женщин (признак sex) представлено в этом наборе данных?
sumMale = sum(data.sex == "Male")
sumFemale = sum(data.sex == "Female")
print("Мужчин: ", sumMale, " Девушек: ", sumFemale)

# 2. Каков средний возраст (признак age) женщин?
print("Средний возраст женщин: ", data.loc[data["sex"] == "Female","age"].mean())

# 3. Какова доля граждан Германии (признак native-country)?
sumGerman = sum(data.native_country == "Germany")
print("Доля граждан Германии: ", sumGerman / len(data))

# 4-5. Каковы средние значения и среднеквадратичные отклонения возраста тех, кто получает более 50K в год
# (признак salary) и тех, кто получает менее 50K в год?
dataMean = data.groupby("salary")[["age"]].mean()
dataStd = data.groupby("salary")[["age"]].std()

print(dataMean, "\n", dataStd)
# очень понравилось 4-5!

# 6. Правда ли, что люди, которые получают больше 50k, имеют как минимум высшее образование? (признак
# education – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters или Doctorate)
print(data[data.salary == ">50K"]["education"].value_counts())

# 7. Выведите статистику возраста для каждой расы (признак race) и каждого пола. Используйте groupby и describe. Найдите
# таким образом максимальный возраст мужчин расы Amer-Indian-Eskimo.
print(data.groupby("race")["age"].describe())


print("\n")
# 8. Среди кого больше доля зарабатывающих много (>50K): среди женатых или холостых мужчин (признак marital-status)?
# Женатыми считаем тех, у кого marital-status начинается с Married (Married-civ-spouse, Married-spouse-absent или Married-AF-spouse), остальных считаем холостыми.

# ну тут надо сгруппировать по статусу женат или нет с полем зп А describe тут опишет каждую группу
print(data.groupby(["marital_status", "salary"]).describe())

# 9. Какое максимальное число часов человек работает в неделю (признак hours-per-week)? Сколько людей работают такое
# количество часов и каков среди них процент зарабатывающих много?
print("Максимальное кол-во часов: ", data["hours_per_week"].max())
maxHours = data["hours_per_week"].max()
print(data[data["hours_per_week"] == maxHours].count())
# а как взять процент зарабатывающих >50К от этих остается вопросом


# 10. Посчитайте среднее время работы (hours-per-week) зарабатывающих мало и много (salary)
# для каждой страны (native-country).
print(data.groupby(['native_country' == "Japan", 'salary'])[['hours_per_week']].mean())




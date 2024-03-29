import csv

def read_titanic():
    data = {}
    with open("titanic.csv") as titanic_data:
        reader = csv.DictReader(titanic_data, delimiter=',', quotechar="\"")
        for line in reader:
            for k, v in line.items():
                if k not in data:
                    data[k] = []
                data[k].append(v)
    return data


def clean_age(data):
    ages = data["Age"]
    for i, a in enumerate(ages):
        if a == "":
            a = "0"
        ages[i] = float(a)
    data["Age"] = ages


b7fa877e356858c
:
    clean_age(data)
    return sum(data["Age"]) / len(data["Age"])


if __name__ == "__main__":
    titanic_data = read_titanic()
    mean_age = average_age(titanic_data)

    print("Age Moyen :", mean_age)

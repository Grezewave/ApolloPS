import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)

    total_above_40 = 0
    high_cholesterol_above_40 = 0
    high_cholesterol_and_high_fbs_above_40 = 0
    high_cholesterol_high_fbs_hypertrophy_above_40 = 0

    for row in reader:
        age = float(row[0])
        chol = float(row[4])
        fbs = float(row[5])
        restecg = float(row[6])

        if age > 40:
            total_above_40 += 1

            if chol > 240:
                high_cholesterol_above_40 += 1

                if fbs == 1:
                    high_cholesterol_and_high_fbs_above_40 += 1

                    if restecg == 2:
                        high_cholesterol_high_fbs_hypertrophy_above_40 += 1

    percentage_high_cholesterol_above_40 = (
        high_cholesterol_above_40 / total_above_40) * 100
    percentage_high_cholesterol_and_high_fbs_above_40 = (
        high_cholesterol_and_high_fbs_above_40 / total_above_40) * 100
    percentage_high_cholesterol_high_fbs_hypertrophy_above_40 = (
        high_cholesterol_high_fbs_hypertrophy_above_40 / total_above_40) * 100


print("Porcentagem de pessoas acima de 40 anos com colesterol alto: {:.2f}%".format(
    percentage_high_cholesterol_above_40))
print("Porcentagem de pessoas acima de 40 anos com colesterol alto e alto teor de açúcar no sangue: {:.2f}%".format(
    percentage_high_cholesterol_and_high_fbs_above_40))
print("Porcentagem de pessoas acima de 40 anos com colesterol alto e alto teor de açúcar no sangue com hipertrofia ventricular esquerda no coração: {:.2f}%".format(
    percentage_high_cholesterol_high_fbs_hypertrophy_above_40))

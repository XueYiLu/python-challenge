import csv

def analyze_financial_data(csv_file_path):
    total_months = 0
    net_total = 0
    previous_profit_loss = 0
    changes = []
    months = []

    with open(csv_file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)

        for row in csvreader:
            date = row[0]
            profit_loss = int(row[1])

            total_months += 1
            net_total += profit_loss

            if total_months > 1:
                change = profit_loss - previous_profit_loss
                changes.append(change)
                months.append(date)

            previous_profit_loss = profit_loss

    average_change = sum(changes) / len(changes)

    greatest_increase = max(changes)
    greatest_increase_date = months[changes.index(greatest_increase)]

    greatest_decrease = min(changes)
    greatest_decrease_date = months[changes.index(greatest_decrease)]

    result = {
        "Total Months": total_months,
        "Total": net_total,
        "Average Change": average_change,
        "Greatest Increase in Profits": {
            "Date": greatest_increase_date,
            "Amount": greatest_increase
        },
        "Greatest Decrease in Profits": {
            "Date": greatest_decrease_date,
            "Amount": greatest_decrease
        }
    }

    return result

def print_and_export_results(results, output_file_path):
    # Print the results to the terminal
    print("Financial Analysis")
    print("----------------------------")
    for key, value in results.items():
        if isinstance(value, dict):
            print(f"{key}:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}: {sub_value}")
        else:
            print(f"{key}: {value}")

    # Export the results to a text file
    with open(output_file_path, 'w') as output_file:
        for key, value in results.items():
            if isinstance(value, dict):
                output_file.write(f"{key}:\n")
                for sub_key, sub_value in value.items():
                    output_file.write(f"  {sub_key}: {sub_value}\n")
            else:
                output_file.write(f"{key}: {value}\n")

if __name__ == "__main__":
    # The path to the CSV file
    csv_file_path = "/Users/xueyilu/Desktop/Github/python-challenge/PyBank/Resources/budget_data.csv"

    # The output text file path
    output_file_path = "/Users/xueyilu/Desktop/Github/python-challenge/PyBank/Analysis/analyze_financial_data.txt"

    # Call the analyze_financial_data function
    financial_results = analyze_financial_data(csv_file_path)

    # Print and export the results
    print_and_export_results(financial_results, output_file_path)

    print(f"Financial analysis results exported to '{output_file_path}'.")

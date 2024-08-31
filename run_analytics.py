from analytics_tool import AnalyticsTool

def main():
    # Path to the CSV file and the target column name
    data_file = "large_ecommerce_customer_data.csv"
    target_column = "age"

    tool = AnalyticsTool(data_file)

    # Clean the data
    tool.clean_data()

    # Visualize the data
    tool.visualize_data()

    # Perform predictive modeling
    mse, r2 = tool.predictive_modeling(target_column)

    # Output the results
    print(f"Mean Squared Error: {mse}")
    print(f"R^2 Score: {r2}")

if __name__ == "__main__":
    main()

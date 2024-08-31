# Python-based Analytics Tool

This project is a Python-based analytics tool that performs data cleaning, exploratory data analysis, and basic predictive modeling on complex datasets. It uses libraries such as Pandas, Matplotlib, Seaborn, and scikit-learn to process, visualize, and save data insights efficiently.

## Features

- Data cleaning: Removes duplicates, handles missing values, and converts date columns to datetime objects.
- Exploratory data analysis: Generates summary statistics and visualizations.
- Data visualization: Creates pair plots and correlation heatmaps, which are saved as image files.
- Basic predictive modeling: Implements linear regression for predictive analysis.
- Visualization output: Saves generated visualizations (pair plots and heatmaps) as image files (pairplot.png and heatmap.png).

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/kananpalya/python-analytics-tool.git
   cd python-analytics-tool
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Place your CSV data file in the project directory.

2. Modify the `run_analytics.py` file to specify your data file and target column:
   ```python
   if __name__ == "__main__":
    data_file = 'large_ecommerce_customer_data.csv'  # Specify your CSV file here
    target_column = 'age'  # Specify your target column here
    # ...(remaining code)
   ```

3. Run the script:
   ```
   python data_generation.py  # Run if you don't have data
   python run_analytics.py

   ```

4. Check the output in the console and the generated visualization files in the project directory.

## Requirements

- Python 3.7+
- pandas
- matplotlib
- seaborn
- scikit-learn

See `requirements.txt` for specific version information.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
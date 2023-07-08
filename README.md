# Python Challenge: PyBank and PyPoll

This repository contains two Python projects, PyBank and PyPoll, which analyze financial records and election data, respectively. Each project has its own set of instructions and data files.

## Project Structure

The repository has the following structure:

- `PyBank` folder: Contains the PyBank project files.
  - `PyBank_main.py`: The main script to run the financial analysis.
  - `Resources` folder: Contains the `budget_data.csv` file with the financial dataset.
  - `analysis` folder: Will store the text file with the analysis results.

- `PyPoll` folder: Contains the PyPoll project files.
  - `PyPoll_main.py`: The main script to run the vote analysis.
  - `Resources` folder: Contains the `election_data.csv` file with the poll data.
  - `analysis` folder: Will store the text file with the analysis results.

## PyBank Instructions

In the PyBank project, the goal is to analyze the financial records of a company provided in the `budget_data.csv` file. The analysis will calculate the following values:

- The total number of months included in the dataset.
- The net total amount of "Profit/Losses" over the entire period.
- The changes in "Profit/Losses" over the entire period and the average of those changes.
- The greatest increase in profits (date and amount) over the entire period.
- The greatest decrease in profits (date and amount) over the entire period.

The analysis will be printed to the terminal and exported to a text file.

## PyPoll Instructions

In the PyPoll project, the objective is to help a small, rural town modernize its vote-counting process using the `election_data.csv` file. The analysis will calculate the following values:

- The total number of votes cast.
- A complete list of candidates who received votes.
- The percentage of votes each candidate won.
- The total number of votes each candidate won.
- The winner of the election based on popular vote.

Try to run it as a "Debug Python file" and the analysis will be printed to the terminal and exported to a text file. 

## Getting Started

To run either PyBank or PyPoll, ensure you have Python installed on your machine. Clone this repository and navigate to the respective project folder. Make sure the required CSV data files are placed in the appropriate `Resources` folder.

Next, execute the `main.py` script to perform the analysis. The results will be displayed in the terminal and stored in the `analysis` folder as a text file.


## Dependencies

Both projects utilize the `csv` module, which is a built-in module in Python, and do not require any external dependencies.

Feel free to explore and analyze the financial records in PyBank or the poll data in PyPoll. Happy coding!

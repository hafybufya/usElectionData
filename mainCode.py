import pandas as pd
import matplotlib.pyplot as plt
csv_in_use = "usData.csv"

prompt_number_bins = "How many bins for the histogram?"
prompt_candidate = "What candidate would you like to generate a histogram for"

min_number_bins = 5
max_number_bins = 50

prompt_error_handling= "Values must fall in the range"


def read_election_data():
    '''
    reads historicalData.csv file and parses the year column as a date and sets it as an index
    '''
    og_df = pd.read_csv(csv_in_use, delimiter=';')
    election_df = (
    og_df.groupby(["state", "candidate"])["fraction_votes"]
    .sum()
    .reset_index()    
)
    return election_df

election_df = read_election_data()

def get_number_bins():
    """function which gets the day of the week the month starts on and preforms error handling """               
    while True:
        try:
            number_bins  = int(input(prompt_number_bins))
            if min_number_bins <= number_bins  <= max_number_bins :
                return number_bins
            else:
                print(f"{prompt_error_handling} {prompt_number_bins} to {max_number_bins}")
        except ValueError:
            print(f"{prompt_error_handling} {min_number_bins} to {max_number_bins}")

            return number_bins
    
number_bins = get_number_bins()


def get_candidate_name():
    list_of_candidates = election_df['candidate'].unique()
    for candidate in list_of_candidates:
        print(candidate, ",")
    while True:
        candidate = input("Enter the candidate name exactly as shown above:")
        
        if candidate in list_of_candidates:
            return candidate
        else:
            print("Invalid candidate name. Please choose from the list above.")

candidate_name = get_candidate_name()


def plot_histogram():
    individual_candidate_df = election_df[election_df['candidate'] == candidate_name].copy()
    plt.hist(individual_candidate_df["fraction_votes"], bins=number_bins, edgecolor="black")
    plt.title(f"Vote Fraction Distribution for {candidate_name}")
    plt.xlabel("Fraction of Votes")
    plt.ylabel("Number of States")
    plt.show()

plot_histogram()



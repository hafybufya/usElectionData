# ---------------------------------------------------------------------
# IMPORTED FUNCTIONS USED IN PROGRAM
# ---------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------
# Defined CSV file name, prompts and values used in program
#  -> make the code flexible if used dataset changed
#  -> or to reuse the same function for a different file.
# ---------------------------------------------------------------------

csv_in_use = "usData.csv"

# Min and max number of bins in histogram
min_number_bins = 5
max_number_bins = 50

# Prompts and error handling for bins
prompt_number_bins = "How many bins for the histogram?"
prompt_error_handling= "Values must fall in the range:"

# Prompts and error handling for candiate name
prompt_candidate = "Enter the candidate name exactly as shown above:"
prompt_error_candidate = "Invalid candidate name. Please choose from the list above."

bins_error_message =  f"{prompt_error_handling} {min_number_bins} to {max_number_bins}"

# ---------------------------------------------------------------------
# FUNCTION: Read CSV data into Dataframe
# ---------------------------------------------------------------------

def read_election_data():
    """

    Loads the US election dataset definied in 'csv_in_use

    Returns
    -------

    pandas Dataframe -> converts csv to df containing US election data
    grouped by state, candiate and fraction of votes. 

    """

    og_df = pd.read_csv(csv_in_use, delimiter=';')
    election_df = (
    og_df.groupby(["state", "candidate"])["fraction_votes"]
    .sum()
    .reset_index()    
)
    # Returned to be used in  plot_histogram()
    return election_df

# Initiliased in main code so can be used in unitTest.py
election_df = read_election_data()

# ---------------------------------------------------------------------
# FUNCTION: Get number of bins from user
# ---------------------------------------------------------------------

def get_number_bins():
    """

    Asks user for number of bins to pass in for histogram

    Paramters
    ---------

    number_bins : integer, without user input = None so can be unit tested


    Returns
    -------

    integer -> integer from user input between 5 to 50 

    """

    while True:
        try:
            number_bins  = int(input(prompt_number_bins))
        # Users can't input strings
        except ValueError:
            raise ValueError(f"{bins_error_message}")
      
        # Users can't input values smaller than min and larger than max
        if number_bins < min_number_bins or number_bins > max_number_bins: 
            raise ValueError(f"{bins_error_message}")     
        
        # Returned to be passed into plot_histogram()
        return number_bins


# ---------------------------------------------------------------------
# FUNCTION: Get candidate name from user
# ---------------------------------------------------------------------

def get_candidate_name():
    """

    Asks user for name of candidate to pass into histogram

    Paramters
    ---------

    candiate : string, without user input = None so can be unit tested


    Returns
    -------

    string -> candiate name which is found in the list 

    """
    # Gets all the individual names from csv in candiate column
    list_of_candidates = election_df['candidate'].unique() 
    for candidate in list_of_candidates:
        print(candidate, ",") # Places results on different lines seperates by ','
   
    while True:
        candidate = input(prompt_candidate)
        if candidate not in list_of_candidates:
            raise ValueError(prompt_error_candidate)
        return candidate


# ---------------------------------------------------------------------
# FUNCTION: Plot histogram
# ---------------------------------------------------------------------

def plot_histogram(number_bins = None , candidate_name= None ):
    """

    Creates a histogram using candidate name and number of bins user selected 

    
    Parameters
    ----------

    number_bins    :     returned from get_number_bins function, integer
    candidate_name :     returned from get_candidate_name function, integer


    
    Returns
    -------

    matplotlib histogram -> histogram with Fraction of Votes on the x axis
                            and Number of States on the y axis
                                

    """
    # Mask to get only user selected candiate  data
    individual_candidate_df = election_df[election_df['candidate'] == candidate_name].copy()
    # Number of bins from get_number_bins()
    plt.hist(individual_candidate_df["fraction_votes"], bins=number_bins, edgecolor="black")
    plt.title(f"Vote Fraction Distribution for {candidate_name}")
    plt.xlabel("Fraction of Votes")
    plt.ylabel("Number of States")
    plt.show()



# run program
if __name__ == "__main__":

    number_bins = get_number_bins()
    candidate_name = get_candidate_name()
    plot_histogram(number_bins, candidate_name)




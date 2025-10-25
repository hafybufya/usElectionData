import pandas as pd
import matplotlib.pyplot as plt
csv_in_use = "usdata.csv"
y_axis = "Close/Last"
# colors for plots
colour_1 = "#2596be"


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





def plot_histogram():
    pass




#mask to get election data 
# masked_state = election_df[election_df['state'] == 'Vermont'].copy()
# print(masked_state)

# masked_candidate = masked_state[masked_state['candidate'] == 'John Kasich'].copy()
# print(masked_candidate)


# #x axis = state and which fraction of the vote support each candidate
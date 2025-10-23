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
   
    election_df = pd.read_csv(csv_in_use, delimiter=';')
    return election_df
election_df = read_election_data()

print(election_df)


def fractional_votes_state():
    pass




def plot_histogram():
    pass




#mask to get OECD data 
masked_state = election_df[election_df['state'] == 'Vermont'].copy()
print(masked_state)

masked_candidate = masked_state[masked_state['candidate'] == 'John Kasich'].copy()
print(masked_candidate)


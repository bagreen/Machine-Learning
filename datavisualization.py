import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
    # gets the axes from the graph
    ax = plt.gca()

    # creates the dataframe from the adult.data file
    df = pd.read_csv('adult.data')

    # just selects people with  a high school degree
    hs = df.loc[df['education-num'] == 9]

    # just selects people with some college experience
    somecollege = df.loc[df['education-num'] == 10]

    # just selects people with a bachelors degree
    bachelors = df.loc[df['education-num'] == 13]

    # just selects people with a masters degree
    masters = df.loc[df['education-num'] == 14]
        
    # plot it
    hs.plot(kind='scatter', x='capital-gain', y='hours-per-week', ax=ax, color='r', label='High School Degree')
    somecollege.plot(kind='scatter', x='capital-gain', y='hours-per-week', ax=ax, color='m', label='Some College')
    bachelors.plot(kind='scatter', x='capital-gain', y='hours-per-week', ax=ax, color='b', label='College Degree')
    masters.plot(kind='scatter', x='capital-gain', y='hours-per-week', ax=ax, color='g', label='Masters Degree')

    # title and labels
    plt.title('Total Net Worth in Dollars by Hours per Week Worked')
    plt.xlabel('Net Worth in Dollars')
    plt.ylabel('Hour Per Week Worked')


    plt.show()

if __name__ == '__main__':
    main()

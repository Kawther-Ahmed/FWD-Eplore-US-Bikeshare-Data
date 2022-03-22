import time
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}
MONTH_DATA = {
              'january' : 1,
              'february' : 2,
              'march' : 3,
              'april' : 4,
              'may' : 5,
              'june' : 6,
              'july' : 7,
              'august' : 8,
              'september' : 9,
              'october' : 10,
              'november' : 11,
              'december' : 12,
}
DAY_DATA = {
            'monday' : 0,
            'tuesday' : 1,
            'wednesday' : 2,
            'thursday' : 3,
            'friday' : 4,
            'saturday' : 5,
            'sunday' : 6,
}


def get_key(dictionary, val):
    for key, value in dictionary.items():
        if val == value:
            return key
    return "key doesn't exist"


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥--INPUT CITY--♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please enter the name of City (chicago, new york city, washington): ").lower()
    while city not in CITY_DATA:
        city = input("Please enter the correct name of City (chicago, new york city, washington)': ").lower()

    #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥--INPUT MONTH--♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    # get user input for month (all, january, february, ... , june)
    month = input("Please enter the name of Month (all, january, february, ... , june): ").lower()
    while month != 'all':
        if month in MONTH_DATA:
            break
        else:
            month = input("Please enter the correct name of Month (all, january, february, ... , june): ").lower()

    #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥--INPUT DAY--♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please enter the name of Day (all, monday, tuesday, ... sunday): ").lower()
    while day != 'all':
        if day in DAY_DATA:
            break
        else:
            day = input("Please enter the correct name of Day (all, monday, tuesday, ... sunday): ").lower()
    
    print('♥'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥--LOAD CITY--♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    df = pd.read_csv(CITY_DATA[city])

    #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥--LOAD MONTH--♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    list1 = []
    if month != 'all':
        for index, row in df.iterrows():
            if datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').month != MONTH_DATA[month]:
                list1.append(index)
        df.drop(list1, axis=0, inplace=True)  

    #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥--LOAD DAY--♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    list1 = []
    if day != 'all':
        for index, row in df.iterrows():
            if datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').weekday() != DAY_DATA[day]:
                list1.append(index)
        df.drop(list1, axis=0, inplace=True)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥--COMMON MONTH--♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    # display the most common month
    month = []
    for index, row in df.iterrows():
        month_in_time = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').month
        month.append(month_in_time)
    
    df['Month'] = month
    most_common_month_num = df['Month'].mode()[0]
    print('The most common month: ', get_key(MONTH_DATA, most_common_month_num))

    #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥--COMMON DAY--♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    # display the most common day of week
    day = []
    for index, row in df.iterrows():
        day_in_time = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').weekday()
        day.append(day_in_time)
    
    df['Days'] = day
    most_common_day_num = df['Days'].mode()[0]
    print('The most common day of week: ', get_key(DAY_DATA, most_common_day_num))

    #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥--COMMON HOUR--♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    # display the most common start hour
    hour = []
    for index, row in df.iterrows():
        hour_in_time = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').hour
        hour.append(hour_in_time)
    
    df['Hour'] = hour
    most_common_hour = df['Hour'].mode()[0]
    print('The most common start hour: ', str(most_common_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('♥'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥--COMMON START STATION--♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station: " + start_station)

    #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥--COMMON END STATION--♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("Most commonly used end station: " + end_station)

    #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥--COMBINATION--♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    # display most frequent combination of start station and end station trip
    combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("Most commonly used combination stations: " + str(combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('♥'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥--SUM--♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    #total trip duration
    total_sec = int(df['Trip Duration'].sum())
    total_time = str(timedelta(seconds=total_sec))
    print('Total trip duration: ', total_time)

    #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥--AVERAGE--♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    #average trip duration
    mean_sec = int(df['Trip Duration'].mean())
    mean_time = str(timedelta(seconds=mean_sec))
    print('Average trip duration: ', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('♥'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥--USER TYPE--♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    # Display counts of user types
    print('Counts of user types: ')
    print(df['User Type'].value_counts())
    print('\n')

    #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥--GENDER--♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    # Display counts of gender
    if 'Gender' in df.columns:
        print('Counts of gender: ')
        print(df['Gender'].value_counts())
        print('\n')

    #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥--YEARS--♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]

        print('Earliest: ' , int(earliest))
        print('Most recent: ' , int(most_recent))
        print('Most common year: ' , int(most_common_year))
        print('\n')

    #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥--THE END--♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('♥'*40)


def display_data(df):
    """ Display 5 lines of data upon request by the user """

    out = input('\nDo you want to see the first 5 rows of data? Enter yes or no.\n')
    start_index = 0
    end_index = 5
    while out.lower() == 'yes':
        print(df.iloc[start_index:end_index])
        start_index = end_index
        end_index += 5
        out = input('\nDo you want to see the next 5 rows of data? Enter yes or no.\n')

        if end_index > 300000:
            print('Sorry the chosen file has only 300000 lines..')
    print('♥'*40)
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

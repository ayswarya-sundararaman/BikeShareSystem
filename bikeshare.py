
# coding: utf-8

# In[ ]:

import time
import pandas as pd
import numpy as np

#Storing all the months,day,citynames and csv files in dictionaries
CITY_DATA = { '1': 'chicago.csv',
              '2': 'new_york_city.csv',
              '3': 'washington.csv' }
CITY_NAMES = {'1': 'Chicago',
              '2': 'New York City',
              '3': 'Washington'}
MONTHS={'1':'January','2':'February','3':'March',
        '4':'April','5':'May','6':'June',
        '7':'July','8':'August','9':'September',
        '10':'October','11':'November','12':'December'}
DAY={'1':'Monday','2':'Tuesday','3':'Wednesday','4':'Thursday','5':'Friday','6':'Saturday','7':'Sunday'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n\nHello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=get_city_input()
    
    #get user option to either filter by day,month or both and also handle invalid inputs" 
    explore_by=get_filterby()
    
    # get user input for month (all, january, february, ... , june) and also handle invalid inputs
    month=get_month(explore_by) 
    
    # get user input for month (all, sunday,monday....) and also handle invalid inputs
    day=get_day(explore_by)
    print('-'*100)
    return city,month,day


def get_city_input():
    # Get the city inputs from user and handle invalid inputs as well
    city=str(input("\nChoose the options given below to enter the City you wish to explore(eg: 1,2,3):\n                 '1' for Chicago \n                 '2' for New York City \n                 '3' for Washington\n"))
    
    while(int(city) not in range(1,4)):
        city=str(input("Oops your city input is wrong please give a valid input eg(1,2,3)\n"))
    
    return city
    
def get_filterby():
    # Get the filter inputs from user (filterby month,day or both) and handle invalid inputs as well
    explore_by=str(input("Do you want to filter by month, day or both?\n"))
    while(explore_by not in ("month","day","both")):
            print("Oops your input is wrong!Lets try again!!")
            explore_by=str(input("Do you want to filter by month, day or both?\n"))
    
    return explore_by
    
    
def get_month(explore_by):
    # Get the month inputs from user and handle invalid inputs as well
    month='0'
    if(explore_by == 'month' or explore_by=='both'):
        month=str(input("Choose the options given below to enter the month for which you wish to explore data (eg:1,2,3)\n                 '0' for all\n                  '1' for January\n                  '2' for February\n                   .........        \n                  '12' for December\n"))
        while(int(month) not in range(0,13)):
            print("Oops your month input is wrong!Lets try again!" )
            month=str(input("Try giving numbers from 0-12 with respect to the months\n"))
    
    return month
        
def get_day(explore_by):
    day='0'
    # get user input for day of week (all, monday, tuesday, ... sunday) and handle invaid inputs
    if(explore_by == 'day' or explore_by=='both'):
        day=str(input("Choose the options given below to enter the day for which you would like to explore the data(eg:1,2,3)\n                '0' for all \n                '1' for Monday \n                '2' for Tuesday\n                 .........  \n                 '7' for Sunday\n"))
        while(int(day) not in range(0,8)):
            print("Oops your day input is wrong!Lets try again!")
            day=str(input("Try giving numbers fro 0-7 with respect to the days\n"))
    return day
    

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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['hour']=df['Start Time'].dt.hour
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.weekday_name
    if month != '0' :
        df=df[df['month']==int(month)]
    if day != '0':
        df=df[df['day']==DAY[day]]
     
    return df


def time_stats(city,month='0',day='0'):
    """
    Displays statistics on the most frequent times of travel. for the entire city is:
    
    P.S -- We are loading the City Data once again because we would like to show the user 
    the popular month,day and hour for the entire city,otherwise if we use the the filtered 
    dataframe as the input for time_stats then most popularmonth/day returned  from  would 
    be the same as the month/day which they have entered as input for exploring datasets 
    
    """  
    city_df=pd.read_csv(CITY_DATA[city])
    city_df['Start Time']=pd.to_datetime(city_df['Start Time'])
    city_df['hour']=city_df['Start Time'].dt.hour
    city_df['month']=city_df['Start Time'].dt.month
    city_df['day']=city_df['Start Time'].dt.weekday_name
    
    print('\nCalculating The Most Frequent Times of Travel in {}...\n'.format(CITY_NAMES[city]))
    start_time = time.time()
    
    # display the most common month
    popular_month=city_df['month'].mode()[0]
    popular_month_name=MONTHS[str(popular_month)].title()
    print ("The most popular month in {} is ".format(CITY_NAMES[city]) +str(popular_month_name))
    
    # display the most common day of week
    popular_day=city_df['day'].mode()[0]
    print ("The most popular day in {} is: ".format(CITY_NAMES[city])+str(popular_day))
    
      # display the most common start hour
    popular_hour=city_df['hour'].mode()[0]
    print("The most popular hour in {} is: ".format(CITY_NAMES[city])+ str(popular_hour))
    
    # display common day for the user selected month
    if (month != '0'):
        selected_month=city_df[city_df['month'] == int(month)]
        popular_day_selected=selected_month['day'].mode()[0]
        print("The most popular day for the month of {} is ".format(MONTHS[month])+str(popular_day_selected))
        
    # display the most common hour for the selected day
    if ((day != '0') and (month != '0')):
        selected_day=city_df[city_df['day'] == DAY[day]]
        popular_hour_selected=selected_day['hour'].mode()[0]
        print("The most popular hour for the month of {} on {} is: ".format(MONTHS[month],DAY[day])+str(popular_hour_selected))
        
    if ((day != '0') and (month == '0')):
        selected_day=city_df[city_df['day'] == DAY[day]]
        popular_hour_selected=selected_day['hour'].mode()[0]
        print("The most popular hour on {} is: ".format(DAY[day])+str(popular_hour_selected))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print("Most commonly used start station is:    " + popular_start_station)

    # display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print("Most commonly used end station is:      " +popular_end_station)

    # display most frequent combination of start station and end station trip
    
    #Groups the start and end station and stores the size of each group
    comb_start_end_station=df.groupby(['Start Station','End Station']).size()
    
    #for storing the group with the max size(i.e the one which is most frequent)
    comb_station_max=comb_start_end_station.max()
    
    #Filters only those combinations which has the maximum size i.e the most used combination of start and end station
    print("\nMost most frequent combination of start station and end station trip ")
    frequent_combo=comb_start_end_station[comb_start_end_station==comb_station_max]
    print(frequent_combo)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("The total time to travel is : {}\n".format(total_travel_time))
    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print("The mean time to travel is : {}".format(mean_travel_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user=df['User Type'].value_counts()
    print("The counts of each user types is:\n {}".format(count_user))
    print("\n")
    
    #Display counts of gender and stats on year of birth only for new york and Chicago as gender and birth column are 
    #not present for Washington
    if(city == '1' or city=='2'):
        
        # Display counts of gender
        count_gender=df['Gender'].value_counts()
        print("The counts of the Males and the Females is:\n {}".format(count_gender))

        # Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        print("\nThe earliest Birth Year was on: {} \n".format(earliest_birth_year))
        recent_birth_year = df['Birth Year'].max()
        print("The recent Birth Year was on: {} \n".format(recent_birth_year))
        print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)
    
def restart():
    """function to restart and also  validate the input from the user"""
    restarts = input('\nWould you like to restart? Enter yes or no in lowercase\n')
    while(restarts != 'yes' and restarts !='no'):
            restarts=str(input("Oops your input is wrong!try again in lower case!!\n"))
    if (restarts=='yes'):
        pass
    elif (restarts=='no'):
        return 0
        
def individual_trips(df):
    """ using loops to get the right input from user for individual trips!!First show 5 raw data if they ask for more
    show 5 more and so on !"""
    i=0
    m=0
    n=5
    inp=str(input("Would you like to see few individual trips.Enter yes or no in lower case?\n"))
    while(True):
        while((inp.lower()!='yes' and inp.lower()!='no')):
            inp=str(input("Seems like you have not entered the input correctly!Please try again in lower case?\n"))
            if(inp=='yes'):
                i=n
                m=i
                n=i+5
            elif(inp=='no'):
                break
        while(i in range(m,n) and inp=='yes'):
            print("{\n")
            print(df.iloc[i])
            print("\n}\n")
            i+=1
        
        if(inp.lower()=='no'):
            break
        elif(inp.lower()=='yes'):
            inp=str(input("Would you like to see some more?\n"))  
            if(inp=='yes'):
                i=n
                m=i
                n=i+5
            elif(inp=='no'):
                break 
        
        
def main():
        while True:  
            try:
                city, month, day = get_filters()
                df = load_data(city, month, day)
                if(df.shape[0] == 0): #to check if the data frame df returned is not empty
                    print("Seems like there is no data available to explore for your input month/day")
                    if(restart()==0):
                        break
                    else:
                        continue
                time_stats(city,month,day) 
                station_stats(df)
                trip_duration_stats(df)
                user_stats(df,city)
                df.fillna(0,inplace=True) #to change all NAN values to 0
                individual_trips(df)
                if(restart() == 0):       
                        break
            except:
                print("\n\nSomething went wrong!!Check your inputs once again!!")
                if(restart() == 0):
                    break
            

if __name__ == "__main__":
	main()


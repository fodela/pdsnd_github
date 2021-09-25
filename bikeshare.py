import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


#some varialbes


possible_cities = {'c' : 'chicago',
                    'n': 'new york city',
                    'w': 'washington'}

filter_categories = ['m','d','b','n']
month_of_year = ['jan','feb','mar','apr','may','jun']
month_name = ['January','February','March','April','May','June']
dow = { 'mo' : 'Monday',
        'tu' : 'Tuesday',
        'we' : 'Wednesday',
        'th' : 'Thursday',
        'fr' : 'Friday',
        'sa' : 'Saturday',
        'su' : 'Sunday'}




def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by
        (str) day - name of the day of week to filter by
        (str) filter_by - name of the filtering category to filter by, or "none" to apply no filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    need_city = True
    need_cat = True
    need_month = True
    need_day = True
    
   
    

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while need_city:
        c = input('\nWhich city would you like to explore? \nPlease enter city name (Chicago, Washington, or New York City): ')
        if  c[:1].lower() in possible_cities:
            city = possible_cities[c[0].lower()]
            need_city = False
        else:
            print(f"\nsorry you can't explore {c} \nEnter Chicago ,new york city or washington")
            c = input('\nWhich city would you like to explore? \nPlease enter city name (Chicago, Washington, or New York City): ')
            if  c[:1].lower() in possible_cities:
                city = possible_cities[c[0].lower()]
                need_city = False

    # Explore by month , day or both or not at all
    while need_cat:
        category = input('\nWould you like to explore by month, day or both or not at all \nEnter m or d or b or n: ')
        if  category[:1].lower() in filter_categories:
            filter_by = category[0].lower()
            need_cat = False
            

        else:
            print(f"Sorry {category} is not a valid entry ")
            category = input('\nWould you like to explore by month, day or both or not atall \nEnter m or d or b or n: ')
            if  category[:1].lower() in filter_categories:
                filter_by = category[0].lower()
                need_cat = False
                
    if filter_by == 'm':
        day = ''
        need_day = False
    elif filter_by == 'd':
        month = ''
        need_month = False
    elif filter_by == 'n':
        month = ''
        day = ''
        need_month = False
        need_day = False

    
    # TO DO: get user input for month (all, january, february, ... , june)
    while need_month:
        m = input('\nWhich month? \nEnter month (eg.. jan, may - jun): ')
        if  m[:3].lower() in month_of_year:
            month = month_of_year.index(m[:3]) + 1
            need_month = False


        else:
            print(f"Sorry {m} is not a valid entry ")
            m = input('\nWhich month? \nEnter month (eg.. jan, may - jun): ')
            if  m[:3].lower() in month_of_year:
                month = month_of_year.index(m[:3]) + 1
                need_month = False

  

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while need_day:
        d = input('\nWhich day? \nEnter day (eg.. mon, tue - sun): ')
        print(need_day)
        if  d[:2].lower() in dow:
            day = dow[d[:2]]
            need_day = False

        else:
            print(f"Sorry {d} is not a valid entry ")
            d = input('\nWhich day? \nEnter day (eg.. mon, tue - sun): ')
            if  d[:2].lower() in dow:
                day = dow[d[:2]]
                need_day = False

    print('-'*40)
    return city, month, day, filter_by


def load_data(city, month, day,filter_by):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    
    most_common_month = month_name[df['month'].mode()[0] - 1]
    
    print(f"Most popular month: {most_common_month} ")

    # TO DO: display the most common day of week
    
    
    most_common_day = df['day_of_week'].mode()[0]
    print(f"Most popular day: {most_common_day} ")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print(f"The most common hour: {most_common_hour} ")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f"Most commonly used start station: \n{popular_start_station} ")


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f"Most commonly used end station: \n{popular_end_station} ")


    # TO DO: display most frequent combination of start station and end station trip
    df['Trip']= df['Start Station']+df['End Station']
    popular_trip = df['Trip'].mode()[0]
    print(f"Most commonly made trip from start to end: {popular_trip} ")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration =df['Trip Duration'].sum()
    print(f"\nWhat is the total trip duration? {total_trip_duration}")

    # TO DO: display mean travel time
    avg_trip_duration = df['Trip Duration'].mean()
    print(f"\nWhat is the total trip duration? {avg_trip_duration}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    # TO DO: Display counts of user types
    users = df['User Type'].value_counts()
    print(f"User breakdown: \n{users} ")

    #TO DO: Display counts of gender
    try:
        genders = df['Gender'].value_counts()
        print(f"\nGender distribution: {genders} ")
    except:
        print(f"\nGender distribution: None ")

    # TO DO: Display earliest, most recent, and most common year of birth
    
    try:
        youngest = pop_birth_year = df['Birth Year'].max()
        oldest = pop_birth_year = df['Birth Year'].min()
        pop_birth_year = df['Birth Year'].mode()[0]
        print(f"\nWhat is the oldest, youngest and most popular year of birth respectively? \n{youngest}, {oldest}, {pop_birth_year} ")
    except KeyError:
        print(f"\nWhat is the oldest, youngest and most popular year of birth respectively? \nNone, None,None ")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

        

def main():
    while True:
        
        city, month, day,filter_by = get_filters()
        df = load_data(city, month, day,filter_by)
        
        time_stats(df)
    # filter data
        if filter_by == 'd':
            print(f"\nFiltering data by {day}... Please wait...")
            df = df[df['day_of_week'] == day]
            
        elif filter_by == 'm':
            print(f"\nFiltering data by {month_name[month - 1]}... Please wait...")
            df = df[df['month'] == month]


        elif filter_by == 'b':
            print(f"\nFiltering data by {month_name[month - 1]} and {day}... Please wait...")
            df = df[(df['day_of_week'] == day) & (df['month'] == month)] 
        else:
            print('\nFetching unfiltered data Please wait...')


    # Display data
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        

        # Display individual data or not
        displaying = True
        index = 0
        while displaying and index <= df.shape[0]:

            ind_data_display = input('\nWould you like to view individual data? Enter yes or no: ')
            if ind_data_display.lower()[:1] == 'y':
                for i in range(5):
                    print('\n',df.iloc[index].to_frame())
                    index +=1
            else:
                displaying = False
        
        
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower()[:1] != 'y':
            break


if __name__ == "__main__":
	main()

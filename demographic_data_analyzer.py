import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load the dataset
    df = pd.read_csv('/workspace/boilerplate-demographic-data-analyzer/adult.data.csv')  # Ganti dengan jalur yang benar ke dataset Anda

    # 1. Count of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # 3. Percentage of people with a Bachelor's degree
    percentage_bachelors = (df['education'].value_counts(normalize=True)['Bachelors'] * 100).round(1)

    # 4. Percentage of people with higher education (Bachelors, Masters, Doctorate) earning >50K
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = (higher_education['salary'].value_counts(normalize=True)['>50K'] * 100).round(1)

    # 5. Percentage of people without higher education earning >50K
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = (lower_education['salary'].value_counts(normalize=True)['>50K'] * 100).round(1)

    # 6. Minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage of rich among those who work the minimum number of hours
    min_hours_people = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (min_hours_people['salary'].value_counts(normalize=True)['>50K'] * 100).round(1)

    # 8. Country with the highest percentage of people earning >50K
    country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack().fillna(0)
    country_salary['percentage_over_50k'] = country_salary['>50K'] * 100
    highest_earning_country = country_salary['percentage_over_50k'].idxmax()
    highest_earning_country_percentage = country_salary['percentage_over_50k'].max().round(1)

    # 9. Most popular occupation for those earning >50K in India
    india_high_salary = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_high_salary['occupation'].value_counts().idxmax()

    # Prepare the result as a dictionary
    result = {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

    # Print data if required
    if print_data:
        print(result)

    return result

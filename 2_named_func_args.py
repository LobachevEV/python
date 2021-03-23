def print_user_data(first_name, last_name, birth_year, birth_city, residence_city, email, phone):
    print(f'{first_name} {last_name} {birth_year} {birth_city} {residence_city} {email} {phone}')


if __name__ == '__main__':
    print_user_data(first_name=input('Enter a user first name: '), last_name=input('Enter a user last name: '),
                    birth_year=input('Enter a user birth year: '), birth_city=input('Enter a user birth city: '),
                    residence_city=input('Enter a user residence city: '), email=input('Enter a user email: '),
                    phone=input('Enter a user phone: '))

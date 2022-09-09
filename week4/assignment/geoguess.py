'''Country Cities Guessing Game Python Project
Create a program that will ask a user to guess
the capital of a country. The program should
have a list of at least 10 countries and their
capitals. The program should randomly choose a
country and ask the user to guess the capital.
The program should tell the user if they are
correct or not. The program should also keep
track of how many questions the user gets correct
and print that out at the end. Use this link to
programatically get the list of countries and their capitals:

https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-capital-city.json'''
import requests
import random
url_api='https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-capital-city.json'

response = requests.get(url_api).json()
i=random.randint(0,len(response))
print(f"What is capital city of {response[i]['country']}")
user_response=input()
if user_response==response[i]['city']:
    print("\nCorrect\n")
else:
    print(f"\nFalse The capity city is {response[i]['city']}\n")

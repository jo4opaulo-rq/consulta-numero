import phonenumbers
from phonenumbers import geocoder, PhoneNumberFormat

num = input("Digite o número no formato 00000000000: ").strip()

def Numero(num):
    numero = phonenumbers.parse('+'+num)

    print(f"O número {phonenumbers.format_number(numero, PhoneNumberFormat.INTERNATIONAL)} está localizado em ", end= "")
    
    print(geocoder.description_for_number(numero, 'pt'), end=', ')
    print(geocoder.country_name_for_number(numero, 'pt'))
    

Numero(num)
import phonenumbers
from phonenumbers import geocoder

phone = input('Digite telefone no formato + 551140028922: ')

ph_n = phonenumbers.parse(phone)

print(geocoder.description_for_number(ph_n, 'pt'))
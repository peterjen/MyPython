# https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=2

message = 'Hello World'

# SLICING
print(message[0:5]) #pass indexs
print(message[6]) 
print(message[6:])

print(message.lower())
print(message.find('Wor'))
print(message.count('l'))  # three l's count

message = message.replace('World','Universe') #REPLACE
print(message)

greet = 'Hello'
name = 'Peter'
message = greet + ', ' + name
print(message)

message = '{}, {}. Welcome'.format(greet,name)  # FORMAT, {} - place holder
print(message)

message1 = f'{greet}, {name.upper()}. Welcome' #F-STRING
print(message1)

#print(dir(name))
#print(help(str))
print(help(str.lower))


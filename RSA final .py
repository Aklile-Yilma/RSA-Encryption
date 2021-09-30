import math
import random

relative_primes=[]


def generate_Primeno():
    def is_prime(n):
        if n == 1:
            return False
        p = 2
        bound = math.floor(math.sqrt(n))
        while p<=bound:
            if n%p == 0:
                return False
            p+=1
        return True

    primes = []
    for i in range(1, 100):
        if is_prime(i):
            primes.append(i)
 
    return random.choice(primes)


def eculids_GCD(phi,e):
    if e==0:
        return phi

    else:
        return eculids_GCD(e,phi%e)



def multiplicative_inverse(e,phi):
    private_key=1
    for i in range(phi):
        if((e*i)%phi == 1):
            private_key=i
    return private_key

def encrypt(message,public_key):
    asci_message=[]
    for char in message:
            var=ord(char)
            value=(var**public_key[0])%public_key[1]
            asci_message.append(value)
    return asci_message


def decrypt(encrypted_message,private_key):
    #decrypt using the private key (SECRET KEY)
    #for i in encrypted_message:
     #   message=i
    message=(encrypted_message).split(',')
    decrypted_message=''
    for num in message:
         if (num=='32'):
             decrypted_message+=' '
         else:
             var=(int(num)**private_key[0])%private_key[1]
             char=chr(var)
             decrypted_message+=char

    return decrypted_message


#generate key 1 which is P       
prime_no=generate_Primeno()
print("prime_no 1(p) ", prime_no)
#generate key 2 which is Q
prime_no2=generate_Primeno()
print("Prime no 2 (q)",prime_no2)
# finding N the product of the primes
product=prime_no*prime_no2
print("The product of the two primes(N) ",product)

#finding the qootient phi(Ã˜)

phi=(prime_no-1)*(prime_no2-1)
print("Here is Phi(N)-quotient ",phi)

#find e or public key  such that it's relatively prime with Ã˜ or phi
for e in range(1,phi):
    if eculids_GCD(phi,e)==1:
        relative_primes.append(e)

public_key=(random.choice(relative_primes), product)
print("Here is the public key(e) ", public_key)
#find d(secret key) such that it's de = 1 (mod (p-1)(q-1))
private_key=(multiplicative_inverse(public_key[0],phi), product)
print("here is the private key(d)", private_key)


#interacting with the user
while  True:
	command=input("Do you want to decrypy or encrypt , enter E for encryption and enter D for decryption: ")
	if command.lower()=='e':
		message=input("enter message to encyrpt: ")
		print("Encypting your message...")
		encrypted_message=encrypt(message,public_key)
		print("here is your encrypted message: ", encrypted_message)
	else:
		
   		i=0
		while i<3 and command.lower()=='d':
			secret_key=eval(input("please enter secret key: "))
			if secret_key==private_key:
				to_decrypt=input("enter message separated by commas: ")
				print("Decrypting your message... ")
				decrypted_message=decrypt(to_decrypt,private_key)
				print("Decrypted message ", decrypted_message)
				break
			elif i==4:
				print("you have run out of tries...Good Bye")
			else:
				print("wrong secret key!!! Try again")



#PLEASE WORK!!!

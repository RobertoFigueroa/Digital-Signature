#Librerias utilizadas
from Crypto.PublicKey import RSA
from hashlib import sha512

message = b'ola k ase'
print("El mensaje es:", message)

aliceKey = RSA.generate(bits=1024)
publicKeyAlice = aliceKey.e
privateKeyAlice=aliceKey.d
nAlice=aliceKey.n

bobKey = RSA.generate(bits=1024)
publicKeyBob=bobKey.e
privateKeyBob=bobKey.d
nBob=bobKeys.n

hash = int.from_bytes(sha512(message).digest(), byteorder='big')
#luego se firman con la misma llave privada de alice
signature = pow(hash, privateKeyAlice,nAlice)
print("la firma del mensaje es:", hex(signature))

#Se encripta y luego se manda con bob usando su llave publica
intMessage = int.from_bytes(message, byteorder='big')
encryptedMessage = pow(intMessage, publicKeyBob,nBob)
print("El mensaje encriptado es:", hex(encryptedMessage))

#Luego del proceso anterior,se usa la lleve privada de bob
intDecryptedMessage = pow(encryptedMessage, privateKeyBob,nBob)
decryptedMessage = intDecryptedMessage.to_bytes((intDecryptedMessage.bit_length()+7)//8,byteorder="big")
print("El mensaje decriptado es: ",decryptedMessage)

#Ahora se verifica si el mensaje es valido 
hash = int.from_bytes(sha512(decryptedMessage).digest(), byteorder='big')
hashFromSignature = pow(signature, publicKeyAlice, nAlice)
print("Firma valida:", hash == hashFromSignature)

def encrypt_decrypt(string,password,mode='enc'):
    _hash = md5(password.encode()).hexdigest() #get hash of password
    cipher_key = urlsafe_b64encode(_hash.encode()) #use the hash as the key of encryption
    cipher = Fernet(cipher_key) #get the cipher based on the cipher key
    if mode == 'enc':
        return cipher.encrypt(string.encode()).decode() #encrypt the data
    else:
        return cipher.decrypt(string.encode()).decode() #decrypt the data
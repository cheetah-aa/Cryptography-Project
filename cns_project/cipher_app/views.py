from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
import json

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def caesar(request):

    # def encrypt(text, key):
    #     result = ""
    #     for char in text:
    #         # check if the character is only in alphabet A-Z, a-z
    #         if char.isalpha():
    #             # condition so if the character is in lowercase use a-z, and if character in uppercase use A-Z
    #             # ord(): return unicode code of the character in form of number
    #             if char.islower():
    #                 ascii_offset = ord('a')
    #             else:
    #                 ascii_offset = ord('A')
    #             shifted = (ord(char) - ascii_offset + key) % 26
    #             # turn the unicode code representation back to character
    #             result += chr(shifted + ascii_offset)
    #         else:
    #             result += char
    #     return result
    
    # # decryption is the same as encryption just the key in reverse so -key
    # def decrypt(text, key):
    #     return encrypt(text, -key)
    
    # context = {}

    # take input value from users
    # if request.method == 'POST':
    #     text = request.POST.get('text', '')
    #     key = int(request.POST.get('key', 0))
    #     action = request.POST.get('action')

    #     if action == 'encrypt':
    #         context['result'] = encrypt(text, key)
    #     else:
    #         context['result'] = decrypt(text, key)

    #     context['original'] = text
    #     context['key'] = key

# -----------------------------------------------

#     #creating the table for letter values
# p_dict = {}

# alphabet = "abcdefghijklmnopqrstuvwxyz"

# for i in range(len(alphabet)):
#     p_dict[alphabet[i]] = {'letter':alphabet[i],'value':i}

    
# key = 15
# cipher = ""

# word = "hello"

# def encrypt(p_value):
#     c_value = (p_value + key)%26
#     return c_value

# for letter in word:
#     if letter in p_dict:
#         print("Letter: ", letter)
#         print("Value of letter: ",p_dict[letter]['value'])

#         #assign variables, encrypt the plaintext
#         p = p_dict[letter]['value']
#         c_val = encrypt(p)

#         #get the cipher letter and add to cipher string
#         for char in p_dict:
#             if c_val == p_dict[char]['value']:
#                 cipher += p_dict[char]['letter']
#                 break
        
        
#     else:
#         print("nay")

# print("Ciphertext: ",cipher.upper())

# ------------------------------------------------

    # using js ajax to solve the reload page when click on encrypt decrypt
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('text', '')
        key = int(data.get('key', 0))
        action = data.get('action')

        def encrypt(text, key):
            text = text.lower()
            result = ""
            for char in text:
                # check if the character is only in alphabet, execute code block
                if char.isalpha():
                    p = ord(char) - ord('a') # example: char is b: ord('b') = 98, while ord('a') = 97 => p = 98 - 97 = 1, which is basically the position of b when a-z count from 0-25
                    
                    # nis formula
                    c = (p + key)%26 # cont. p = 1, say key = 3 => c = (1 + 3)%26 = 4

                    # convert back from unicode code (ascii value??) to character
                    result += chr(c + ord('a')) # why +ord('a') because we minus it before so just add it back... ex: c=4 and ord('a')=97 => 4+97 = 101, which is equivalent to 'e'
                else:
                    result += char
                    
            return result.upper()
    
        # decryption is the same as encryption just the key in reverse so -key
        def decrypt(text, key):
            return encrypt(text, -key)
        
        if action == 'encrypt':
            result = encrypt(text, key)
        else:
            result = decrypt(text, key)

        return JsonResponse({'result': result})
    
    return render(request, 'caesar.html')

def vigenere(request):

# #Vignere Cipher

# #creating the table for letter values
# p_dict = {}

# alphabet = "abcdefghijklmnopqrstuvwxyz"

# for i in range(len(alphabet)):
#     p_dict[alphabet[i]] = {'letter':alphabet[i],'value':i}


# key = "keyke"
# cipher = ""

# word = "hello"

# def encrypt(p_val,key_val):
#     c_val = (p_val+key_val)%26
#     return c_val

# if len(key) == len(word):
#     for i in range(len(word)):
#         if word[i] in p_dict:
#             #assign values
#             p = p_dict[word[i]]['value']
#             k = p_dict[key[i]]['value']
#             c = encrypt(p,k)

#             for char in p_dict:
#                 if c == p_dict[char]['value']:
#                     cipher += p_dict[char]['letter']
#                     break
#         else:
#             print("Chracter '",word[i], "' is not in the dictionary.")
# else:
#     print("The length of the key and the plaintext do not match.")

# print("Ciphertext: ",cipher.upper())
# -----------------------------------------------

    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('text', '')
        key = data.get('key', '')
        action = data.get('action')

        def encrypt(text, key):
            text = text.lower()
            key = key.lower()
            result = ""
            key_index = 0

            for char in text:
                # ber vea alphabet perform code ng tv ber ot nus else: nv krom oy tuk tdel
                if char.isalpha():
                    p = ord(char) - ord('a')
                    k = ord(key[key_index]) - ord('a')

                    c = (p + k) % 26

                    result += chr(c + ord('a'))

                    key_index += 1
                    if key_index == len(key):
                        key_index = 0
                else:
                    result += char
            return result.upper()
        
        def decrypt(text, key):
            text = text.lower()
            key = key.lower()
            result = ""
            key_index = 0

            for char in text:
                if char.isalpha():
                    c = ord(char) - ord('a')
                    k = ord(key[key_index]) - ord('a')

                    p = (c - k)%26

                    result += chr(p + ord('a'))

                    key_index += 1
                    if key_index == len(key):
                        key_index = 0
                else:
                    result += char
            return result.upper()
        
        if action == 'encrypt':
            result = encrypt(text, key)
        else:
            result = decrypt(text, key)

        return JsonResponse({'result': result})

    return render(request, 'vigenere.html')

# return back to homepage when click on home link
def home(request):
    return redirect("/")
import sys
import os
import re

#create first function that cut the key 
# if it's longer than the string
def cut_key(key, l):
    return(key[:l])

#create a function that repeat a key until the length of  
#our text 
def extend_key(key, l):
    return((key*l)[:l])

#the function that transfers the string to a list of ascci code
def return_ascii_word(word):
    return([ord(c) for c in word])

#the function that calculate the xor between two list 
def calculate_xor_product(plainText, secretKey ):
    encryptedText=""
    for i in range(len(plainText)):
        encryptedText+= chr (plainText[i] ^ ord(secretKey[i]))
        #print(plainText[i], secretKey[i], encryptedText[i], ord (plainText[i])^ ord (secretKey[i]) )
        #print (ord (plainText[i])^ ord (secretKey[i])%256)
    return encryptedText

#function to transfert the key 
def change_key ( key,plainText):
    if len(key)>len(plainText):
        return cut_key(key,len(plainText))
    elif len(key) < len(plainText):
        return extend_key(key, len(plainText))
    return key

#function to test if the source file or folder exist
def if_srcTarget_not_exist(srcTarget):
    if not os.path.exists(srcTarget):
        print("error, file doesn't exist")
        sys.exit()

#function to test if the source file or folder exist
def if_destTarget_exist(destTarget):
    if os.path.exists(destTarget):
        print("error, overwrite")
        sys.exit()

#function to encode a text file
def encrypt_file (srcFile,key,destFile):
    plainText = open(srcFile,'rb').read()
    #plain_text = ascii_Word(plain_text)
    key = change_key(key, plainText)
    #key = ascii_Word(key)
    #print(plain_text)
    encryptedText = calculate_xor_product(plainText,key)
    if destFile ==0:
        sys.stdout.write(encryptedText)
    else:
        f = open(destFile,'x')
        f.write(encryptedText)
        f.close()

#function to clone a directory
def encrypt_folder(srcTarget,destTarget):

    os.makedirs(os.path.join(os.getcwd(),destTarget))
    for root, dirs, files in os.walk(srcTarget, topdown= True):
        for name in dirs:
            actualPath = os.path.join(root, name)
            newPath = re.sub(srcTarget,destTarget,actualPath,1)
            os.makedirs(newPath)

        for name in files:
            actualPath = os.path.join(root, name)
            #print(actual_path)
            newPath = re.sub(srcTarget,destTarget,actualPath,1)
            #print(new_path)
            encrypt_file(actualPath, key, newPath)


    
if __name__ == '__main__':
    
    sys.argv
    
    if len(sys.argv) == 4:

        script, srcTarget, key , destTarget = sys.argv

        if_srcTarget_not_exist(srcTarget)
        if_destTarget_exist(destTarget)
        #when the input is a file  
        if os.path.isfile(srcTarget):
            encrypt_file(srcTarget,key,destTarget)
        #when the input is folder
        elif os.path.isdir(srcTarget):
            #print("this is directory")
            #os.makedirs(os.path.join(os.getcwd(),destTarget))
            encrypt_folder(srcTarget, destTarget)
           
    elif len(sys.argv)==3:

        script, srcTarget, key = sys.argv
        if_srcTarget_not_exist(srcTarget)
        
        if os.path.isfile(srcTarget):
            destTarget = 0
            encrypt_file(srcTarget,key, destTarget)
        
        elif os.path.isdir(srcTarget): 
            #output_file = 'destination'
            print("error, no destination folder")
            sys.exit()
            #os.makedirs(os.path.join(os.getcwd(),output_file))
            #encode_folder(target)
    else:
        print("help, not enough argument")
        sys.exit()

    
 
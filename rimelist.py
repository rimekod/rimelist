class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(bcolors.OKBLUE + """
 ______     __     __    __     ______     __         __     ______     ______  
/\  == \   /\ \   /\ "-./  \   /\  ___\   /\ \       /\ \   /\  ___\   /\__  _\ 
\ \  __<   \ \ \  \ \ \-./\ \  \ \  __\   \ \ \____  \ \ \  \ \___  \  \/_/\ \/ 
 \ \_\ \_\  \ \_\  \ \_\ \ \_\  \ \_____\  \ \_____\  \ \_\  \/\_____\    \ \_\ 
  \/_/ /_/   \/_/   \/_/  \/_/   \/_____/   \/_____/   \/_/   \/_____/     \/_/
  """ + "\n" + "by rimekod\n\n")


inp = str(input(bcolors.BOLD + "Enter the string keywords (Separate with space) -> "))
inp2 = str(input(bcolors.BOLD + "Enter the numeric keywords (Separate with space) -> "))
file_content = str(input(bcolors.HEADER + "Delete content and add new passwords to file? (w), Add passwords to current file content? (a) [w/a] "))

rimelist = ["123456","1234567","12345678","123456789","1234567890","mypassword","password"]
appends = ["#","!","?","00","01","02","03","04","05","06","07","08","09","09","10","11","123","1234","12345","321","4321"]

for string in inp.split(" "):
    if string.isalpha() == False:
        print(bcolors.FAIL + 'Please enter only alpha chars!')
        exit()
for num in inp2.split(" "):
    if num.isnumeric() == False:
        print(bcolors.FAIL + 'Please enter only numeric chars!')
        exit()
if(file_content == 'w' or file_content == 'a'):
    pass
else:
    print(bcolors.FAIL + 'Please enter valid file content type [w/a]')
    exit()
words = inp2.split(" ") + inp.split(" ")

WL_alpha = []
WL_num = []
wordlist = []
WL_append = []
combines = []
combine_words = []
numbers_with_letter = []

for pureword in words:
    word = pureword.lower()
    if word.isalpha():
        WL_alpha.append(word)
        WL_alpha.append(word[::-1])
        # upper all letters
        split_word = list(word)
        x = 0
        while x <= len(split_word) - 1:
            if str(split_word[x]).islower():
                split_word[x] = split_word[x].upper()
                if x > 0:
                    split_word[x-1] = split_word[x-1].lower()
                if x == len(split_word) - 1:
                    split_word[x] = split_word[x].upper()
                WL_alpha.append("".join(split_word))
                x+=1
    elif word.isnumeric():
        WL_num.append(word)
        

# combine words from same array
for wrd in words:
    y = 0
    while y < len(words):
        combines.append(words[y] + wrd)
        y+=1

# Append chars to words
for alphaword in WL_alpha:
    for append in appends:
        WL_append.append(alphaword + append)

# combine words with char
for wrd in words:
    z = 0
    while z < len(words):
        combine_words.append(words[z] + "_" + wrd)
        combine_words.append(words[z] + "-" + wrd)
        combine_words.append(words[z] + "." + wrd)
        combine_words.append(words[z] + "+" + wrd)
        combine_words.append(words[z] + "*" + wrd)
        combine_words.append(words[z] + "0" + wrd)
        combine_words.append(words[z] + "1" + wrd)
        z+=1

# append first letter of word to end of numbers
for wrd in words:
    if wrd.isalpha():
        t = 0
        while t < len(WL_num):
            numbers_with_letter.append(WL_num[t] + WL_num[t] + list(wrd)[0])
            t+=1

#combine
wordlist = WL_alpha + WL_num + combines + rimelist + WL_append + combine_words + numbers_with_letter

str_list = "\n".join(wordlist)
file = open('passwords.txt', file_content)
file.write(str_list)
file.close()

print(bcolors.OKBLUE + '{0:,}'.format(len(wordlist)) + " password created and written to the passwords.txt file.")
print("")
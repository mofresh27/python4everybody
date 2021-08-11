

#play.clear()


FileName = input ('Enter file name here:\n')
# f = open(FileName,'r')
fhand = open(FileName) #conditional code may not need 
play =list()

for word in fhand:
    #conditional code may not need 
    word = (word.strip()) #conditional code may not need
    if word in play: continue
    play.append(word)
    play = word.split()
    print(play)

    
    #print(play[6])
    

#print(f.read())


# this is a four loop to count lines in a docurment

# FileName = input ('Enter file name here:\n')
# try:
#     f = open(FileName,'r')
# except:
#     print('File cannot be open:', FileName)
#     quit()

# count = 0 
# for line in f:
#     count = count + 1

# print('There were',count, 'lines in this documnet')



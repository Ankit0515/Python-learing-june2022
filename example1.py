# %%
my_string=" Ankit Srivastava"
print(my_string)

# %%
Str="Lucknow"
print(len(Str))

# %%
name= "python is great"
c=name[10:16]
print(c)

# %%
str2="Python is everywhere"
for x in str2.split():
    print (x)



# %%
str3 = "Hello World!"[::-1]
print(str3)

# %%
str4="How are you?"
x=str4.upper()
print(x)

# %%
str1=input("enter a string: ")
print(len(str1))

# %%
str5="How Is It Going?"
x=str5.lower()
print(x)

# %%
str5="How Is It Going?"
print(str5.lower())

# %%
words = ['Python', 'is', 'easy', 'to', 'learn']
strlist= " ".join(words)
print(strlist)

# %%
print("This is a example of \n""wrinting code in python\n""and printing multiline string on \n" "new lines")

# %%
new_string= r"to move to newline \n. "
print(new_string)

# %%
print("the variable is 15")

# %%
a= "the variable is 15"
print(a)

# %% [markdown]
# 12. concatenate the following strings and print the result
# s1 = 'python '
# s2 = 'is '
# s3 = 'great.'
# 

# %%
s1="python"
s2="is"
s3="great"
print(s1+" "+s2+" "+s3)

# %% [markdown]
# 13. Print # 20 times without using a loop

# %%
print("#"*20)

# %% [markdown]
# 14. Print numbers from 1 to 9, each on a seperate line, followed by a dot, output should look like the following-
# 1.
# 2.
# 3.
# 

# %%

for i in range(1,10):
    print(f"{i}.")

# %% [markdown]
# 15. Ask user to input a sentence and print each word on a different line.

# %%
new_sen=input("kindly enter sentence")
for c in new_sen.split():
    print(c)

# %% [markdown]
# #Ask user to input a string and check if the string ends with '?'
# 

# %%
txt = input("please enter a text")
x = txt.endswith("?")
print(x)

# %%
story = input("enter a sentence")

q ="e"
start = 0
while True:
    idx = story.find(q,start)
    if idx == -1:
        break
    print(f'{q} found at position {idx}')
    start = idx + 1

# %% [markdown]
# #Check if the user input is a number.

# %%
number1 = int(input("Enter number and hit enter "))
print("Printing type of input value")
print("type of number ", type(number1))

# %% [markdown]
# # ask user to enter a string and check if the string contains fyi

# %%
story = input("enter a sentence")

q ="fyi"
start = 0
while True:
    idx = story.find(q,start)
    if idx == -1:
        break
    print(f'{q} found at position {idx}')
    start = idx + 1

# %%




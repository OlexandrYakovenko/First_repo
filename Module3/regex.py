import re
import random
# https://www.w3schools.com/python/python_regex.asp
# https://regex101.com/

# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string

#p=r"[^\.\w\d\s]{1,}"

s=r"Python is the most popular language now. Чарівно ж!"
p=r"[a-zA-Z]{4,}"
p2=r"([а-яА-ЯіІїЇєЄa-zA-Z\.]+)(\s+)"
pfull=r".*"
pao=r"(?:a|o)"
p_comp=r""

a=re.search(p,s)#Search anywhere
print(a.span())
print(a.group())
print(a.groups())

print()

b=re.match(p2,s) #Search only from the beginning of the string
print(b.span())
print(b.group())
print(b.groups())

print()
print(re.fullmatch(p, s))
print(re.fullmatch(pfull, s))
print()

print(re.findall(p2,s))
print(re.split(r" ",s))
print(re.sub(p,"nyan",s))

print()

iter=re.finditer(p, s)
print(iter)
for e in iter:
    print(e.group())



print(re.findall(pao,s))

print(re.split(p2,s))

text = "We arrive on 03/25/2018. So you are welcome after 04/01/2018." 
print(re.sub(r'(\d\d)/(\d\d)/(\d{4})', r'\2.\1.\3', text)) 

def long(w):
    return str(len(w.group()))
print(re.sub(p2,long,s,re.ASCII))
print(re.sub(p2,lambda x: str(len(x.group())),s))
print(re.sub(r"\d+",lambda x: str(int(x[0])**2) ,"1 2 3 4 5 6 7 8 9 10"))

# positive lookahead assertion
print(re.findall(r"[a-zA-Z]+(?=\s)",s))
# negative lookahead assertion,
print(re.findall(r"[a-zA-Z]+(?!\s)",s))
# positive lookbehind assertion
print(re.findall(r"(?<=\s)[a-zA-Z]+",s))
# negative lookbehind assertion
print(re.findall(r"(?<!\s)[a-zA-Z]+",s))
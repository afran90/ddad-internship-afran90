def evncheckpal(o,f,l):
    if f==l:
        return True
    #print('1',o[f], o[l])
    if o[f]!=o[l]:
        return False
    #print('2',o[f],o[l])
    if f<l+1:
        return evncheckpal(o,f+2,l-2)
    return True
def oddcheckpal(o,f,l):
    if f==l:
        return True
    if o[f]!=o[l]:
        return False
    if f<l+1:
        return oddcheckpal(o,f+2,l-2)
    return True

s=input()
if oddcheckpal(s,1,len(s)-2):
    print("Odd palindrome")
elif evncheckpal(s,0,len(s)-1):
    print("Even palindrome")
else:
    print("Not a palindrome")
s=str(input())
string =''
def reversed(s,string):
    list=s.split(' ')
    list.reverse()
    for x in list:
        string+=x
        string+=' '
    print (string)

reversed(s, string)
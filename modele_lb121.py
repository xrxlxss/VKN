def func(file):
    file=open("D:\\fileslab\\not4.txt",'r')
    res=file.read()
    print(res)
    file.close()


def func1(files):
    files=open("D:\\fileslab\\not4.txt",'a')
    n=str(input("Введіть що бажаєте додати?"))
    files.write(n)
    files.close()

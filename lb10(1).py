fin = open("D:\\fileslab\\out.txt.txt", "rt")
fout = open("D:\\fileslab\\fragment.txt.txt", "wt")
for line in fin:
	fout.write(' '.join(line.split()))
fin.close()
fout.close()
sec=open("D:\\fileslab\\fragment.txt.txt")
files=0
for line in sec:
    files += 1
print(files)

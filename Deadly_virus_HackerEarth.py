A new deadly virus has infected large population of a planet. A brilliant scientist has discovered a new strain of virus which can cure this disease. Vaccine produced from this virus has various strength depending on midichlorians count. A person is cured only if midichlorians count in vaccine batch is more than midichlorians count of person. A doctor receives a new set of report which contains midichlorians count of each infected patient, Practo stores all vaccine doctor has and their midichlorians count. You need to determine if doctor can save all patients with the vaccines he has. The number of vaccines and patients are equal.

n=int(input())
vaccine=list(map(int,input().split()))
patient=list(map(int,input().split()))
vaccine.sort()
patient.sort()
cured=False
for i in range(n):
    if vaccine[i]>patient[i]:
        cure=True
    else:
        cure=False
        break
if cure:
    print("Yes")
else:
    print("No")
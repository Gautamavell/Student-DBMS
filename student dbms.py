#students database management system in csv file

import csv

#creating file

def create(a):
    f=open(a,'w+',newline='')
    print('FILE HAS BEEN CREATED IN NAME OF ',a,"\n")
    f_writer=csv.writer(f,delimiter=',')
    f_writer.writerow(['ADM.NO','NAME','GRADE','ADDRESS','CONTACT NUMBER'])
    rec=[]
    n=int(input('Please enter the no.of entries:'))
    print('Please enter the values:-')
    for i in range(0,n):
        print('\nEntry ',i+1)
        ad=int(input('Admission number:'))
        na=input('Name of the student:')
        g=int(input('Grade:'))
        add=input('Address:')
        ph=int(input('Contact number:'))
        l=[ad,na,g,add,ph]
        rec.append(l)
    for i in rec:
        f_writer.writerow(i)
    f.close()
    print('\^o^ #DATA ENTERED SUCCESSFULLY!# ^o^/')
    input('\nEnter any key to continue...')

#appending value
def append(a):
    print('\nExisting values:-')
    f=open(a,'r',newline="\r\n")
    f_reader=csv.reader(f)
    for i in f_reader:
        print(i)
    f.close()
    f=open(a,'a',newline='')
    f_writer=csv.writer(f,delimiter=',')
    rec=[]
    n=int(input('\nPlease enter the no.of entries:'))
    print('Please enter the values:-')
    for i in range(0,n):
        print('\nEntry ',i+1)
        ad=int(input('Admission number:'))
        na=input('Name of the student:')
        g=int(input('Grade:'))
        add=input('Address:')
        ph=int(input('Contact number:'))
        l=[ad,na,g,add,ph]
        rec.append(l)
    for i in rec:
        f_writer.writerow(i)
    print('DATA HAVE BEEN ADDED TO THE FILE  ',a)
    f.close()
    input('\nEnter any key to continue...')

#read file
def read(a):
    print('\nINFO AVAILABLE IN FILE ',a)
    f=open(a,'r',newline="\r\n")
    f_reader=csv.reader(f)
    for i in f_reader:
        print('\n')
        for j in range(0,5):
            print(i[j],end='  ')
    f.close()
    print('\n\n<<<<End of file>>>>')
    input('\nClick Enter key to continue...')
    
#modifying the file
def modify(a):
    print('Modify a record in file ',a)
    f=open(a,'r',newline='\r\n')
    f1=open('temp.csv','w',newline='\r\n')
    r=input('Enter the ADM.no of record to modify:')
    s=csv.reader(f)
    s1=csv.writer(f1)
    for i in s:
        if i[0]==r:
                print('Adm.no     :',i[0])
                print('Name       :',i[1])
                print('Grade      :',i[2])
                print('Address    :',i[3])
                print('Contact.no :',i[4])
                c=input('Is this  the  record you want to modify? [y/n]:')
                if c=='y' or c=='Y':
                   print('Please enter the new value')
                   i[0]=int(input('Admission number:'))
                   i[1]=input('Name of the student:')
                   i[2]=int(input('Grade:'))
                   i[3]=input('Address:')
                   i[4]=int(input('Contact number:'))
                   s1.writerow(i)
                   print('RECORD MODIFIED!')
                else:
                   s1.writerow(i)
        else:
            s1.writerow(i)
    f.close()
    f1.close()
    k=open('temp.csv','r',newline='\r\n')
    k1=open(a,'w',newline='\n')
    l=csv.reader(k)
    l2=csv.writer(k1)
    for i in l:
        l2.writerow(i)
    k.close()
    k1.close()
    print('SUCCESSFULLY!!!   (*v*)/')
    input('\nEnter any key to continue...')
        
    
#search
def search(a):
    s=input('Please enter the ad.no :')
    f=open(a,'r',newline="\r\n")
    f_reader=csv.reader(f)
    j=0
    for i in f_reader:
            if i[0]==s:
                print('Adm.no     :',i[0])
                print('Name       :',i[1])
                print('Grade      :',i[2])
                print('Address    :',i[3])
                print('Contact.no :',i[4])
                j=1
            else:
                continue
    if j==0:
        print('NO ENTRY FOUND!')
    f.close()
    input('\nEnter any key to continue...')

def delete(a):
    print('Delete a record in file ',a)
    f=open(a,'r',newline='\r\n')
    f1=open('temp.csv','w',newline='\r\n')
    r=input('Enter the ADM.no of record to delete:')
    s=csv.reader(f)
    s1=csv.writer(f1)
    for i in s:
        if i[0]==r:
                print('Adm.no     :',i[0])
                print('Name       :',i[1])
                print('Grade      :',i[2])
                print('Address    :',i[3])
                print('Contact.no :',i[4])
                c=input('Is this  the  record you want to delete? [y/n]:')
                if c=='y' or c=='Y':
                   pass
                else:
                   s1.writerow(i)
        else:
            s1.writerow(i)
    f.close()
    f1.close()
    k=open('temp.csv','r',newline='\r\n')
    k1=open(a,'w',newline='\n')
    l=csv.reader(k)
    l2=csv.writer(k1)
    for i in l:
        l2.writerow(i)
    k.close()
    k1.close()
    print('SUCCESSFULLY DELETED!!!   (*v*)/')
    input('\nEnter any key to continue...')

 #--------------------------------------------------   
print('STUDENT DATABASE MANAGEMENT SYSTEM IN CSV FILE')
print('----------------------------------------------')
print('\n\(^o^) HI (^o^)/')
p=1
a=input('\nPLEASE ENTER THE NAME OF FILE :')
while p!=0:
  o=int(input('''
Which of the following operation you want to perform?
1-->Create
2-->Append
3-->Read
4-->Modify
5-->Search
6-->Delete
0-->Close
Your choice:'''))
  if  o==1:
      create(a)
  elif o==2:
      append(a)
  elif o==3:
      read(a)
  elif o==4:
      modify(a)
  elif o==5:
      search(a)
  elif o==6:
      delete(a)
  elif o==0:
      print('\n\(^o^) BYEBYE (^o^)/')
      p=0

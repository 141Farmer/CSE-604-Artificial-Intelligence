from  math  import  sqrt

def printBoard(arr):
    length=len(arr)
    matrix=sqrt(length)

    for i in range(length):
        if (i+1)%matrix==1:
            print(f'|{arr[i]}',end='')
        elif  (i+1)%matrix==0:
            print(f'{arr[i]}|')
        else:
            print(f'|{arr[i]}|',end='')



def move(arr,index):
    if index>9 or index<0:
        print('False move')
        return
    if arr[index-2]!='*' and arr[index+2]!='*' and arr[index+3]!='*' and arr[index-3]!='*':
        print('False move')
        return
    currentIndex=arr.index('*')
    arr[currentIndex],arr[index-1]=arr[index-1],'*'
    printBoard(arr)

def main():
    arr=[1,2,3,4,5,6,7,8,'*']
    printBoard(arr)
    move(arr,8)

if __name__=='__main__':
    main()
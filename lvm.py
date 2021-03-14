import os

print('\t\t\ LVM AUTOMATION ')
print('\t\t------------------')

def LVM():
    fdisk = os.system('sudo fdisk -l')
    print(fdisk)
    hdname = input('Enter the hardisk name: ')
    pv = os.system('sudo pvcreate {}'.format(hdname))
    print(pv)
    vgname = input('Enter Vgname: ')
    vg = os.system('sudo vgcreate {}  {}'.format(vgname,hdname)) 
    lvname = input('Enter Lvname: ')
    lvsize = input('Enter the size of Lv in G/M: ')
    os.system('sudo lvcreate --size {} --name {} {}'.format(lvsize,lvname,vgname))
    os.system('sudo mkfs.ext4 /dev/{}/{}'.format(vgname,lvname))
    os.system('sudo mount /dev/{}/{}  /datanode'.format(vgname,lvname))
    df = os.system('df -hT')
    print(df)

def LVMONFLY():
    size = input('Enter the size to increase(+) with G/M: ')
    lvdisplay =  os.system('lvdisplay')
    print(lvdisplay)
    lvm = input('Enter the lv name: ')
    os.system('lvextend --size {} /dev/{}'.format(size,lvm))
    os.system('sudo resize2fs /dev/{}'.format(lvm))
    dfht = os.system('df -hT')
    print(dfht)
while True:
    print('press 1 to create a lvm \n press 2 to increase the lvm onfly ')
    cmd=input()
    if '1' in cmd:
        LVM()
    elif '2' in cmd:
        LVMONFLY()
    else:
        break


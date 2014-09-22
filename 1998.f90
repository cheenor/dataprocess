implicit none
! read Q1 and Q2 of a given year for a given period 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
integer,parameter :: nrec=1460
integer,parameter :: nvr=19
character levname(6)*20,area(6)*4
integer i,j,k,m,n,p
character dirEC*100,dirTP*100,path*100,name*200
character cel(nrec)*10, hour(nrec)*5
real taget(nvr,6,nrec,6),raw(17,nvr,1464,6)
real temp(nvr)
integer pd_sr(2),pd_ed(2),ids,ide
integer dys(12)

pd_sr(1)=6     ;pd_sr(2)=1
pd_ed(1)=8     ;pd_ed(2)=31

dirEC='Z:\DATA\LargeScale\NcepR2_Pre\980101-981231\'
dirTP='Z:\DATA\LargeScale\TP\NcepR2_Pre\980101-981231\'
levname(1)='_lowlevel.txt'
levname(2)='_Middlelevel.txt'
levname(3)='_Hightlevel.txt'
levname(4)='_Abovelevel.txt'
levname(5)='_Tropsphere.txt'
levname(6)='_AllLevels.txt'
area(1)='PRD'  ;    area(2)='MLYR'
area(3)='NPC'  ;    area(4)='NEC'
area(5)='WTP'  ;    area(6)='ETP'
do i=1,12
dys(i)=31
enddo

dys(2)=28
dys(6)=30
dys(4)=30
dys(9)=30
dys(11)=30
do i=1,6
   if(i<5)then
      path=trim(dirEC)//'1998'//trim(area(i))//'_raw.txt'
      open(10,file=trim(path))
      read(10,*)
      do j=1,nrec
        do k=1,17
         read(10,99) cel(j), hour(j),(raw(k,n,j,i),n=1,nvr)
        enddo
      enddo
      close(10)
      do m=1,6
      path=trim(dirEC)//'1998'//trim(area(i))//trim(levname(m))
      open(10,file=trim(path))
      read(10,*)
      do j=1,nrec
         read(10,99)cel(j), hour(j),(taget(n,m,j,i),n=1,nvr)
      enddo
      close(10)
      enddo
   else     
     path=trim(dirTP)//'1998'//trim(area(i))//'_raw.txt'
     open(10,file=trim(path))
     read(10,*)name
     do j=1,nrec
       do k=1,17
         read(10,99)cel(j), hour(j),(raw(k,n,j,i),n=1,nvr)
       enddo
     enddo
     close(10)
     do m=1,6
      path=trim(dirTP)//'1998'//trim(area(i))//trim(levname(m))
      open(10,file=trim(path))
      read(10,*)
      do j=1,nrec
         read(10,99)cel(j), hour(j),(taget(n,m,j,i),n=1,nvr)
      enddo
      close(10)
     enddo
   endif
enddo
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
ids=0
ide=0
do i=1,pd_sr(1)-1
  ids=ids+dys(i)*4
enddo
ids=ids+(pd_sr(2)-1)*4+1
do i=1,pd_ed(1)-1
  ide=ide+dys(i)*4
enddo
ide=ide+pd_ed(2)*4
path='D:\MyPaper\Phd01\data\1998\'//'date_and_name.txt'
open(20,file=trim(path))
write(20,908)'DATE','HOUR','T_ls(k/day)','Q_ls(k/day)','U(m/s)', &
     'V(m/s)','moisture(kg/kg)','HGT(m)','AIR(K)','Adj_omega(pa/s)',&
     'RH(%)','Theta(K)','Q1(k/day)','Q2(k/day)','HADQ(K/day)',&
     'VADQ(K/day)','TCHQ(K/day)','HADT(K/day)','HADT(K/day)',&
     'TCHT(K/day)','Ori_omega(pa/s)'
908   format(1X,A10,1X,A5,19(1X,A15))
do i=ids,ide
  write(20,98)cel(i),hour(i)
enddo
close(20)
do m=1,6
  do i=1,6
  path='D:\MyPaper\Phd01\data\1998\'//trim(area(m))//trim(levname(i))//'_ori.txt'
  open(20,file=trim(path))
  path='D:\MyPaper\Phd01\data\1998\'//trim(area(m))//trim(levname(i))//'_fn4days.txt'
  open(30,file=trim(path))
    do j=ids,ide
      write(20,97) (taget(n,m,j,i),n=1,nvr)
      temp=0
      do n=1,nvr
        do p=j,j+16
         temp(n)=temp(n)+taget(n,m,p,i)
        enddo
        temp(n)=temp(n)/16.0
      enddo
      write(30,97) (temp(n),n=1,nvr)
    enddo
  close(20)
  close(30)
  enddo 
  path='D:\MyPaper\Phd01\data\1998\'//trim(area(m))//'raw_ori.txt'  
  open(20,file=trim(path))
  path='D:\MyPaper\Phd01\data\1998\'//trim(area(m))//'raw_fn4days.txt'  
  open(30,file=trim(path))
   do j=ids,ide
    	do k=1,17
          write(20,97) (raw(k,n,j,m),n=1,nvr)
          temp=0
          do n=1,nvr
            do p=j,j+16
              temp(n)=temp(n)+raw(k,n,p,m)
            enddo
            temp(n)=temp(n)/16.0
           enddo
         write(30,97) (temp(n),n=1,nvr)
        enddo
    enddo
   close(20)
   close(30) 
enddo 



97 format(1X,19(E12.4,1X))
98 format(1X,A10,1X,A5)
99 format(1X,A10,1X,A5,1X,19(1X,E12.4))
end

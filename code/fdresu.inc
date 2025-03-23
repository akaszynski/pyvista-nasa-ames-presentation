c   ---      i       1     numdof   Degrees of freedom per node
c                                   DOF reference numbers are:
c         UX  = 1, UY  = 2, UZ  = 3, ROTX= 4, ROTY= 5, ROTZ= 6, AX  = 7, AY  = 8
c         AZ  = 9, VX  =10, VY  =11, VZ  =12, GFV1=13, GFV2=14, GFV3=15, WARP=16
c         CONC=17, HDSP=18, PRES=19, TEMP=20, VOLT=21, MAG =22, ENKE=23, ENDS=24
c         EMF =25, CURR=26, SP01=27, SP02=28, SP03=29, SP04=30, SP05=31, SP06=32
c         TBOT=33, TE2 =34, TE3 =35, TE4 =36, TE5 =37, TE6 =38, TE7 =39, TE8 =40
c         TE9 =41, TE10=42, TE11=43, TE12=44, TE13=45, TE14=46, TE15=47, TE16=48
c         TE17=49, TE18=50, TE19=51, TE20=52, TE21=53, TE22=54, TE23=55, TE24=56
c         TE25=57, TE26=58, TE27=59, TE28=60, TE29=61, TE30=62, TE31=63, TTOP=64
c                                    (curdof(i),i=1,numdof)

c   NOD      i       1     nnod     Nodal equivalence table. This table equates
c                                   the number used for storage to the actual
c                                   node number

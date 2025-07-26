# https://rosalind.info/problems/iprb/
AApop = 29
Aapop = 17
aapop = 22

totalpop = AApop + Aapop + aapop

#                             aA                                          AA                                                 aa                                                   Aa
aaoutcome = ((aapop/totalpop) * ((Aapop)/(totalpop-1))*0.5) + ((Aapop/totalpop) * ((Aapop-1)/(totalpop-1))*0.25) + ((aapop/totalpop) * ((aapop-1)/(totalpop-1))) + ((Aapop/totalpop) * ((aapop)/(totalpop-1))*0.5)




Aoutcome = (1 - aaoutcome) * 100

print(Aoutcome)

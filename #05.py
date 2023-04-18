#1
kocha="bog'bon"
mahalla="    sog'bon"
tuman="bodomzor"
viloyat="samarqand       "
result=f"{kocha.capitalize()} ko'chasi\n {(mahalla.title()).lstrip()} mahallasi \n{tuman.upper()} tumani \n{(viloyat.lower()).rstrip()} viloyati"
print(result)

#2
kocha=input("kucha nomi:")
mahalla=input("mahalla nomi:")
tuman=input('tuman nomi:')
viloyat=input("viloyat nomi:")

print(kocha+' kuchasi\n '+mahalla+' mahallasi \n'+tuman+" tumani \n"+viloyat+' viloyati')
manzil=f"{kocha} kuchasi\n {mahalla} mahallasi\n {tuman} tumani\n{viloyat} viloyati "
print(manzil.title())

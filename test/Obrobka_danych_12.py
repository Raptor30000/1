import pandas as pd #import pandas libarty to analise dataframe
numer_pomiaru=5 #imput number of processing file

try:
    plik=open("pomiar%d.txt" % numer_pomiaru,"r") #check that file existing

except:
    print("Plik pomiar%d.txt nie istnieje" % numer_pomiaru) #if not show information and stop
    raise
zapis= open("pomiar%dzimny.txt" % numer_pomiaru,"a+") #Create file with processed data
zapis.close()   #close file to avoid errors

filename = './pomiar%d.txt' %numer_pomiaru #prepare file with date and precessed date to make code easier to read
filename2 = './pomiar%dzimny.txt' %numer_pomiaru
data = pd.read_csv(filename) #read by pandas file with data
data.head() #show information about data
data.info()
data['roznica_napiec'] = data['Voltage[V]'] - data['Voltage[V]'].shift(-1) #preapare column with difference between voltage in current and past row
dane= data.index[data['roznica_napiec'] <= -5].tolist() #find row with grow voltage  between curren row and past more than 5V and indeks of this row as a list
lista = list(map(lambda x: x - 3, dane))    #change each found index about -3 to get values just before power supply start changing voltage
do_zapisu= data.iloc[lista] #make dataframe with row with index before difference
zapis= open("pomiar%dzimny.txt" % numer_pomiaru,"w") #open file to save proceesed data
do_zapisu.to_csv(filename2) #save preocessed data
zapis.close() #close file to avoid errors
print("zakonczono")
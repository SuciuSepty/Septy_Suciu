opera= """Guvernul a aprobat, miercuri, suplimentarea bugetului Ministerului Justiţiei cu peste 2,8 milioane lei pentru continuarea proiectelor în curs. Printre ele se numără și suma necesară acoperirii serviciilor de consultanță pentru modernizarea Palatului de Justiție din Cluj-Napoca.

„Toate investiţiile aflate în desfăşurare sunt pentru ca cetăţenii plătitori de impozite şi taxe să beneficieze de un serviciu public de calitate, de sedii de instanţe spaţioase, moderne. În plus, este vorba despre asigurarea unor condiţii de lucru corespunzătoare pentru magistraţi şi pentru personalul auxiliar. Suplimentarea bugetului Ministerului Justiţiei era mai mult decât necesară pentru că avem multe proiecte în desfăşurare, inclusiv dintre cele care vizează asigurarea încălzirii corespunzătoare în perioada de iarnă. Îi mulţumesc ministrului Boloş pentru înţelegere şi suport”, a declarat Gorghiu, citată de Agerpres.

Palatul de Justiție Cluj-Napoca va fi reabilitat
Asocierea Bog’Art (lider) – Athenaeum Construct – Popp & Asociatii, ACI Cluj – UTI Construction and Facility Management – Electroproiect, alaturi de Schindler Romania, ca subcontractant, a castigat contractul de modernizare a clădirii Palatului de Justitie Cluj-Napoca, în urma licitației organizate de Curtea de Apel Cluj.""" # Un sir de caractere
splitting= len(opera) // 2 # len = cate caractere are
first_half= opera[:splitting] # for-u cela cu inceput:final:pas (default e 0 , last, +1)
first_half=first_half.strip() # pentru a filtra
first_half= first_half.upper() # pt caps
second_half= opera[splitting:] # Second half
second_half_inv=second_half[::-1] # pentru a atribui NOUL SIR PENTRU CA NU POTI SA LE MODIFIC IN PYTHON
second_half_3=second_half_inv.capitalize() # PENTRU A ATRIBUI IAR UN NOU SIR # ADORAM PYTHON
second_half_4=second_half_3.replace('.','').replace('!','').replace(',','').replace('?','') # Replace-ul
print(first_half + second_half_4)


# Scrie un program în Python care declara un sir cu continutul copiat de pe internet, dintr-un articol de stiri in limba romana și efectuează pe acel articol(care este stocat ca un sir de caractere) următoarele operații:
#
# Împarte șirul în două părți egale. Dacă numărul de caractere este impar, prima parte va avea un caracter în plus.
# Pe prima parte:
# Transformă toate literele în majuscule.
# Elimină toate spațiile goale de la începutul și finalul șirului.
# Pe a doua parte:
# Inversează ordinea caracterelor.
# Transformă prima literă în majusculă.
# Elimină toate caracterele de punctuație (., ,, !, ?) din această parte.
# Combină cele două părți și afișează rezultatul.
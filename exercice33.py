import random
def simulation_lancer_de(n):
   nombre_de_lancers = 0
   nombre_de_6 = 0
   freq_de_6 = 0
   for i in range(1, n+1):
            random.randint(1, 6)
            nombre_de_lancers += 1 
            
   if (random.randint(1, 6) == 6):
         nombre_de_6 += 1
         freq_de_6 = nombre_de_6 / nombre_de_lancers
         print('nombre de fois 6 :',nombre_de_6)
         print('frequence de 6 :',freq_de_6)
         return freq_de_6
   
   
   print('nombre de lancer:', nombre_de_lancers)
print(simulation_lancer_de(10))
import sys
input = sys.stdin.readline

def correspond(s, motif, liste):
   _len = len(motif)
   s = str(s)
   gauche, droite = motif.split('?')
   cond1 = gauche == '' and droite == ''
   cond2 = not cond1 and gauche == '' and s.endswith(droite)
   cond3 = not cond1 and droite == '' and s.startswith(gauche)
   cond4 = gauche != '' and droite != '' and s.endswith(droite) and s.startswith(gauche)
   if (s != '0' and len(s) >= _len) and (cond1 or cond2 or cond3 or cond4):
       liste.append(s)

def parcoursLargeur(graphe, s, motif):
   liste = []
   visiter = set([])
   Avisiter = [s]
   while Avisiter:
      noeud = Avisiter.pop(0)
      correspond(noeud, motif, liste)
      visiter.add(noeud)
      for n in graphe[noeud]:
         if n not in visiter: Avisiter.append(n)
   return liste

def main():
   graphe = [[] for _ in range(int(input())+1)]
   data = list(map(int, input().split()))
   for v,n in enumerate(data, start=1):
      graphe[n].append(v)
      
   motif = input()
   
   #print(' '.join(parcoursLargeur(graphe, 0, motif)))
   ch = ' '.join(parcoursLargeur(graphe, 0, motif))
   #print('7 8 3 6 1 2 4 5')
   print("type(ch):{} type 7 8 3 6 1 2 4 5: {}".format(type(ch), type('7 8 3 6 1 2 4 5')))
   

main()
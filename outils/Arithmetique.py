# -*- coding: utf-8 -*-

import math, random

def pgcd(a, b):
    """Calcule le pgcd entre a et b."""
    while b:
        a, b = b, a%b
    return a

def ppcm(a, b):
    """Calcule le ppcm entre a et b."""
    return a*b/pgcd(a, b)

def premier(n):
    """Teste si un nombre est premier."""
    return not [x for x in xrange(2,int(math.sqrt(n)) + 1)
                if n%x == 0]

def eratosthene(n):
    """Etablit la liste des nombres premiers inferieurs a n."""
    return [x for x in xrange(2, n) if premier(x)]


def factor(n):
    """Retourne la liste des facteurs premiers du nombre n."""
    premiers = []
    candidats = xrange(2,n+1)
    candidat = 2
    while not premiers and candidat in candidats:
        if n%candidat == 0 and premier(candidat):
            premiers.append(candidat)
            premiers = premiers + factor(n/candidat)
        candidat += 1
    return premiers

def factorise(n):
    """Retourne la liste des facteurs premiers du nombre n, ainsi que le détail de la factorisation pour LateX. PAS FINI."""
    global corrige

    primes = []
    candidates = xrange(2,n+1)
    candidate = 2

    espace = len(str(n))
    corrige = '$$'
    text = ' = '

    while n > 1:
        if n%candidate == 0 and premier(candidate):
            primes.append(candidate)
            for nb in primes:
                text += str(nb) + ' \\times '
            if n / candidate <> 1:
                corrige += text + str(n/candidate) + '\n'
            n = n / candidate

        if n % candidate <> 0:
            candidate += 1
        text = ' ' * espace + ' = '
    corrige += "$$"
    return (primes, corrige)

def carrerise(n):
    """Trouve le plus petit facteur par lequel multiplier pour obtenir un carré."""
    if round(sqrt(n), 0)==sqrt(n):
        return n
    primes = factorise(n)[0]
    for element in primes:
        if (primes.count(element) % 2 == 1):
            primes.append(element)
    q = 1
    for element in primes:
        q *= element

    return int(float(q) / float(n))

def signe(a):
    """renvoie 1 si a est>0, -1 si a<0"""
    if a < 0:
        return -1
    else:
        return 1
def valeur_alea(a, b):
    """choisit une valeur comprise entre a et b non nulle"""
    while True:
        alea = random.randrange(a, b + 1)
        if alea != 0:
            return alea

#---------------------------------------------------------------------
# A supprimer dès que troisiemes aura été converti au nouveau format
#---------------------------------------------------------------------

def ecrit_tex(file, formule, cadre=None, thenocalcul='\\thenocalcul = ',
              tabs=1):
    """Écrit la ligne dans le fichier"""
    if formule != '':
        if cadre == None or not cadre:
            file.write((u'  \\[ %s%s \\] \n') % (thenocalcul, formule))
        else:
            file.write((u'  \\[ \\boxed{%s%s} \\] \n') % (thenocalcul, formule))

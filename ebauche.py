
#!##############################################################################
#! Implémentation IMMUABLE d'un arbre binaire.
#! Les arbres binaires ne seront JAMAIS modifiées.
#!##############################################################################

type vide = tuple[()]
type arbre_bin = vide | tuple[ int, arbre_bin, arbre_bin]

ARBRE_VIDE = ()

#?#####################################
#! LES FONCTIONS D'ACCES ET DE CREATION
#*#####################################

def cle(a: arbre_bin) -> int:
    """
    Renvoie la clé de la racine de l'arbre binaire.

    Précondition :
    - L'arbre ne doit pas être vide.

    >>> cle((5, ARBRE_VIDE, ARBRE_VIDE))
    5
    >>> cle(ARBRE_VIDE)
    Traceback (most recent call last):
    AssertionError: L'arbre binaire est vide
    """
    assert not a == ARBRE_VIDE, "L'arbre binaire est vide"
    return a[0]


def sag(a: arbre_bin) -> arbre_bin:
    """
    Renvoie le sous-arbre gauche de l'arbre binaire.

    Précondition :
    - L'arbre ne doit pas être vide.

    >>> sag((5, (3, ARBRE_VIDE, ARBRE_VIDE), ARBRE_VIDE))
    (3, (), ())
    >>> sag(ARBRE_VIDE)
    Traceback (most recent call last):
    AssertionError: L'arbre binaire est vide
    """
    assert not a == ARBRE_VIDE, "L'arbre binaire est vide"
    return a[1]


def sad(a: arbre_bin) -> arbre_bin:
    """
    Renvoie le sous-arbre droit de l'arbre binaire.

    Précondition :
    - L'arbre ne doit pas être vide.

    >>> sad((5, ARBRE_VIDE, (7, ARBRE_VIDE, ARBRE_VIDE)))
    (7, (), ())
    >>> sad(ARBRE_VIDE)
    Traceback (most recent call last):
    AssertionError: L'arbre binaire est vide
    """
    assert not a == ARBRE_VIDE, "L'arbre binaire est vide"
    return a[2]


def est_vide(a: arbre_bin) -> bool:
    """
    Vérifie si l'arbre est vide.

    >>> est_vide(ARBRE_VIDE)
    True
    >>> est_vide((5, ARBRE_VIDE, ARBRE_VIDE))
    False
    """
    return len(a) == 0


def est_feuille(a: arbre_bin) -> bool:
    """
    Vérifie si l'arbre est une feuille (sans sous-arbres).

    >>> est_feuille((5, ARBRE_VIDE, ARBRE_VIDE))
    True
    >>> est_feuille((5, (3, ARBRE_VIDE, ARBRE_VIDE), ARBRE_VIDE))
    False
    """
    return est_vide(sad(a)) and est_vide(sag(a))


def exemple() -> arbre_bin:
    """
    Crée et renvoie un exemple d'arbre binaire.

    >>> exemple()
    (2, (4, (), ()), (7, (9, (), ()), (4, (), ())))
    """
    return (2, (4, ARBRE_VIDE, ARBRE_VIDE), (7, (9, ARBRE_VIDE, ARBRE_VIDE), (4, ARBRE_VIDE, ARBRE_VIDE)))


#?#########################
#! LES FONCTIONS EN LECTURE
#*#########################

def hauteur(a: arbre_bin)-> int:
    """
    Renvoie la hauteur de l'arbre binaire.

    >>> hauteur(ARBRE_VIDE)
    0
    >>> hauteur(exemple())
    3
    """
    if est_vide(a):
        return 0
    else:
        h_gauche = 1 + hauteur(sag(a))
        h_droite = 1 + hauteur(sad(a))
        return max(h_gauche, h_droite) 
    
def taille(a: arbre_bin)-> int:
    """
    Calcule le nombre de nœuds dans l'arbre binaire.

    >>> taille(ARBRE_VIDE)
    0
    >>> taille(exemple())
    5
    """
    if est_vide(a):
        return 0
    else:
        taille_gauche = taille(sag(a))
        taille_droite = taille(sad(a))
        return  1 + taille_gauche + taille_droite
    
def somme(a: arbre_bin)-> int:
    """
    Calcule la somme des clés de l'arbre binaire.

    >>> somme(ARBRE_VIDE)
    0
    >>> somme(exemple())
    26
    """
    if est_vide(a):
        return 0
    if est_feuille(a):
        return cle(a)
    else:
        somme_gauche = somme(sag(a))
        somme_droite = somme(sad(a))
        return cle(a) + somme_gauche + somme_droite
    
def to_str(a: arbre_bin)-> str:
    """
    Génère une str à partir d'un arbre binaire avec toutes ses clés

    >>> to_str(exemple())
    '2 <-> 4 <-> 7 <-> 9 <-> 4'
    >>> to_str(ARBRE_VIDE)
    '*'
    """
    if est_vide(a):
        return "*"
    if est_feuille(a):
        return cle(a)
    else:
        str_gauche = to_str(sag(a))
        str_droite = to_str(sad(a))
        return f"{cle(a)} <-> {str_gauche} <-> {str_droite}"
    
def minimum(a: arbre_bin)-> int:
    """
    Renvoie la valeur minimale contenue dans l'arbre.

    Précondition :
    - L'arbre ne doit pas être vide.

    >>> minimum(exemple())
    2
    >>> minimum(ARBRE_VIDE)
    Traceback (most recent call last):
    AssertionError: L'arbre binaire est vide
    """
    assert not est_vide(a), "L'arbre binaire est vide"
    if est_feuille(a):
        return cle(a)
    else:
        minimum_gauche = minimum(sag(a))
        minimum_droite = minimum(sad(a))
        return min(cle(a), minimum_gauche, minimum_droite)
    
def maximum(a: arbre_bin)-> int:
    """
    Renvoie la valeur maximale contenue dans l'arbre.

    Précondition :
    - L'arbre ne doit pas être vide.

    >>> maximum(exemple())
    9
    >>> maximum(ARBRE_VIDE)
    Traceback (most recent call last):
    AssertionError: L'arbre binaire est vide
    """
    assert not est_vide(a), "L'arbre binaire est vide"
    if est_feuille(a):
        return cle(a)
    else:
        maximum_gauche = maximum(sag(a))
        maximum_droite = maximum(sad(a))
        return max(cle(a), maximum_gauche, maximum_droite)
    
def sont_egaux(a: arbre_bin, b: arbre_bin)-> int:
    """
    Renvoie si oui ou non un arbre est égal à un autre arbre
    
    >>> a = exemple()
    >>> b = exemple()
    >>> sont_egaux(a, b)
    True
    >>> c = (2,(4 , ARBRE_VIDE, ARBRE_VIDE), ARBRE_VIDE)
    >>> sont_egaux(a, c)
    False
    """
    return to_str(a) == to_str(b)

if __name__ == "__main__":
    import doctest
    print("#############################################################################")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("||                           NOUVEAU CODE                                  ||")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("#############################################################################")
    doctest.testmod()
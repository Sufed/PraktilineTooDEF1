#Harjutus 6.
def is_prime(число)->bool:
    """
    Määrme is_prime...
    :parem int arv: Järjend is_prime numbridest
    :rtype: str
    """
    flag=True
    for i in range(2, число):
        if число%i==0:
            flag=False
            break
    return flag

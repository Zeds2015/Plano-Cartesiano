class PontosEm2D:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @x.setter
    def mover_horizontal(self, valor):
        self._x = valor
    
    @y.setter
    def mover_vertical(self, valor):
        self._y = valor
        
    def __add__(self, outro_ponto):
        if type(outro_ponto) == type(self):
            return PontosEm2D(self._x + outro_ponto._x, self._y + outro_ponto._y)
        elif type(outro_ponto) == tuple and len(outro_ponto) == 2:
            return (self._x + outro_ponto[0], self._y + outro_ponto[1])
    
    def __sub__(self, outro_ponto):
        if type(self) == type(outro_ponto):
            return PontosEm2D(self._x - outro_ponto._x, self._y - outro_ponto._y)
        elif type(outro_ponto) == tuple and len(outro_ponto) == 2:
            return (self._x - outro_ponto[0], self._y - outro_ponto[1])
    
    def __mul__(self, outro_ponto):
        if type(self) == type(outro_ponto):
            return PontosEm2D(self._x * outro_ponto._x, self._y * outro_ponto._y)
        elif type(outro_ponto) == tuple and len(outro_ponto) == 2:
            return (self._x * outro_ponto[0],self._y * outro_ponto[1])
    
    def __truediv__(self, outro_ponto):
        try:
            if type(self) == type(outro_ponto):
                return PontosEm2D(self._x / outro_ponto._x, self._y / outro_ponto._y)
            elif type(outro_ponto) == tuple and len(outro_ponto) == 2:
                return (self._x / outro_ponto[0],self._y / outro_ponto[1])
        except ZeroDivisionError:
            print('Impossivel dividir por zero')
    
    def __floordiv__(self, outro_ponto):
        try:
            if type(self) == type(outro_ponto):
                return PontosEm2D(self._x // outro_ponto._x, self._y // outro_ponto._y)
            elif type(outro_ponto) == tuple and len(outro_ponto) == 2:
                return (self._x // outro_ponto[0],self._y // outro_ponto[1])
        except ZeroDivisionError:
            print('Impossivel dividir por zero')
    
    def __repr__(self):
        return str((self._x, self._y))
    
    def __eq__(self,outro_ponto):
        if type(self) == type(outro_ponto):
            return self._x == outro_ponto._x and self._y == outro_ponto._y
        elif type(outro_ponto) == tuple and len(outro_ponto) == 2:
            return self._x == outro_ponto[0] and self._y == outro_ponto[1]
    
    
if __name__ == '__main__':
    from math import sqrt
    
    def retorna_primos(num):
        eh_primo = True
        for i in range(2, int(sqrt(num) + 1)):
            if num % i == 0:
                #eh_primo = not eh_primo
                break
                
        return num if eh_primo else None
    
    def primos_gerador(fib, i=0):
        for i in fib:
            yield retorna_primos(i)
    
    #soma n numeros da sequencia de fibonacci
    fib = [0, 1]
    [fib.append(fib[-1] + fib[-2]) for i in range(int(input('Digite um numero: ')))]
    print(sum(fib))
    
    #captura todos os elementos pares da sequencia de fibonacci com n numeros
    pares = list(filter(lambda x: x % 2 == 0, fib))
    print(pares)
    
    #captura todos os elementos impares da sequencia de fibonacci
    impares = list(filter(lambda x: x not in pares, fib))
    print(impares)
    
    #captura todos os numeros primos em fibonacci
    primos = list(primos_gerador(fib))
    primos = list(filter(lambda x: x != None and x > 1, primos))
    print(primos)

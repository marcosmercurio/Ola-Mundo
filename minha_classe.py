class pessoa (object):
    def __init__(self,n,i,a,p):
            
            self.nome = n
            self.idade = i
            self.altura = a
            self.peso = p
  
    def __repr__(self):
            return f'Nome: {self.nome}, Idade: {self.idade} anos, Altura: {self.altura} metros, Peso: {self.peso} kilos,'    
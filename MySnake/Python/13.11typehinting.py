class Banknote:
    pass
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return f'Banknote({self.value})'
    
    def __str__(self):
        return f'Banknote {self.value}'

if __name__=='__main__':
    banknote = Banknote(10)
    print(f'{banknote!r}')
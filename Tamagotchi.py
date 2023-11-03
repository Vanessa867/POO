class Pessoa:
    def __init__(self):
        self.andando = False
        self.dormindo = False
        self.comendo = False

    def andar(self):
        if not self.dormindo and not self.comendo:
            self.andando = True
            print("A pessoa está andando.")
        else:
            print("A pessoa não pode andar enquanto está dormindo ou comendo.")

    def dormir(self):
        if not self.andando and not self.comendo:
            self.dormindo = True
            print("A pessoa está dormindo.")
        else:
            print("A pessoa não pode dormir enquanto está andando ou comendo.")

    def comer(self):
        if not self.andando and not self.dormindo:
            self.comendo = True
            print("A pessoa está comendo.")
        else:
            print("A pessoa não pode comer enquanto está andando ou dormindo.")

    def parar_atividades(self):
        self.andando = False
        self.dormindo = False
        self.comendo = False

pessoa = Pessoa()
pessoa.andar()
pessoa.comer()
pessoa.dormir()
pessoa.parar_atividades()
pessoa.dormir()
pessoa.andar()

class ContaBancaria:
    def __init__(self, numero_conta, saldo, status, nome_cliente, tipo_conta):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.status = status
        self.nome_cliente = nome_cliente
        self.tipo_conta = tipo_conta

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor} realizado com sucesso. Novo saldo: R${self.saldo}')
        else:
            print('Valor inválido para depósito.')

    def sacar(self, valor):
        if self.status == 'Ativa':
            if valor > 0 and valor <= self.saldo:
                self.saldo -= valor
                print(f'Saque de R${valor} realizado com sucesso. Novo saldo: R${self.saldo}')
            else:
                print('Valor inválido para saque.')
        else:
            print('A conta está inativa. Não é possível realizar saques.')

    def verificar_saldo(self):
        print(f'Saldo da conta: R${self.saldo}')

    def ativar_conta(self):
        if self.saldo == 0:
            self.status = 'Ativa'
            print('A conta foi ativada com sucesso.')
        else:
            print('Não é possível ativar a conta com saldo não zerado.')

    def desativar_conta(self):
        if self.saldo == 0:
            self.status = 'Inativa'
            print('A conta foi desativada com sucesso.')
        else:
            print('Não é possível desativar a conta com saldo diferente de zero.')

minha_conta = ContaBancaria(12345, 1000, 'Ativa', 'João', 'Poupança')
minha_conta.depositar(500)
minha_conta.sacar(300)
minha_conta.verificar_saldo()
minha_conta.ativar_conta()
minha_conta.desativar_conta()

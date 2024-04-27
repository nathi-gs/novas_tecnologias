import cliente.cliente
import conta1.conta1

cliente1 = cliente("João", "Silva", "11111-1")
conta2 = conta1("123-4", cliente1, 1000.00, 4000.00)

print(conta1.extrato())
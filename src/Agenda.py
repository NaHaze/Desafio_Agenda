def add_contact(contacts, name_contact, phone_contact, email_contact):
    contact = {"contact": name_contact, "phone": phone_contact,"email": email_contact, "favorite": False}
    contacts.append(contact)
    print(f"Contato {name_contact} foi adicionado com sucesso!")
    return

def view_contact(contacts):
    print("\n Lista de contatos: ")
    for index, contact in enumerate(contacts, start=1):
        name_contact = contact["contact"]


contacts=[]
while True:

    print("\n (__Menu da sua Agenda de Contatos__) ")
    print("1. Adicione um novo contato")
    print("2. Lista de Contatos")
    print("3. Edite um contato existente")
    print("4. Veja sua lista de Favoritos")
    print("5. Deletar um contato")
    print("6. Sair da Agenda")

    choice = input("Digite a opção desejada: ")

    if choice == "1":
        name_contact = input("Digite o nome do contato: ")
        phone_contact = input("Digite o número de telefone: ")
        email_contact = input("Digite o e-mail deste novo contato: ")
        add_contact(contacts, name_contact, phone_contact, email_contact)
    elif choice == "6":
        break


print("Agenda finalizada")



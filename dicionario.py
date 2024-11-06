agentes = {
    "Jett": ["smoke","dash","pulo","ultimate"],
    "Gekko": ["bang","rastreador","molotov","ultimate"],
    "Omen": ["teleporte","smoke","bang","ultimate"]
}
print("CONHECENDO AS HABILIDADES")
person = input("Digite o nome de um personagem para saber suas habilidades: ")
if person in agentes:
    print (f"habilidades de {person}:{', '.join(agentes[person])}")

#adicionar habilidade
print("ADICIONANDO HABILIDADES")
person = input("Digite o nome de um personagem: ")
new_habilidade = input("Digite uma nova habilidades: ")
if person in agentes:
    agentes[person].append(new_habilidade)
    print(f"habilidade {new_habilidade} adicionada ao personagem {person}")

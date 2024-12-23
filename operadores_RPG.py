# Status de um personagem em um RPG
vida = True  # O personagem está vivo
mana = False  # O personagem tem mana suficiente para magia
buff = True  # O personagem tem algum buff ativo

# 1. O personagem pode atacar (vida e mana precisam estar ativos)
print("O personagem pode atacar:", vida and mana)

# 2. O personagem pode usar habilidades (vida ou mana são suficientes)
print("O personagem pode usar habilidades:", vida or mana)

# 3. O personagem não está morto (não está sem vida)
print("O personagem não está morto:", not vida)

# 4. Pode lutar (vida e tem buff ativo, mas sem mana)
print("Pode lutar (vida e buff, sem mana):", vida and buff and not mana)

# 5. Está em modo crítico (não tem vida ou mana, mas tem buff)
print("Modo crítico:", not vida or not mana and buff)

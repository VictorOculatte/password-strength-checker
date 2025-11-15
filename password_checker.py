import re

def check_password_strength(password):
    score = 0
    reasons = []

    # Comprimento
    if len(password) >= 12:
        score += 1
    else:
        reasons.append("A senha possui menos de 12 caracteres.")

    # Maiúsculas
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        reasons.append("A senha não possui letras maiúsculas.")

    # Minúsculas
    if re.search(r"[a-z]", password):
        score += 1
    else:
        reasons.append("A senha não possui letras minúsculas.")

    # Números
    if re.search(r"[0-9]", password):
        score += 1
    else:
        reasons.append("A senha não possui números.")

    # Caracteres especiais (comum)
    if re.search(r"[@$!%*?&#^()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
        score += 1
    else:
        reasons.append("A senha não possui caracteres especiais.")

    # Classificação simples
    if score <= 2:
        strength = "Fraca"
    elif score == 3 or score == 4:
        strength = "Média"
    else:
        strength = "Forte"

    return strength, reasons

def main():
    pw = input("Digite a senha para analisar: ")
    strength, reasons = check_password_strength(pw)
    print(f"\nForça: {strength}\n")
    if reasons:
        print("Motivos:")
        for r in reasons:
            print(f"- {r}")
    else:
        print("Boa senha! Pontos positivos atendidos.")

    input("\nPressione ENTER para sair...")

if __name__ == "__main__":
    main()
    
input("\nPressione ENTER para sair...")

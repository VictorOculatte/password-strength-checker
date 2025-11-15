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

    # Caracteres especiais
    if re.search(r"[@$!%*?&#^()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
        score += 1
    else:
        reasons.append("A senha não possui caracteres especiais.")

    # Classificação final
    if score <= 2:
        strength = "Fraca"
    elif score in [3, 4]:
        strength = "Média"
    else:
        strength = "Forte"

    return strength, reasons


def main():
    print("=== Password Strength Checker ===\n")

    while True:  # LOOP até ficar forte
        password = input("Digite uma senha para analisar: ")
        strength, reasons = check_password_strength(password)

        print(f"\nForça da senha: {strength}")

        # Se não for forte, mostrar motivos e repetir
        if strength != "Forte":
            print("\nMotivos para não ser forte:")
            for r in reasons:
                print(f"- {r}")

            print("\n⚠ Tente novamente! A senha precisa ser forte para continuar.\n")
        
        else:
            print("\n✔ Senha forte! Boa escolha.")
            break  # Sai do loop

    input("\nPressione ENTER para sair...")


if __name__ == "__main__":
    main()

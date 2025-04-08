import random
import time

caras = {
    1: "[     ]\n[  *  ]\n[     ]",
    2: "[*    ]\n[     ]\n[    *]",
    3: "[*    ]\n[  *  ]\n[    *]",
    4: "[*   *]\n[     ]\n[*   *]",
    5: "[*   *]\n[  *  ]\n[*   *]",
    6: "[* * *]\n[     ]\n[* * *]"
}

def tirar_dado():
    for _ in range(10):
        num = random.randint(1, 6)
        print(f"\nTirando...\n{caras[num]}")
        time.sleep(0.1)
        print("\033c", end="")  # Limpia pantalla
    print(f"Resultado final:\n{caras[num]}")

tirar_dado()
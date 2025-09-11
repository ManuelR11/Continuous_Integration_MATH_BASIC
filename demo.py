
from math_basic import square, factorial, is_prime, gcd, lcm


def run_quick_demo() -> None:
    print("== Quick demo ==")
    print(f"square(3)      -> {square(3)}")
    print(f"factorial(5)   -> {factorial(5)}")
    print(f"is_prime(17)   -> {is_prime(17)}")
    print(f"gcd(54, 24)    -> {gcd(54, 24)}")
    print(f"lcm(4, 6)      -> {lcm(4, 6)}")
    print("-" * 40)


def _input_float(msg: str) -> float:
    while True:
        raw = input(msg).strip()
        try:
            if raw.lower() in ("true", "false"):
                raise ValueError("No se permite bool.")
            return float(raw)
        except ValueError:
            print("⚠️  Ingresa un número válido (int o float, no bool).")


def _input_int(msg: str, *, non_negative: bool | None = None) -> int:
    while True:
        raw = input(msg).strip()
        try:
            if raw.lower() in ("true", "false"):
                raise ValueError("No se permite bool.")
            n = int(raw)
            if non_negative and n < 0:
                print("⚠️  Debe ser un entero ≥ 0.")
                continue
            return n
        except ValueError:
            print("⚠️  Ingresa un entero válido (no bool).")


def menu():
    print("Menú — Matemática básica")
    print("1) square (n^2)")
    print("2) factorial (n!)")
    print("3) is_prime (¿n es primo?)")
    print("4) gcd (máximo común divisor)")
    print("5) lcm (mínimo común múltiplo)")
    print("6) salir")
    print("-" * 40)


def main() -> int:
    run_quick_demo()

    while True:
        menu()
        op = input("Elige una opción [1-6]: ").strip()
        try:
            if op == "1":
                n = _input_float("n = ")
                print(f"Resultado: {square(n)}\n")
            elif op == "2":
                n = _input_int("n (entero ≥ 0) = ", non_negative=True)
                print(f"Resultado: {factorial(n)}\n")
            elif op == "3":
                n = _input_int("n (entero) = ")
                print(f"Resultado: {is_prime(n)}\n")
            elif op == "4":
                a = _input_int("a (entero) = ")
                b = _input_int("b (entero) = ")
                print(f"Resultado: {gcd(a, b)}\n")
            elif op == "5":
                a = _input_int("a (entero) = ")
                b = _input_int("b (entero) = ")
                print(f"Resultado: {lcm(a, b)}\n")
            elif op == "6":
                print("¡Hasta luego!")
                return 0
            else:
                print("Opción inválida. Elige un número del 1 al 6.\n")
        except Exception as e:
            print(f"Error: {e}\n")



if __name__ == "__main__":
    raise SystemExit(main())

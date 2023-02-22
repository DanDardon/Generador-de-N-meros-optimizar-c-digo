import random

def generate_random_numbers(num_values):
    min_value = -10000000
    max_value = 10000000
    values = {}
    for i in range(num_values):
        values[i] = random.randint(min_value, max_value)
    with open("numbers.txt", "w") as file:
        for key, value in values.items():
            file.write(f"{key}\t{value}\n")

def sort_numbers():
    with open("numbers.txt", "r") as file:
        values = {}
        keys = []
        for line in file:
            key, value = line.strip().split("\t")
            values[int(key)] = int(value)
            keys.append(int(key))
        size = len(keys)
        gap = size // 2
        while gap > 0:
            for i in range(gap, size):
                temp = values[keys[i]]
                j = i
                while j >= gap and values[keys[j - gap]] > temp:
                    values[keys[j]] = values[keys[j - gap]]
                    j -= gap
                values[keys[j]] = temp
            gap //= 2
        with open("sorted_numbers.txt", "w") as file:
            for key in keys:
                file.write(f"{key}\t{values[key]}\n")

def main():
    while True:
        print("Menú:")
        print("1. Generar un millón de números aleatorios y almacenarlos en un archivo de texto.")
        print("2. Ordenar los números almacenados en el archivo de texto con el método de ordenamiento por shell.")
        print("3. Salir.")
        option = int(input("Ingrese la opción que desea realizar: "))
        if option == 1:
            num_values = 1000000
            generate_random_numbers(num_values)
            print("Los números aleatorios han sido generados y almacenados en un archivo de texto.")
        elif option == 2:
            sort_numbers()
            print("Los números almacenados en el archivo de texto han sido ordenados y almacenados en un nuevo archivo.")
        elif option == 3:
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()

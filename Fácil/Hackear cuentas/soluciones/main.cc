#include <iostream>
#include <string>
#include <vector>

int main() {
    try {
        std::string input;
        std::getline(std::cin, input);
        long long vida = std::stoll(input);

        std::getline(std::cin, input); // Línea vacía
        std::vector<long long> empleado;
        long long total = 0;
        long long suma = 0;
        while (std::getline(std::cin, input)) {
            input.erase(input.find_last_not_of(" \n\r\t") + 1);
            if (input.empty()) { // Si hay una línea vacía cambiamos de empleado
                if (suma >= vida) {
                    total += suma;
                }
                suma = 0;
            } else {
                suma += std::stoll(input);
            }
        }

        if (suma >= vida) { // Como no termina con línea vacía tenemos que comprobarlo fuera otra vez
            total += suma;
        }

        std::cout << total << std::endl;
    } catch (std::exception& e) {
        // Manejo de excepciones
    }

    return 0;
}

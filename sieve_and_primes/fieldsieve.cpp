#include <iostream>
#include <vector>
#include <cmath>
#include <ctime>

std::vector<int> sieve_of_eratosthenes(int n) {
    std::vector<bool> sieve(n + 1, true);
    std::vector<int> primes;
    for (int p = 2; p <= std::sqrt(n); ++p) {
        if (sieve[p]) {
            primes.push_back(p);
            for (int i = p * p; i <= n; i += p) {
                sieve[i] = false;
            }
        }
    }
    for (int i = std::sqrt(n) + 1; i <= n; ++i) {
        if (sieve[i]) {
            primes.push_back(i);
        }
    }
    return primes;
}

int find_factor(int n) {
    std::vector<int> primes = sieve_of_eratosthenes(std::sqrt(n) + 1);
    for (int p : primes) {
        if (n % p == 0) {
            return p;
        }
    }
    return -1;
}

std::vector<int> number_field_sieve(int n) {
    std::vector<int> factors;
    while (true) {
        int factor = find_factor(n);
        if (factor != -1) {
            factors.push_back(factor);
            n /= factor;
        } else {
            factors.push_back(n);
            break;
        }
    }
    return factors;
}

int main() {
    long long int number = 280682857807;
    clock_t start_time = clock();
    std::vector<int> factors = number_field_sieve(number);
    clock_t end_time = clock();
    std::cout << "Factors of " << number << " are: ";
    for (int factor : factors) {
        std::cout << factor << " ";
    }
    std::cout << "\nExecution time: " << double(end_time - start_time) / CLOCKS_PER_SEC << " seconds\n";
    return 0;
}

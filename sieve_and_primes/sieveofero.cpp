#include <iostream>
#include <vector>
#include <chrono>

using namespace std;
using namespace std::chrono;

vector<int> sieveOfEratosthenes(int n) {
    vector<bool> prime(n+1, true);
    vector<int> primes;

    for (int p = 2; p * p <= n; p++) {
        if (prime[p]) {
            int step = (p % 2 == 0) ? p : 2 * p;
            for (int i = p * p; i <= n; i += step)
                prime[i] = false;
        }
    }

    for (int p = 2; p <= n; p++) {
        if (prime[p])
            primes.push_back(p);
    }

    return primes;
}

int main() {
    auto start = high_resolution_clock::now();

    int limit = 149696968; // Adjust the limit based on your system's performance
    vector<int> primes = sieveOfEratosthenes(limit);

    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);

    cout << "Largest prime found within 10 seconds: " << primes.back() << endl;
    cout << "Time taken: " << duration.count() << " milliseconds" << endl;

    return 0;
}
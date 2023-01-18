#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
// Variabel
int data[10] = {3, 5, 2, 4, 1, 7, 6, 8, 9, 10}; // Data yang akan ditampilkan
int maks = 0; // Nilai maksimum dari data
// Mencari nilai maksimum dari data
for (int i = 0; i < 10; i++)
{
    if (data[i] > maks)
    {
        maks = data[i];
    }
}

// Menampilkan grafik batang
for (int i = maks; i >= 1; i--)
{
    for (int j = 0; j < 10; j++)
    {
        if (data[j] >= i)
        {
            cout << "* ";
        }
        else
        {
            cout << "  ";
        }
    }
    cout << endl;
}

return 0;
}

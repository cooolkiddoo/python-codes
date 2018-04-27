
#include <algorithm>
#include <iostream>
using namespace std;

void printSmall(int arr[], int asize, int n)
{

    vector<int> copy_arr(arr, arr + asize);
 

    sort(copy_arr.begin(), copy_arr.begin() + asize);
 
  
    for (int i = 0; i < asize; ++i)
        if (binary_search(copy_arr.begin(), 
                copy_arr.begin() + n, arr[i]))
            cout << arr[i] << " ";
}

int main()
{
    int arr[] = { 1, 5, 8, 9, 6, 7, 3, 4, 2, 0 };
    int asize = sizeof(arr) / sizeof(arr[0]);    
    int n = 5;
    printSmall(arr, asize, n);
    return 0;

#include <iostream>
#include <vector>

int binary_search(const std::vector<int> &arr, int item);

int main()
{
    std::vector<int> data = {1, 2, 3, 4, 5};
    std::cout << binary_search(data, 2) << "\n";
    std::cout << binary_search(data, 5) << "\n";
    std::cout << binary_search(data, -2) << "\n";

    return 0;
}

int binary_search(const std::vector<int> &arr, int item)
{
    int low = 0;
    int high = arr.size() - 1;
    int mid;
    int guess;
    while (low <= high)
    {
        mid = (low + high) / 2;
        guess = arr[mid];
        if (item == guess)
        {
            return mid;
        }
        else if (item < guess)
        {
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }
    return -1;
}
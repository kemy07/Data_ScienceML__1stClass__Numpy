import  numpy as np
def main():

    # Searching
    arr3 = np.array ( [ 1 , 2 , 3  , 7 , 10 , 6 , 4 , 4 ] )
    x = np.where (arr3 == 4)
    print("Searching  : " , x)
    # finding the indexes where the values are even
    arr_even = np.array([1, 2, 3, 4, 6, 4, 4])
    even = np.where(arr_even % 2 == 0)
    print("Index of Even Num Is   : ", even)
    # Sorting
    print("The Sorted Array Is   : " ,np.sort(arr3))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import  numpy as np
def main():

    ###############################################
    # How To  Shape and Reshape Array

    arr2 = np.array([1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 ,  ])
    new_arr = arr2.reshape(4 , 3)
    print(new_arr)
    print("################### ")

    # Flattening means that --> converting a m.dim array into 1D array
    arr3 = np.array ([[1 , 2 , 3 ] , [3 , 6 , 4] ])
    new_arr3 = arr3.reshape(-1)
    print("Flattening " , new_arr3)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

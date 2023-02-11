import  numpy as np
def main():
    # zero - D Array
    # arr = np.array(42)
    # print(arr)
    # print(type(arr))
    # one - D Array
    # arr = np.array([1 , 2 , 3 ])
    # print(arr)
    # print(type(arr))
    ###############################################
    # How To Know The Degree Array using np.ndim
    arr1 = np.array(42)
    arr_test = np.array(6523)
    arr2 = np.array([1 , 2 , 3 ])
    arr3 = np.array ([[1 , 2 , 3 ] , [3 , 6 , 4] ])
    print(arr1.ndim)
    print(arr2.ndim)
    print(arr3.ndim)
    print(arr_test.ndim)
    #print(type(arr))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

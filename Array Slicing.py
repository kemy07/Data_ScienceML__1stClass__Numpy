import  numpy as np
def main():

    # Array Slicing : taking elements from one given index to another given index
    # Array Slicing 1-D Array
    arr = np.array ([1 , 2 , 3 , 4 , 5 , 6 , 7])
    print("Array Slicing " , arr [1:5:2])    #1 --> start
                                             #5 --> End
                                             #2 --> Step
    # Array Slicing 2-D Array
    arr2 = np.array([ [1, 2, 3] , [5, 6, 7] ])
    print("Array Slicing ", arr2[0,1:4])    # 0 is the array you want to slice
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

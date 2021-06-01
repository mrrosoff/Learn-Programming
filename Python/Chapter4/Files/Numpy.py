
import numpy as np

if __name__ == "__main__":

    # Sometimes you are going to want to do Math. Real Math. Matrix Math. Or whatever. Numpy is your friend!!!

    # The import line above will probably be red. Import numpy by rolling over it and clicking install!

    # Here is a numpy array. This is basically a list, but its a numpy list, so it does different stuff!

    anArray = np.array([1, 2, 3, 4, 5])
    print(anArray)

    # What do these do?

    print(anArray.mean())
    print(anArray.std())

    # Statistics! Useful!

    # What about a 2D Matrix?

    aMatrix = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])

    print(aMatrix)

    # You can do Matrix things

    print(aMatrix.transpose() @ aMatrix)

    # Or see the number of rows and cols

    print(aMatrix.shape)

    # The uses are endless! See the numpy documentation if you want to learn more!

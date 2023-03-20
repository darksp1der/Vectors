import matplotlib.pyplot as plt
import numpy as np


class MyVector:
    """
    the properties of each vector are:
        name as a given string
        color given as one letter(possible values: 'r', 'g', 'b', 'y' and 'm'
        type given as a positive integer greater of equal to 1
        values given as a list of numbers
    """
    def __init__(self, n, c, t, v):
        self.__name = n
        if c != "r" and c != "g" and c != "b" and c != "y" and c != "m":
            raise AttributeError("The color is not available")
        self.__color = c
        if t < 1:
            raise ValueError("The type must be greater or equal to 1")
        else:
            self.__type = t
        self.__values = v[:]

    """
    get and set the name, color, type and the list of values for a vector
    """
    def get_name(self):
        return str(self.__name)

    def get_color(self):
        return str(self.__color)

    def get_type(self):
        return self.__type

    def get_values(self):
        return self.__values[:]

    def set_name(self, n):
        self.__name = n

    def set_color(self, c):
        if c != "r" and c != "g" and c != "b" and c != "y" and c != "m":
            raise AttributeError("The color is not available")
        else:
            self.__color = c

    def set_type(self, t):
        if t > 0:
            self.__type = t
        else:
            raise ValueError("t must be greater or equal to 1")

    def set_values(self, v):
        self.__values = v[:]
    """
    the string representation of a vector
    """
    def __repr__(self):
        r = "Vector(" + str(self.__name) + ", " + str(self.__color)
        r += ", " + str(self.__type) + ", " + str(self.__values) + ")"
        return r

    """
    the functions in the 1st iteration
    """

    # Add a scalar to a vector
    def add_scalar(self,scalar):
        for i in range(len(self.__values)):
            self.__values[i] += scalar

    # Add two vectors
    def add_vectors(self,other):
        if len(self.__values) != len(other) != 0:
            raise IndexError("The vectors dont have the same length")
        else:
            for i in range(len(other)):
                self.__values[i] += other[i]

    # Subtract two vectors
    def sub_vectors(self,other):
        if len(self.__values) != len(other) != 0:
            raise IndexError("The vectors dont have the same length")
        else:
            for i in range(len(other)):
                self.__values[i] -= other[i]

    # Multiplication
    def multiplication(self,other):
        if len(self.__values) != len(other) != 0:
            raise IndexError("The vectors dont have the same length")
        else:
            p = 0
            s = 0
            for i in range(len(other)):
                p = self.__values[i] * other[i]
                s += p
        return s

    # Sum of elements in a vector
    def sum_of_elem(self):
        if len(self.__values) == 0:
            return None
        else:
            s = 0
            for i in range(len(self.__values)):
                s += self.__values[i]
            return s

    # Product of elements in a vector
    def product(self):
        if len(self.__values) == 0:
            return None
        else:
            p = 1
            for i in range(len(self.__values)):
                p *= self.__values[i]
            return p

    # Average of elements in a vector
    def average(self):
        if len(self.__values) == 0:
            return None
        else:
            s = 0
            for i in range(len(self.__values)):
                s += self.__values[i]
            avg = s / len(self.__values)
            return avg

    # Minimum of a vector
    def min_of_vect(self):
        if len(self.__values) == 0:
            return None
        else:
            mini = self.__values[0]
            for i in range(1,len(self.__values)):
                if self.__values[i] < mini:
                    mini = self.__values[i]
            return mini

    # Maximum of a vector
    def max_of_vect(self):
        if len(self.__values) == 0:
            return None
        else:
            maxi = self.__values[0]
            for i in range(1,len(self.__values)):
                if self.__values[i] > maxi:
                    maxi = self.__values[i]
            return maxi


class VectorRepository:

    """
    data is the list of vectors
    """
    def __init__(self,data):
        self.__data = data[:]
        for i in range(len(self.__data)):
            for j in range(i+1,len(self.__data)):
                if self.__data[i].get_name() == self.__data[j].get_name():
                    raise ValueError("The names cannot be the same")

    """
    the functions in the 2nd iteration
    """
    # Add a vector to the repository
    def add_to_rep(self,n,c,t,v):
        for i in range(len(self.__data)):
            if self.__data[i].get_name() == n:
                raise ValueError("The name already exists")
            else:
                vector = MyVector(n,c,t,v)
                self.__data.append(vector)

    # Get all vectors
    def get_all_vect(self):
        return self.__data[:]

    # Get a vector at a given index
    def get_vect_by_index(self,index):
        if index < 0 or index > len(self.__data)-1:
            raise IndexError("The index is not well defined")
        else:
            return self.__data[index]

    # Update a vector at a given index
    def update_vect_by_index(self,index,n,c,t,v):
        if index < 0 or index > len(self.__data) - 1:
            raise IndexError("The index is not well defined")
        else:
            self.__data[index].set_name(n)
            self.__data[index].set_color(c)
            self.__data[index].set_type(t)
            self.__data[index].set_values(v)

    # Update a vector identified by name_id
    def update_vect_by_name(self,name,n,c,t,v):
        for i in range(len(self.__data)):
            if self.__data[i].get_name() == n:
                raise AttributeError("The name is taken")
        for i in range(len(self.__data)):
            if self.__data[i].get_name() == name:
                self.__data[i].set_name(n)
                self.__data[i].set_color(c)
                self.__data[i].set_type(t)
                self.__data[i].set_values(v)

    # Delete a vector by index
    def del_vect_by_index(self,index):
        if index < 0 or index > len(self.__data) - 1:
            raise IndexError("The index is not well defined")
        else:
            del self.__data[index]

    # Delete a vector by name_id
    def del_vect_by_name(self,name):
        for i in range(len(self.__data)):
            if self.__data[i].get_name() == name:
                del self.__data[i]

    # Plot all vectors in a chart based on the type and colour of each vector
    # On the X axis
    # 1 - circle, 2 - square, 3 - triangle, others - diamond
    def PlotVectors(self):
        for i in range(len(self.__data)):
            x = []
            for j in range(len(self.__data[i].get_values())):
                x.append(j)
            t = self.__data[i].get_type()
            if t == 1:
                marker = "o"  # o - representation of a circle
            elif t == 2:
                marker = "s"  # s - representation of a square
            elif t == 3:
                marker = "v"  # v - representation of a triangle down
            else:
                marker = "D"  # D - representation of diamond in matplotlib
            plt.scatter(x,self.__data[i].get_values(),s = 100,c = self.__data[i].get_color(),marker = marker)
        plt.title("Vectors")
        plt.show()

    """
    The functions in the 3rd iteration using the functions
    in library numpy
    """

    # Add a scalar to a vector using numpy add
    def add_scalar_np(self,scalar,index):
        v = np.add(self.__data[index].get_values(),scalar)
        return v[:]

    # Add two vectors using numpy add
    def add_vectors_np(self,index,other):
        v = np.add(self.__data[index].get_values(),other)
        return v[:]

    # Subtract two vectors using numpy sub
    def sub_vectors_np(self,index,other):
        v = np.sub(self.__data[index].get_values(),other)
        return v[:]

    # Get the dot product of two vectors using numpy dot
    def multiplication_np(self,index,other):
        v = np.dot(self.__data[index].get_values(),other)
        return v

    # Get the sum of elements in the vector using numpy sum
    def sum_of_elem_np(self,index):
        v = np.sum(self.__data[index].get_values())
        return v

    # Get the product of elements in a vector using numpy prod
    def prod_of_elem_np(self,index):
        v = np.prod(self.__data[index].get_values())
        return v

    # Get the average of elements in a vector using numpy average
    def avg_of_elem_np(self,index):
        v = np.average(self.__data[index].get_values())
        return v

    # Get the minimum value in a vector using numpy min
    def min_of_vect_np(self,index):
        v = np.min(self.__data[index].get_values())
        return v

    # Get the maximum value in a vector using numpy max
    def max_of_vect_np(self,index):
        v = np.max(self.__data[index].get_values())
        return v


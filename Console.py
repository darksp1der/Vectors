from Logic import VectorRepository
from Logic import MyVector


def printmenu():
    # Displays the menu
    msg = "Menu:\n"
    msg += "\t 1 Add scalar to a vector\n"
    msg += "\t 2 Add two vectors\n"
    msg += "\t 3 Subtract two vectors\n"
    msg += "\t 4 Multiplication\n"
    msg += "\t 5 Get sum of elements in a vector\n"
    msg += "\t 6 Get product of elements in a vector\n"
    msg += "\t 7 Get the average of elements in a vector\n"
    msg += "\t 8 Get minimum of a vector\n"
    msg += "\t 9 Get maximum of a vector\n"
    msg += "\t 10 Add a vector to repository\n"
    msg += "\t 11 Get all vectors\n"
    msg += "\t 12 Update a vector at a given index\n"
    msg += "\t 13 Update a vector by name_id\n"
    msg += "\t 14 Delete a vector by index\n"
    msg += "\t 15 Delete a vector by name_id\n"
    msg += "\t 16 Plot all vectors in a chart\n"
    msg += "\t 0 Exit\n"
    print(msg)


def main():
    # Starts the app
    my_vectors = VectorRepository([MyVector(1,"r",2,[1,2,3]),MyVector(2,"b",3,[3,4,5])])

    stop = False
    while stop == False:
        printmenu()
        option = int(input("Enter option:"))
        if option == 0:
            print("Goodbye!")
            stop = True
        elif option == 1:
            scalar = int(input("The scalar:"))
            for i in range(len(my_vectors.get_all_vect())):
                my_vectors.get_vect_by_index(i).add_scalar(scalar)
            print("The new vectors are:",my_vectors.get_all_vect())
        elif option == 2:
            other = []
            print("Give the length of the vector you want to add")
            n = int(input("n="))
            print("Give the elements of the vector:")
            for i in range(n):
                x = int(input("x="))
                other.append(x)
            for i in range(len(my_vectors.get_all_vect())):
                my_vectors.get_vect_by_index(i).add_vectors(other)
            print("The new vectors are:", my_vectors.get_all_vect())
        elif option == 3:
            other = []
            print("Give the length of the vector you want to subtract")
            n = int(input("n="))
            print("Give the elements of the vector:")
            for i in range(n):
                x = int(input("x="))
                other.append(x)
            for i in range(len(my_vectors.get_all_vect())):
                my_vectors.get_vect_by_index(i).sub_vectors(other)
            print("The new vectors are:", my_vectors.get_all_vect())
        elif option == 4:
            other = []
            print("Give the length of the vector you want to multiply")
            n = int(input("n="))
            print("Give the elements of the vector:")
            for i in range(n):
                x = int(input("x="))
                other.append(x)
            for i in range(len(my_vectors.get_all_vect())):
                print(my_vectors.get_vect_by_index(i).multiplication(other))
        elif option == 5:
            for i in range(len(my_vectors.get_all_vect())):
                print(my_vectors.get_vect_by_index(i).sum_of_elem())
        elif option == 6:
            for i in range(len(my_vectors.get_all_vect())):
                print(my_vectors.get_vect_by_index(i).product())
        elif option == 7:
            for i in range(len(my_vectors.get_all_vect())):
                print(my_vectors.get_vect_by_index(i).average())
        elif option == 8:
            for i in range(len(my_vectors.get_all_vect())):
                print(my_vectors.get_vect_by_index(i).min_of_vect())
        elif option == 9:
            for i in range(len(my_vectors.get_all_vect())):
                print(my_vectors.get_vect_by_index(i).max_of_vect())
        elif option == 10:
            values = []
            print("Give the name, the color and the type of the vector")
            name = str(input("name="))
            print("Available colors: r, g, b, y and m")
            c = str(input("color="))
            t = int(input("t="))
            print("Give the number of the elements")
            n = int(input("n="))
            print("Give the elements")
            for i in range(n):
                x = int(input("x="))
                values.append(x)
            my_vectors.add_to_rep(name,c,t,values)
        elif option == 11:
            print(my_vectors.get_all_vect())
        elif option == 12:
            values = []
            print("Give an index")
            index = int(input("i="))

            print("Give a new name, color, type and elements")
            name = str(input("name="))
            print("Available colors: r, g, b, y and m")
            c = str(input("color="))
            t = int(input("t="))
            print("Give the number of elements")
            n = int(input("n="))
            print("Give the elements")
            for i in range(n):
                x = int(input("x="))
                values.append(x)
            my_vectors.update_vect_by_index(index,name,c,t,values)
        elif option == 13:
            values = []
            print("Give a name_id")
            name_id = str(input("name_id="))

            print("Give a new name, color, type and elements")
            name = str(input("name="))
            print("Available colors: r, g, b, y and m")
            c = str(input("color="))
            t = int(input("t="))
            print("Give the number of elements")
            n = int(input("n="))
            print("Give the elements")
            for i in range(n):
                x = int(input("x="))
                values.append(x)
            my_vectors.update_vect_by_name(name_id, name, c, t, values)
        elif option == 14:
            print("Give an index")
            index = int(input("i="))
            my_vectors.del_vect_by_index(index)
        elif option == 15:
            print("Give a name_id")
            name = str(input("name="))
            my_vectors.del_vect_by_name(name)
        elif option == 16:
            my_vectors.PlotVectors()
        elif option == 17:
            scalar = int(input("The scalar:"))
            index = int(input("The index:"))
            print(my_vectors.add_scalar_np(scalar,index))
        elif option == 18:
            index = int(input("The index:"))
            other = [1,2,3]
            print(my_vectors.add_vectors_np(index,other))
        elif option == 19:
            index = int(input("The index:"))
            other = [1, 2, 3]
            print(my_vectors.sub_vectors_np(index, other))
        elif option == 20:
            index = int(input("The index:"))
            other = [1, 2, 3]
            print(my_vectors.multiplication_np(index,other))
        elif option == 21:
            index = int(input("The index:"))
            print(my_vectors.sum_of_elem_np(index))
        elif option == 22:
            index = int(input("The index:"))
            print(my_vectors.prod_of_elem_np(index))
        elif option == 23:
            index = int(input("The index:"))
            print(my_vectors.avg_of_elem_np(index))
        elif option == 24:
            index = int(input("The index:"))
            print(my_vectors.max_of_vect_np(index))
        elif option == 25:
            index = int(input("The index:"))
            print(my_vectors.min_of_vect_np(index))
        else:
            print("Invalid option")
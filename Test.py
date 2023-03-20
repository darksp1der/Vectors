from Logic import VectorRepository
from Logic import MyVector


"""
20 data examples for the functions
"""


def dataExamples():
    vector = VectorRepository()
    # 1
    vector.add_to_rep(1,"r",1,[1,2,3])
    print(vector) # [MyVector(1,"r",1,[1,2,3])]

    # 2
    vector.add_to_rep(2,"m",1,[2,3,4])
    print(vector) # [MyVector(1,"r",1,[1,2,3]), MyVector(2,"m",1,[2,3,4])]

    # 3
    vector.add_to_rep(3,"y",1,[3,4,5])
    print(vector) # [MyVector(1,"r",1,[1,2,3]), MyVector(2,"m",1,[2,3,4]), MyVector(3,"y",1,[3,4,5])]

    # 4
    vector.del_vect_by_index(2)
    print(vector) # [MyVector(1,"r",1,[1,2,3]), MyVector(2,"m",1,[2,3,4])]

    # 5
    vector.del_vect_by_name(1)
    print(vector) # [MyVector(2,"m",1,[2,3,4])]

    # 6
    vector.update_vect_by_index(0,3,"r",2,[1,2])
    print(vector) # [MyVector(3,"r",2,[1,2])]

    # 7
    vector.update_vect_by_name(3,1,"y",1,[1])
    print(vector) # [MyVector(1,"y",1,[1])]

    # 8
    vector.update_vect_by_name(1, 2, "b", 2, [5,6,6])
    print(vector)  # [MyVector(2,"b",2,[5,6,6])]

    # 9
    vector.update_vect_by_index(0, 5, "r", 5, [100, 120])
    print(vector)  # [MyVector(5,"r",5,[100,120])]

    # 10
    vector.del_vect_by_index(0)
    print(vector) # []

    vector = VectorRepository([MyVector(1,"r",1,[1,2,3]),MyVector(2,"b",2,[2,3,4]),MyVector(3,"y",3,[3,4,5])])

    # 11
    vector.get_vect_by_index(0).add_scalar(2)
    print(vector) # [MyVector(1,"r",1,[3,4,5]),MyVector(2,"b",2,[2,3,4]),MyVector(3,"y",3,[3,4,5])]

    # 12
    vector.get_vect_by_index(1).add_scalar(10)
    print(vector) # [MyVector(1,"r",1,[3,4,5]),MyVector(2,"b",2,[12,13,14]),MyVector(3,"y",3,[3,4,5])]

    # 13
    vector.get_vect_by_index(2).add_scalar(-5)
    print(vector) # [MyVector(1,"r",1,[3,4,5]),MyVector(2,"b",2,[12,13,14]),MyVector(3,"y",3,[-2,-1,0])]

    # 14
    vector.get_vect_by_index(0).add_vector([1,2,3])
    print(vector)  # [MyVector(1,"r",1,[4,6,8]),MyVector(2,"b",2,[12,13,14]),MyVector(3,"y",3,[-2,-1,0])]

    # 15
    vector.get_vect_by_index(1).add_vector([3, 4, 5])
    print(vector)  # [MyVector(1,"r",1,[4,6,8]),MyVector(2,"b",2,[15,17,19]),MyVector(3,"y",3,[-2,-1,0])]

    # 16
    vector.get_vect_by_index(2).add_vector([-1, -1, -1])
    print(vector)  # [MyVector(1,"r",1,[4,6,8]),MyVector(2,"b",2,[15,17,19]),MyVector(3,"y",3,[-3,-2,-1])]

    # 17
    print(vector.get_vect_by_index(0).product()) # 192

    # 18
    print(vector.get_vect_by_index(1).product())  # 4845

    # 19
    print(vector.get_vect_by_index(0).average())  # 6

    # 20
    print(vector.get_vect_by_index(2).average())  # -2


"""
test functions for each function in Logic:
    in class MyVector
    in class VectorRepository
"""
def test_add_to_rep():
    test = VectorRepository()
    assert test.add_to_rep(1,"r",1,[1,2,3]) == [[1,"r",1,[1,2,3]]]
    assert test.add_to_rep(2, "b", 2, [1, 5, 3]) == [[1,"r",1,[1,2,3]],[2,"b",2,[1,5,3]]]
    assert test.add_to_rep(3, "r", 1, [1, 10, 2]) == [[1,"r",1,[1,2,3]],[2,"b",2,[1,5,3]],[3, "r", 1, [1,10,2]]]


def test_get_all_vect():
    test = VectorRepository()
    test.add_to_rep(1, "r", 1, [1, 2, 3])
    assert test.get_all_vect() == [[1,"r",1,[1,2,3]]]

    test.add_to_rep(2, "b", 2, [1, 5, 3])
    assert test.get_all_vect() == [[1,"r",1,[1,2,3]], [2,"b",2,[1,5,3]]]

    test.add_to_rep(3, "r", 1, [1, 10, 2])
    assert test.get_all_vect() == [[1,"r",1,[1,2,3]],[2,"b",2,[1,5,3]],[3, "r", 1, [1,10,2]]]


def test_get_vect_by_index():
    test = VectorRepository()
    test.add_to_rep(1, "r", 1, [1, 2, 3])
    test.add_to_rep(2, "b", 2, [1, 5, 3])
    test.add_to_rep(3, "r", 1, [1, 10, 2])

    assert test.get_vect_by_index(0) == [[1,"r",1,[1,2,3]]]
    assert test.get_vect_by_index(1) == [[2,"b",2,[1,5,3]]]
    assert test.get_vect_by_index(2) == [[3,"r",1,[1,10,2]]]


def test_update_vect_by_index():
    test = VectorRepository()
    test.add_to_rep(1, "r", 1, [1, 2, 3])
    test.add_to_rep(2, "b", 2, [1, 5, 3])
    test.add_to_rep(3, "r", 1, [1, 10, 2])

    assert test.update_vect_by_index(0,2,"b",3,[1]) == [[2,"b",3,[1]]]
    assert test.update_vect_by_index(1,1,"y",4,[44,51]) == [[1,"y",4,[44,51]]]
    assert test.update_vect_by_index(2,5,"b",5,[1,2,9]) == [[5,"b",5,[1,2,9]]]


def test_update_vect_by_name():
    test = VectorRepository()
    test.add_to_rep(1, "r", 1, [1, 2, 3])
    test.add_to_rep(2, "b", 2, [1, 5, 3])
    test.add_to_rep(3, "r", 1, [1, 10, 2])

    assert test.update_vect_by_index(1, 2, "b", 3, [1]) == [[2, "b", 3, [1]]]
    assert test.update_vect_by_index(2, 1, "y", 4, [44, 51]) == [[1, "y", 4, [44, 51]]]
    assert test.update_vect_by_index(3, 5, "b", 5, [1, 2, 9]) == [[5, "b", 5, [1, 2, 9]]]


def test_del_vect_by_index():
    test = VectorRepository()
    test.add_to_rep(1, "r", 1, [1, 2, 3])
    test.add_to_rep(2, "b", 2, [1, 5, 3])
    test.add_to_rep(3, "r", 1, [1, 10, 2])

    assert test.del_vect_by_index(0) == [[2, "b", 2, [1, 5, 3]],[3, "r", 1, [1, 10, 2]]]
    assert test.del_vect_by_index(1) == [[1, "r", 1, [1, 2, 3]], [3, "r", 1, [1, 10, 2]]]
    assert test.del_vect_by_index(2) == [[1, "r", 1, [1, 2, 3]], [2, "b", 2, [1, 5, 3]]]


def test_del_vect_by_name():
    test = VectorRepository()
    test.add_to_rep(1, "r", 1, [1, 2, 3])
    test.add_to_rep(2, "b", 2, [1, 5, 3])
    test.add_to_rep(3, "r", 1, [1, 10, 2])

    assert test_del_vect_by_name(3) == [[1, "r", 1, [1, 2, 3]], [2, "b", 2, [1, 5, 3]]]
    assert test_del_vect_by_name(2) == [[1, "r", 1, [1, 2, 3]], [3, "r", 1, [1, 10, 2]]]
    assert test_del_vect_by_name(1) == [[2, "b", 2, [1, 5, 3]],[3, "r", 1, [1, 10, 2]]]


def test_add_scalar():
    test = MyVector(1,"r",1,[1,2,3])

    assert test.add_scalar(2) == [[1,"r",1,[3,4,5]]]
    assert test.add_scalar(0) == [[1,"r",1,[1,2,3]]]
    assert test.add_scalar(-1) == [[1,"r",1,[0,1,2]]]


def test_add_vectors():
    test = MyVector(1,"r",1,[1,2,3])

    assert test.add_vectors([1,2,3]) == [[1,"r",1,[4,6,8]]]
    assert test.add_vectors([0,0,0]) == [[1,"r",1,[1,2,3]]]
    assert test.add_vectors([2,2,2]) == [[1,"r",1,[3,4,5]]]


def test_sub_vectors():
    test = MyVector(1,"r",1,[1,2,3])

    assert test.sub_vectors([0,0,0]) == [[1,"r",1,[1,2,3]]]
    assert test.sub_vectors([1,2,3]) == [[1,"r",1,[0,0,0]]]
    assert test.sub_vectors([1,1,1]) == [[1,"r",1,[0,1,2]]]


def test_multiplication():
    test = MyVector(1,"r",1,[1,2,3])

    assert test.multiplication([0,0,0]) == 0
    assert test.multiplication([1,1,1]) == 6
    assert test.multiplication([2,2,2]) == 12


def test_sum_of_values():
    test = MyVector(1,"r",1,[1,2,3])
    assert test.sum_of_elem() == 6

    test = MyVector(1,"r",1,[2,4,6])
    assert test.sum_of_elem() == 12

    test = MyVector(1,"r",1,[2,-5,10])
    assert test.sum_of_elem() == 7


def product():
    test = MyVector(1, "r", 1, [1, 2, 3])
    assert test.product() == 6

    test = MyVector(1, "r", 1, [2, 4, 6])
    assert test.product() == 48

    test = MyVector(1, "r", 1, [2, -5, 10])
    assert test.product() == -100


def test_average():
    test = MyVector(1, "r", 1, [1, 2, 3])
    assert test.average() == 2

    test = MyVector(1, "r", 1, [2, 4, 6])
    assert test.average() == 4

    test = MyVector(1, "r", 1, [2, -5, 10])
    assert test.average() == -33.33


def test_min_of_vect():
    test = MyVector(1, "r", 1, [1, 2, 3])
    assert test.min_of_vect() == 1

    test = MyVector(1, "r", 1, [2, 4, 6])
    assert test.min_of_vect() == 2

    test = MyVector(1, "r", 1, [2, -5, 10])
    assert test.min_of_vect() == -5


def test_max_of_vect():
    test = MyVector(1, "r", 1, [1, 2, 3])
    assert test.max_of_vect() == 3

    test = MyVector(1, "r", 1, [2, 4, 6])
    assert test.max_of_vect() == 6

    test = MyVector(1, "r", 1, [2, -5, 10])
    assert test.max_of_vect() == 10
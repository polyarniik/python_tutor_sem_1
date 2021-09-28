list_ = ["a", "b", "dsf", 6]
l = list_


for ind in range(len(list_)):
    print(ind, list_[ind])

print("%" * 40)

for i, element in enumerate(list_, start=1):
    if element == "b":
        del l[i]
    print(i, element, sep=". ")

print(list_)


books_authors = {"Гарри Поттер": "Роулинг", "Зеленая миля": "Стивен"}

for k, v in books_authors.items():
    print(k, v, sep=", ")


print(list(books_authors.items()))

# books_authors.clear()

new_dict = books_authors

new_dict["1"] = 42332

print(books_authors)


new_set = set([1, 2, 3, 3])
print(new_set)


lst = [1, 2, 3, 4, 5, 6]
bilst = [[1, 2], [3, 4], [5, 6]]
print(lst[1])
print()
print(bilst[2], bilst[2][1])


def my_name(i):
    print(i, "Руслан")

my_name(2)


if __name__ == '__main__':

    my_name(1)

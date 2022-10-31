from copy import deepcopy


def is_singleton(factory):
    return factory() is factory()


# код ниже руками не трогать:
obj = ["1", "2", "3"]
res1 = is_singleton(lambda: obj)
res2 = is_singleton(lambda: deepcopy(obj))

print(f"{res1} {res2}")

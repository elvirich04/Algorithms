def LinearSearch(Dataset, keyword):
    for Data in Dataset:
        if (Data==keyword):
            return True
    return False
Dataset=["Alice", "Bob"]
result=LinearSearch(Dataset,"Bob")
print(result)

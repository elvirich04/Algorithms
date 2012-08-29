def Swap(Dataset,IndexToSwap1,IndexToSwap2):
    temp=Dataset[IndexToSwap1]
    Dataset[IndexToSwap1]=Dataset[IndexToSwap2]
    Dataset[IndexToSwap2]=temp
    return Dataset
Dataset=[3, 2, 1]
IndexStart=0
for IndexToCompare1 in range(IndexStart,len(Dataset)):
    for IndexToCompare2 in range(IndexToCompare1,len(Dataset)):
        if(Dataset[IndexToCompare1]>Dataset[IndexToCompare2]):
            Dataset=Swap(Dataset,IndexToCompare1,IndexToCompare2)

print(Dataset)

class Apple:
    def __init__ (self,Color):
        self.Color=Color
ListOfApples=[Apple("Red"),Apple("Red"),Apple("Green"),Apple("Red"),Apple("Red"),Apple("Green")]
IndexToSwap1=0
IndexToSwap2=2
IndexToSwap3=1
IndexToSwap4=5

temp=ListOfApples[IndexToSwap1]
ListOfApples[IndexToSwap1]=ListOfApples[IndexToSwap2]
ListOfApples[IndexToSwap2]=temp
ListOfApples[IndexToSwap3]=ListOfApples[IndexToSwap4]
ListOfApples[IndexToSwap4]=temp

for apples in ListOfApples:
    print("This apple is %s"%(apples.Color))




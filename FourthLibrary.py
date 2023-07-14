import decimal
class fourthClass():
    import decimal

    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine LearningNeural")
        print("NetworksVision")
        print("RoboticsSpeech")
        print("ProcessingNatural")
        print("Language")
        
    def OddEven():
        oe=int(input("Enter a Number:"))
        if(oe%2==0):
            print(oe,"is Even Number")
        else:
            print(oe, "is Odd Number")
            
    def Elegible():
        gender="Male"
        age=int(input("Enter the Age:"))
        print("Your Gender:",gender)
        print("Your Age:",age)
        if(age>=18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
            
    def percentage():
        Subject1= 98
        Subject2= 87
        Subject3= 95
        Subject4= 95
        Subject5= 93

        print("Subject1=", Subject1)
        print("Subject2=", Subject2)
        print("Subject3=", Subject3)
        print("Subject4=", Subject4)
        print("Subject5=", Subject5)
        total = Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total=", total)
        print("Percentage=",decimal.Decimal(total/5))
        
    def triangle():
        height=3
        breadth1=4
        area=(height*breadth1)/2
        height1=3
        height2=4
        breadth=45
        perimeter=height1+height2+breadth

        print("Height:",height)
        print("Breadth:",breadth1)
        print("Area of Triangle:",area)
        print("Height1:",height1)
        print("Height2",height2)
        print("breadth:",breadth)
        print("Perimeter of Triangle:",perimeter)
    
    
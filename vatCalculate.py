totalPrice = int(input("กรุณาใส่ตัวเลขเพื่อตรวจสอบ VAT. : "))
def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return(result)
print("มูลค่ารวม VAT. :",vatCalculate(totalPrice))
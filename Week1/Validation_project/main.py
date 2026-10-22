from validators import (validate_age,validate_price,validate_number)


def main():
    try:
        print("Number : " , validate_number(12))
        print("Age :", validate_age(10))
        print("Price :", validate_price(100))

    except (ValueError , TypeError) as e :
        print("Error : ", e)
    

if __name__ == "__main__":
    main()
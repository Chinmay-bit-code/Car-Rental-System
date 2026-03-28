class Car:
    def __init__(self, car_id, brand, model, base_price_per_day):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.base_price_per_day = base_price_per_day
        self.is_available = True

    def get_car_id(self):
        return self.car_id

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_base_price_per_day(self):
        return self.base_price_per_day

    def is_available_for_rent(self):
        return self.is_available

    def rent(self):
        self.is_available = False

    def return_car(self):
        self.is_available = True

    def calculate_price(self, rental_days, locality, is_member):
        # locality multiplier
        locality_multiplier = {
            "mumbai": 1.5,
            "pune": 1.2,
            "delhi": 1.4,
            "nagpur": 1.0
        }

        multiplier = locality_multiplier.get(locality.lower(), 1.0)
        price = self.base_price_per_day * rental_days * multiplier

        # distance/long rental discount
        if rental_days > 10:
            price *= 0.85  # 15% discount
        elif rental_days > 5:
            price *= 0.90  # 10% discount

        # membership discount
        if is_member:
            price *= 0.85  # 15% membership discount

        return price


class Customer:
    def __init__(self, customer_id, name, is_member):
        self.customer_id = customer_id
        self.name = name
        self.is_member = is_member

    def get_customer_id(self):
        return self.customer_id

    def get_name(self):
        return self.name

    def is_member_func(self):
        return self.is_member


class Rental:
    def __init__(self, car, customer, days, locality):
        self.car = car
        self.customer = customer
        self.days = days
        self.locality = locality

    def get_car(self):
        return self.car

    def get_customer(self):
        return self.customer

    def get_days(self):
        return self.days

    def get_locality(self):
        return self.locality


class CarRentalSystem:
    def __init__(self):
        self.cars = []
        self.customers = []
        self.rentals = []

    def add_car(self, car):
        self.cars.append(car)

    def add_customer(self, customer):
        self.customers.append(customer)

    def rent_car(self, car, customer, days, locality):
        if car.is_available_for_rent():
            car.rent()
            self.rentals.append(Rental(car, customer, days, locality))
        else:
            print("Car is not available for rent.")

    def return_car(self, car):
        car.return_car()
        rental_to_remove = None
        for rental in self.rentals:
            if rental.get_car() == car:
                rental_to_remove = rental
                break
        if rental_to_remove:
            self.rentals.remove(rental_to_remove)
            print("Car returned Successfully ✅")
        else:
            print("Car was not rented.")

    def menu(self):
        while True:
            print("\n===== Car Rental System =====")
            print("1. Rent a Car")
            print("2. Return a Car")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                print("\n== Rent a Car ==\n")
                customer_name = input("Enter your name: ")

                member_input = input("Are you a Premium Member? (yes/no): ")
                is_member = member_input.lower() == "yes"

                locality = input("Enter your locality (Mumbai/Pune/Delhi/Nagpur): ")

                print("\nAvailable Cars:")
                for car in self.cars:
                    if car.is_available_for_rent():
                        print(f"{car.get_car_id()} - {car.get_brand()} {car.get_model()} "
                              f"| ₹{car.get_base_price_per_day()} per day")

                car_id = input("\nEnter the car ID you want to rent: ")
                rental_days = int(input("Enter the number of days for rental: "))

                new_customer = Customer(f"CUS{len(self.customers) + 1}", customer_name, is_member)
                self.add_customer(new_customer)

                selected_car = None
                for car in self.cars:
                    if car.get_car_id() == car_id and car.is_available_for_rent():
                        selected_car = car
                        break

                if selected_car:
                    total_price = selected_car.calculate_price(rental_days, locality, is_member)
                    print("\n== Rental Information ==\n")
                    print(f"Customer ID: {new_customer.get_customer_id()}")
                    print(f"Customer Name: {new_customer.get_name()}")
                    print(f"Car: {selected_car.get_brand()} {selected_car.get_model()}")
                    print(f"Locality: {locality}")
                    print(f"Rental Days: {rental_days}")
                    print(f"Total Price: ₹{total_price:.2f}")

                    confirm = input("\nConfirm rental (Y/N): ")

                    if confirm.lower() == "y":
                        self.rent_car(selected_car, new_customer, rental_days, locality)
                        print("\nCar rented successfully ✅")
                    else:
                        print("\nRental canceled.")
                else:
                    print("\nInvalid car selection or car not available for rent.")

            elif choice == "2":
                print("\n== Return a Car ==\n")
                car_id = input("Enter the car ID you want to return: ")

                car_to_return = None
                for car in self.cars:
                    if car.get_car_id() == car_id and not car.is_available_for_rent():
                        car_to_return = car
                        break

                if car_to_return:
                    customer = None
                    for rental in self.rentals:
                        if rental.get_car() == car_to_return:
                            customer = rental.get_customer()
                            break

                    if customer:
                        self.return_car(car_to_return)
                        print(f"Car returned successfully by {customer.get_name()}")
                    else:
                        print("Car was not rented or rental information is missing.")
                else:
                    print("Invalid car ID or car is not rented.")

            elif choice == "3":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

        print("\nThank you for using the Car Rental System!")


if __name__ == "__main__":
    rental_system = CarRentalSystem()

    car1 = Car("C001", "Toyota", "Camry", 60.0)
    car2 = Car("C002", "Honda", "Accord", 70.0)
    car3 = Car("C003", "Mahindra", "Thar", 150.0)

    rental_system.add_car(car1)
    rental_system.add_car(car2)
    rental_system.add_car(car3)

    rental_system.menu()

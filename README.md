# 🚗 Car Rental System

A command-line based Car Rental Management System built in Python using Object-Oriented Programming principles. It supports dynamic pricing based on locality, rental duration, and membership status.

---

## Overview

The Car Rental System simulates a real-world vehicle rental workflow through a terminal-based interface. Users can browse available cars, provide rental details, receive a dynamic price quote, confirm the booking, and return vehicles — all within a clean, menu-driven experience.

---

## Features

- **Browse Available Cars** — View cars currently available for rent with their base prices
- **Dynamic Pricing Engine** — Calculates rental cost based on:
  - City/locality multipliers
  - Rental duration discounts (long-term bookings)
  - Premium membership discounts
- **Rental Confirmation Flow** — Review a full cost breakdown before confirming
- **Car Return System** — Return rented cars and free them up for other customers
- **OOP Architecture** — Clean separation of concerns across four core classes

---

## Project Structure

```
car-rental-system/
│
├── car_rental.py       # Main application file containing all classes and entry point
└── README.md
```

---

## Classes & Responsibilities

| Class | Responsibility |
|---|---|
| `Car` | Represents a vehicle with ID, brand, model, pricing, availability, and cost calculation |
| `Customer` | Stores customer details including ID, name, and membership status |
| `Rental` | Links a car, customer, rental duration, and locality into a single rental record |
| `CarRentalSystem` | Manages the car fleet, customer list, active rentals, and the interactive menu |

---

## Pricing Logic

The final price is computed as:

```
Final Price = Base Price Per Day × Rental Days × Locality Multiplier
             × Long-Rental Discount × Membership Discount
```

### Locality Multipliers

| City    | Multiplier |
|---------|------------|
| Mumbai  | 1.5×       |
| Delhi   | 1.4×       |
| Pune    | 1.2×       |
| Nagpur  | 1.0×       |
| Other   | 1.0×       |

### Duration Discounts

| Rental Duration | Discount |
|-----------------|----------|
| More than 10 days | 15% off |
| 6 – 10 days       | 10% off |
| Up to 5 days      | No discount |

### Membership Discount

| Status          | Discount |
|-----------------|----------|
| Premium Member  | 15% off  |
| Non-member      | No discount |

> **Note:** All discounts are applied sequentially (multiplicative), not combined additively.

---

## Usage

Once launched, you will be presented with the main menu:

```
===== Car Rental System =====
1. Rent a Car
2. Return a Car
3. Exit
```

**To rent a car:**
1. Select option `1`
2. Enter your name, membership status, and locality
3. Choose a car from the available list
4. Enter the number of rental days
5. Review the price breakdown and confirm

**To return a car:**
1. Select option `2`
2. Enter the Car ID you wish to return

---

*Built with Python · Object-Oriented Design · CLI Interface*
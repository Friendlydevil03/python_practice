from abc import ABC, abstractmethod

print("=" * 70)
print("INHERITANCE vs ABSTRACTION - What's the Difference?")
print("=" * 70)

# ============================================
# SCENARIO 1: REGULAR INHERITANCE (Code Reuse)
# ============================================
print("\n📚 REGULAR INHERITANCE - Purpose: REUSE CODE")
print("-" * 70)


class Animal:
    """Parent class with ACTUAL working code"""

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating... 🍽️")

    def sleep(self):
        print(f"{self.name} is sleeping... 😴")

    def move(self):
        print(f"{self.name} is moving... 🚶")


class Dog(Animal):
    """Child class REUSES parent's code"""

    def bark(self):
        print(f"{self.name} says: Woof! 🐕")


class Cat(Animal):
    """Child class REUSES parent's code"""

    def meow(self):
        print(f"{self.name} says: Meow! 🐈")


print("\n✅ Inheritance gives us FREE code:")
dog = Dog("Buddy")
dog.eat()  # ← Got this FREE from Animal class!
dog.sleep()  # ← Got this FREE from Animal class!
dog.move()  # ← Got this FREE from Animal class!
dog.bark()  # ← Dog's own method

cat = Cat("Whiskers")
cat.eat()  # ← Got this FREE from Animal class!
cat.sleep()  # ← Got this FREE from Animal class!

# ============================================
# SCENARIO 2: ABSTRACTION (Enforce Rules)
# ============================================
print("\n\n🎯 ABSTRACTION - Purpose: ENFORCE RULES")
print("-" * 70)


class PaymentMethod(ABC):
    """Abstract class - NO working code, just RULES"""

    @abstractmethod
    def process_payment(self, amount):
        """Rule: You MUST implement this!"""
        pass

    @abstractmethod
    def refund(self, amount):
        """Rule: You MUST implement this!"""
        pass


class CreditCard(PaymentMethod):
    """MUST implement all abstract methods"""

    def process_payment(self, amount):
        print(f"💳 Processing ${amount} via Credit Card")

    def refund(self, amount):
        print(f"💳 Refunding ${amount} to Credit Card")


class PayPal(PaymentMethod):
    """MUST implement all abstract methods"""

    def process_payment(self, amount):
        print(f"🅿️ Processing ${amount} via PayPal")

    def refund(self, amount):
        print(f"🅿️ Refunding ${amount} to PayPal")


print("\n✅ Abstraction enforces that ALL payment methods have same methods:")
card = CreditCard()
card.process_payment(100)

paypal = PayPal()
paypal.process_payment(100)

# ============================================
# THE KEY DIFFERENCE
# ============================================
print("\n\n" + "=" * 70)
print("⚡ THE KEY DIFFERENCE")
print("=" * 70)

print("\n❌ Try to create incomplete implementation with regular inheritance:")


class Bird(Animal):
    """Missing fly() but it still works!"""
    pass


bird = Bird("Tweety")
bird.eat()  # Works fine! No error!
print("✓ Bird created successfully - No enforcement!")

print("\n❌ Try to create incomplete implementation with abstraction:")


class Bitcoin(PaymentMethod):
    """Only implemented ONE method, missing refund()"""

    def process_payment(self, amount):
        print(f"₿ Processing ${amount} via Bitcoin")
    # Missing refund() method!


try:
    bitcoin = Bitcoin()
    print("✓ Bitcoin created successfully")
except TypeError as e:
    print(f"✗ ERROR: {e}")
    print("👉 Abstraction FORCES you to implement ALL methods!")

# ============================================
# WHEN TO USE WHAT?
# ============================================
print("\n\n" + "=" * 70)
print("🤔 WHEN TO USE WHAT?")
print("=" * 70)

print("""
📚 USE INHERITANCE when:
  ✓ You want to REUSE existing code
  ✓ Parent has WORKING implementations
  ✓ "IS-A" relationship (Dog IS-A Animal)

  Example: All animals eat/sleep the same way
           → Put it in parent, reuse it!

🎯 USE ABSTRACTION when:
  ✓ You want to ENFORCE a contract
  ✓ Different classes need DIFFERENT implementations
  ✓ You want to ensure consistency

  Example: All payments need process/refund methods
           BUT each payment method works DIFFERENTLY
           → Use abstraction to enforce the rule!
""")

# ============================================
# THE REAL POWER: COMBINING BOTH!
# ============================================
print("\n" + "=" * 70)
print("💪 THE REAL POWER: INHERITANCE + ABSTRACTION!")
print("=" * 70)


class Vehicle(ABC):
    """Abstract class with BOTH rules AND reusable code"""

    def __init__(self, brand):
        self.brand = brand

    # ✅ Concrete method - REUSABLE code
    def show_brand(self):
        print(f"Brand: {self.brand}")

    # ✅ Abstract method - ENFORCED rule
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print(f"🚗 {self.brand} Car: Engine started with key")

    def stop_engine(self):
        print(f"🚗 {self.brand} Car: Engine stopped")


class Bike(Vehicle):
    def start_engine(self):
        print(f"🏍️ {self.brand} Bike: Engine started with kick")

    def stop_engine(self):
        print(f"🏍️ {self.brand} Bike: Engine stopped")


print("\n✅ Both get show_brand() for FREE (inheritance)")
print("✅ Both MUST implement start/stop (abstraction)\n")

car = Car("Toyota")
car.show_brand()  # ← FREE from parent (inheritance)
car.start_engine()  # ← Must implement (abstraction)

bike = Bike("Harley")
bike.show_brand()  # ← FREE from parent (inheritance)
bike.start_engine()  # ← Must implement (abstraction)

# ============================================
# SUMMARY
# ============================================
print("\n\n" + "=" * 70)
print("📊 SUMMARY TABLE")
print("=" * 70)
print("""
┌─────────────────┬──────────────────────┬────────────────────────┐
│                 │    INHERITANCE       │      ABSTRACTION       │
├─────────────────┼──────────────────────┼────────────────────────┤
│ Purpose         │ Code REUSE           │ Contract ENFORCEMENT   │
│ Parent has      │ Working code         │ Just rules (no code)   │
│ Child gets      │ FREE methods         │ MUST implement methods │
│ Focus           │ "Don't repeat code"  │ "Follow the rules"     │
│ Flexibility     │ Optional override    │ MANDATORY implement    │
│ Use when        │ Same behavior        │ Different behaviors    │
│ Example         │ All animals eat()    │ Each payment differs   │
└─────────────────┴──────────────────────┴────────────────────────┘

🎯 KEY INSIGHT:
   Inheritance = "Here's working code, use it!"
   Abstraction = "Here's the rules, follow them!"

   You can use BOTH together! 💪
""")

print("\n" + "=" * 70)
print("🏦 YOUR ATM CODE")
print("=" * 70)
print("""
Your code uses ABSTRACTION because:

❌ NOT code reuse:
   - user_show has NO working code (just 'pass')
   - ATM can't reuse anything

✅ YES contract enforcement:
   - user_show says: "MUST have these 5 methods"
   - ATM MUST implement all 5
   - Ensures every ATM has same interface

If you wanted code REUSE, you'd write:

class BasicATM:
    def common_security_check(self):
        # Actual working code here
        print("Checking security...")

class AdvancedATM(BasicATM):
    # Gets common_security_check() for FREE!
    pass

That's inheritance for reuse! 📚
""")
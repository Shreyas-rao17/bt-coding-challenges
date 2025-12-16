"""
HealWell Care Hospital Billing System

Supports:
1. Interactive mode (when running normally)
2. Evaluation mode (through solve(input_data))

All 8 levels implemented:
- Patient details
- Service selection
- Cost lookup
- Subtotal
- GST
- Invoice generation
- Admin configuration
- Discounts (senior + high bill)
"""

GST_RATE = 0.18
SENIOR_DISCOUNT = 0.10
HIGH_BILL_DISCOUNT = 0.05


# ------------------------------------------------------------
# Patient Class
# ------------------------------------------------------------

class Patient:
    def __init__(self, name, age, gender, contact):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact


# ------------------------------------------------------------
# Hospital System (Stores & updates services)
# ------------------------------------------------------------

class HospitalSystem:
    def __init__(self):
        self.services = [
            "General Consultation",
            "Blood Test",
            "Covid Test",
            "X-Ray",
            "CT Scan",
            "MRI"
        ]
        self.costs = [500, 300, 800, 1500, 4000, 7000]

    def update_services(self, names, cost_values):
        if len(names) != len(cost_values):
            raise ValueError("Service list and cost list must match.")
        self.services = names
        self.costs = cost_values

    def get_service_details(self, indices):
        selected_services = []
        selected_costs = []

        for idx in indices:
            if idx < 1 or idx > len(self.services):
                raise ValueError("Invalid service index.")
            selected_services.append(self.services[idx - 1])
            selected_costs.append(self.costs[idx - 1])

        return selected_services, selected_costs

    def print_services(self):
        print("Available Services:")
        for i, svc in enumerate(self.services, start=1):
            print(f"{i}. {svc} - ₹{self.costs[i-1]}")


# ------------------------------------------------------------
# Billing Engine
# ------------------------------------------------------------

class BillingEngine:
    def __init__(self, system):
        self.system = system

    def subtotal(self, costs):
        return sum(costs)

    def apply_discounts(self, age, subtotal):
        discount_total = 0
        current_total = subtotal

        if age >= 60:
            cut = current_total * SENIOR_DISCOUNT
            discount_total += cut
            current_total -= cut

        if current_total > 5000:
            cut = current_total * HIGH_BILL_DISCOUNT
            discount_total += cut
            current_total -= cut

        return current_total, discount_total

    def apply_gst(self, amount):
        gst = amount * GST_RATE
        return gst, amount + gst

    def generate_invoice(self, patient, services, costs, subtotal,
                         discount_amt, gst_amt, grand_total):

        lines = []
        lines.append("-----------------------------------------------")
        lines.append("HealWell Care Hospital")
        lines.append("Patient Invoice")
        lines.append("-----------------------------------------------")
        lines.append("Patient Information:")
        lines.append(f"Name: {patient.name}")
        lines.append(f"Age: {patient.age}")
        lines.append(f"Gender: {patient.gender}")
        lines.append(f"Contact: {patient.contact}")

        lines.append("Services Availed:")
        for i, (svc, cost) in enumerate(zip(services, costs), start=1):
            lines.append(f"{i}. {svc}: ₹{cost}")

        lines.append(f"Subtotal: ₹{subtotal}")

        if discount_amt > 0:
            lines.append(f"Discount Applied: -₹{discount_amt:.2f}")

        lines.append(f"GST (18%): ₹{gst_amt:.2f}")
        lines.append(f"Grand Total: ₹{grand_total:.2f}")
        lines.append("Thank you for choosing HealWell Care Hospital!")
        lines.append("-----------------------------------------------")

        return "\n".join(lines)


# ------------------------------------------------------------
# System instance (GLOBAL)
# ------------------------------------------------------------

HOSPITAL = HospitalSystem()


# ------------------------------------------------------------
# solve() for BT evaluation (NO INTERACTIVITY)
# ------------------------------------------------------------

def solve(input_data):
    tokens = input_data.split()
    if len(tokens) < 2:
        return "Invalid input"

    mode = tokens[0].upper()

    # ---------------- ADMIN MODE -----------------
    if mode == "ADMIN":
        try:
            count = int(tokens[1])
        except ValueError:
            return "Invalid input"
        
        if count <= 0:
            return "Invalid input"


        if len(tokens) != 2 + count * 2:
            return "Invalid input"

        new_services, new_costs = [], []
        i = 2

        for _ in range(count):
            name = tokens[i]
            try:
                cost = float(tokens[i + 1])
            except ValueError:
                return "Invalid input"

            new_services.append(name)
            new_costs.append(cost)
            i += 2

        try:
            HOSPITAL.update_services(new_services, new_costs)
        except ValueError:
            return "Invalid input"

        return "Services updated successfully"

    # ---------------- USER MODE -----------------
    elif mode == "USER":
        if len(tokens) < 6:
            return "Invalid input"

        name = tokens[1]

        try:
            age = int(tokens[2])
        except ValueError:
            return "Invalid input"

        gender = tokens[3]
        contact = tokens[4]

        try:
            count = int(tokens[5])
        except ValueError:
            return "Invalid input"
        
        if count <= 0:
            return "Invalid input"


        if len(tokens) != 6 + count:
            return "Invalid input"

        try:
            indices = list(map(int, tokens[6:]))
        except ValueError:
            return "Invalid input"

        try:
            patient = Patient(name, age, gender, contact)
            billing = BillingEngine(HOSPITAL)

            services, costs = HOSPITAL.get_service_details(indices)
            subtotal = billing.subtotal(costs)
            discounted_total, discount_amt = billing.apply_discounts(age, subtotal)
            gst_amt, grand_total = billing.apply_gst(discounted_total)

            return billing.generate_invoice(
                patient, services, costs, subtotal,
                discount_amt, gst_amt, grand_total
            )
        except ValueError:
            return "Invalid input"

    return "Invalid input"


# ------------------------------------------------------------
# INTERACTIVE MODE (ONLY WHEN RUN DIRECTLY)
# ------------------------------------------------------------

def run_interactive():
    print("Welcome to HealWell Care Hospital Billing System")
    print("Are you a:")
    print("1. Admin")
    print("2. Patient")

    choice = input("Enter 1 or 2: ").strip()

    # ---------------- ADMIN MODE -----------------
    if choice == "1":
        try:
            count = int(input("How many services to configure? "))
            new_services, new_costs = [], []

            for _ in range(count):
                name = input("Service name: ").strip()
                cost = float(input("Service cost: "))
                new_services.append(name)
                new_costs.append(cost)

            HOSPITAL.update_services(new_services, new_costs)
            print("Services updated successfully")

        except Exception:
            print("Invalid details. Try again.")

    # ---------------- PATIENT MODE -----------------
    elif choice == "2":
        name = input("Name: ").strip()
        age = int(input("Age: "))
        gender = input("Gender: ").strip()
        contact = input("Contact: ").strip()

        patient = Patient(name, age, gender, contact)
        billing = BillingEngine(HOSPITAL)

        print("\nServices Available Today:")
        HOSPITAL.print_services()

        count = int(input("How many services do you want? "))
        indices = []
        for _ in range(count):
            indices.append(int(input("Enter service index: ")))

        services, costs = HOSPITAL.get_service_details(indices)
        subtotal = billing.subtotal(costs)
        discounted_total, discount_amt = billing.apply_discounts(age, subtotal)
        gst_amt, grand_total = billing.apply_gst(discounted_total)

        invoice = billing.generate_invoice(
            patient, services, costs, subtotal,
            discount_amt, gst_amt, grand_total
        )
        print(invoice)

    else:
        print("Invalid choice. Exiting.")


if __name__ == "__main__":
    run_interactive()

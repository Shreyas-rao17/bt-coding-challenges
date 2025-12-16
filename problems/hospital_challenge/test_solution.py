import pytest
from solution import (
    solve,
    HOSPITAL,
    BillingEngine,
    Patient
)

# ============================================================
# ADMIN MODE TESTS
# ============================================================

def test_admin_update_services_correctly():
    result = solve("ADMIN 2 ECG 500 XRay 1200")
    assert result == "Services updated successfully"
    assert HOSPITAL.services == ["ECG", "XRay"]
    assert HOSPITAL.costs == [500.0, 1200.0]


def test_admin_invalid_cost_string():
    assert solve("ADMIN 1 ECG abc") == "Invalid input"


def test_admin_invalid_count_mismatch():
    assert solve("ADMIN 2 ECG 500") == "Invalid input"


def test_admin_zero_services():
    result = solve("ADMIN 0")
    assert result == "Invalid input"    # count=0 but no data


def test_admin_negative_cost():
    result = solve("ADMIN 1 ECG -500")
    # negative values are allowed mathematically, but check system stability
    assert HOSPITAL.costs[0] == -500.0 or result == "Services updated successfully"


# ============================================================
# BILLING ENGINE — DISCOUNT LOGIC
# ============================================================

def test_discount_senior_only():
    billing = BillingEngine(HOSPITAL)
    discounted, disc_amt = billing.apply_discounts(65, 3000)
    assert pytest.approx(discounted) == 2700
    assert pytest.approx(disc_amt) == 300


def test_discount_high_bill_only():
    billing = BillingEngine(HOSPITAL)
    discounted, disc_amt = billing.apply_discounts(30, 6000)
    assert pytest.approx(discounted) == 5700
    assert pytest.approx(disc_amt) == 300


def test_discount_senior_then_high_bill():
    billing = BillingEngine(HOSPITAL)
    discounted, disc_amt = billing.apply_discounts(70, 6000)
    # 6000 → 5400 (senior) → 5130 (high bill)
    assert pytest.approx(discounted) == 5130
    assert pytest.approx(disc_amt) == 870


def test_discount_no_eligibility():
    billing = BillingEngine(HOSPITAL)
    discounted, disc_amt = billing.apply_discounts(25, 3000)
    assert discounted == 3000
    assert disc_amt == 0


# ============================================================
# BILLING ENGINE — GST
# ============================================================

def test_gst_on_normal_amount():
    billing = BillingEngine(HOSPITAL)
    gst, total = billing.apply_gst(2000)
    assert pytest.approx(gst) == 360
    assert pytest.approx(total) == 2360


def test_gst_on_zero_amount():
    billing = BillingEngine(HOSPITAL)
    gst, total = billing.apply_gst(0)
    assert gst == 0
    assert total == 0


# ============================================================
# USER MODE — VALID FLOWS
# ============================================================

def test_user_flow_basic():
    solve("ADMIN 3 A 100 B 200 C 300")
    output = solve("USER Arjun 35 Male 9876 2 1 3")
    assert "A: ₹100.0" in output
    assert "C: ₹300.0" in output
    assert "Subtotal: ₹400" in output
    assert "GST (18%):" in output


def test_user_flow_senior_discount():
    solve("ADMIN 2 MRI 7000 XRay 1500")
    output = solve("USER Ravi 65 Male 5555 1 1")

    assert "Subtotal: ₹7000" in output
    assert "Discount Applied: -₹1015.00" in output
    assert "Grand Total: ₹7062.30" in output       


def test_user_flow_high_bill_discount():
    solve("ADMIN 1 MRI 7000")
    output = solve("USER Manoj 40 Male 1234 1 1")
    # 7000 → high bill discount → 6650 → GST → 7837
    assert "Grand Total" in output


def test_user_flow_both_discounts():
    solve("ADMIN 1 MRI 7000")
    output = solve("USER Raju 70 Male 9999 1 1")
    assert "Discount Applied" in output  # both discounts should appear


# ============================================================
# USER MODE — INVALID CASES
# ============================================================

def test_user_invalid_missing_fields():
    assert solve("USER Arjun 35") == "Invalid input"


def test_user_invalid_service_index():
    solve("ADMIN 2 A 100 B 200")
    assert solve("USER Akash 25 Male 9999 1 3") == "Invalid input"


def test_user_invalid_service_non_integer():
    assert solve("USER A 20 M 1234 1 abc") == "Invalid input"


def test_user_zero_services_requested():
    solve("ADMIN 1 A 100")
    assert solve("USER Test 20 M 1234 0") == "Invalid input"


# ============================================================
# INVOICE FORMAT & CONTENT
# ============================================================

def test_invoice_contains_patient_details():
    solve("ADMIN 2 A 100 B 200")
    output = solve("USER Kiran 32 Male 1122 1 1")

    assert "Name: Kiran" in output
    assert "Age: 32" in output
    assert "Gender: Male" in output
    assert "Contact: 1122" in output


def test_invoice_service_listing():
    solve("ADMIN 2 A 100 B 200")
    output = solve("USER Rhea 20 Female 9988 2 1 2")

    assert "1. A: ₹100.0" in output
    assert "2. B: ₹200.0" in output


def test_invoice_totals_correct():
    solve("ADMIN 2 A 100 B 100")
    output = solve("USER Rohan 50 Male 5555 2 1 2")

    assert "Subtotal: ₹200" in output
    assert "GST (18%): ₹36.00" in output
    assert "Grand Total: ₹236.00" in output

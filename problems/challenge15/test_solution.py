"""
Tests for report generation.
"""

from solution import generate_report

def test_report():
    report = generate_report("John", "E123", 50000, 600000, 550000, 30000, 570000)
    assert "John" in report
    assert "E123" in report
    assert "50000.00" in report
"""
Farmer sales calculation.
"""

def calculate_farmer_sales():
    """
    Calculate total sales and chemical-free sales at 11 months.

    Returns:
        tuple: (total_sales, chemical_free_sales_11_months)
    """
    total_land = 80
    segments = 5
    land_per_segment = total_land / segments  # 16

    # Yields per acre
    tomato_yield_30pct = 10  # tonne/acre
    tomato_yield_70pct = 12
    potato_yield = 10
    cabbage_yield = 14
    sunflower_yield = 0.7
    sugarcane_yield = 45

    # Prices
    tomato_price_per_kg = 7
    potato_price_per_kg = 20
    cabbage_price_per_kg = 24
    sunflower_price_per_kg = 200
    sugarcane_price_per_tonne = 4000

    # Tomato sales
    tomato_land_30pct = land_per_segment * 0.3  # 4.8
    tomato_land_70pct = land_per_segment * 0.7  # 11.2
    tomato_yield_total = (tomato_land_30pct * tomato_yield_30pct +
                          tomato_land_70pct * tomato_yield_70pct)  # 182.4
    tomato_sales = tomato_yield_total * 1000 * tomato_price_per_kg  # tonne to kg

    # Potato sales
    potato_yield_total = land_per_segment * potato_yield  # 160
    potato_sales = potato_yield_total * 1000 * potato_price_per_kg

    # Cabbage sales
    cabbage_yield_total = land_per_segment * cabbage_yield  # 224
    cabbage_sales = cabbage_yield_total * 1000 * cabbage_price_per_kg

    # Sunflower sales
    sunflower_yield_total = land_per_segment * sunflower_yield  # 11.2
    sunflower_sales = sunflower_yield_total * 1000 * sunflower_price_per_kg

    # Sugarcane sales
    sugarcane_yield_total = land_per_segment * sugarcane_yield  # 720
    sugarcane_sales = sugarcane_yield_total * sugarcane_price_per_tonne

    # Total sales
    total_sales = (tomato_sales + potato_sales + cabbage_sales +
                   sunflower_sales + sugarcane_sales)

    # Chemical-free at 11 months: vegetables (6 months) + sunflower (4 months done by month 10)
    # Sugarcane starts month 11, not done
    chemical_free_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales

    return total_sales, chemical_free_sales

if __name__ == "__main__":
    total, cf = calculate_farmer_sales()
    print(f"a. Overall sales: Rs. {total:,.0f}")
    print(f"b. Chemical-free sales at 11 months: Rs. {cf:,.0f}")
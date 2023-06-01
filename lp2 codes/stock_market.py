def get_stock_recommendation(stock_data):
    print("Expert System: Analyzing stock market data...")
    recommendation = "Hold"  # Default recommendation

    # Extract relevant information from stock_data
    stock_price = stock_data["price"]
    moving_average = stock_data["moving_average"]
    rsi = stock_data["rsi"]

    # Analyze stock market data and generate recommendation
    if stock_price < moving_average:
        if rsi < 30:
            recommendation = "Buy"
        else:
            recommendation = "Hold"
    else:
        if rsi > 70:
            recommendation = "Sell"
        else:
            recommendation = "Hold"

    return recommendation

# Example stock data
stock_data = {
    "price": 100,
    "moving_average": 95,
    "rsi": 40
}

# Main function
def main():
    recommendation = get_stock_recommendation(stock_data)
    print("Expert System Recommendation:", recommendation)

# Run the expert system
if __name__ == '__main__':
    main()

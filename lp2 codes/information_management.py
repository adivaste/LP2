def get_information_recommendation(file_types, file_sizes):
    print("Expert System: Analyzing information management data...")
    recommendation = "Organize your files based on file types"  # Default recommendation

    # Analyze information management data and generate recommendation
    if len(file_types) > 0:
        recommendation = "Organize your files based on file types"
    elif len(file_sizes) > 0:
        total_size = sum(file_sizes)
        if total_size > 1000:
            recommendation = "Perform disk cleanup to free up space"
        else:
            recommendation = "No specific recommendation at the moment"
    else:
        recommendation = "No specific recommendation at the moment"

    return recommendation

# Example information management data
file_types = ["doc", "pdf", "jpg", "xlsx"]
file_sizes = [500, 200, 1500, 300]

# Main function
def main():
    recommendation = get_information_recommendation(file_types, file_sizes)
    print("Expert System Recommendation:", recommendation)

# Run the expert system
if __name__ == '__main__':
    main()

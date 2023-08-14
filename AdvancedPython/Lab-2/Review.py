def extract_review_data(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    review_data = []
    total_reviews = 0
    valid_reviews = 0
    invalid_reviews = 0
    total_ratings = 0

    for line in lines:
        if "= =" in line or ("=" + '\n') in line:
            invalid_reviews += 1
        else:
            valid_reviews += 1

    for line in lines:
        parts = line.strip().split("=")
        if len(parts) >= 5:
            p_id, c_id, date, re_rat, review = parts[:5]
            if re_rat.strip():  # Check if re_rat is not an empty string
                total_reviews += 1
                total_ratings += float(re_rat)
                review_data.append((p_id, int(re_rat)))

    avg_rating = total_ratings / total_reviews if total_reviews > 0 else 0

    return review_data, total_reviews, avg_rating, valid_reviews, invalid_reviews


def main():
    product_files = ["product1.txt", "product2.txt", "product3.txt", "product4.txt"]
    product_reviews = [extract_review_data(file) for file in product_files]

    print("Product ID, Total number of reviews, Average rating, Valid reviews, Invalid reviews\n")
    for product_review in product_reviews:
        print(product_review[0][0], product_review[1], product_review[2], product_review[3], product_review[4])

    avg_rating_dict = {review[0][0]: review[2] for review in product_reviews}
    print("\nDictionary of average ratings:\n")
    print(avg_rating_dict)

    sorted_avg_ratings = sorted(avg_rating_dict.items(), key=lambda x: x[1], reverse=True)
    print("\nSorted dictionary by average ratings:\n")
    print(sorted_avg_ratings)

    with open("summary.txt", 'w') as f:
        f.write("Product ID, Total number of reviews, Average rating, Valid reviews, Invalid reviews\n")
        f.write("\n".join([str(review) for review in product_reviews]) + "\n")

        f.write("\nProducts' average ratings in descending order:\n")
        f.write(str(sorted_avg_ratings))

if __name__ == '__main__':
    main()

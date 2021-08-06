from reviews import neg_list, pos_list, neg_counter, pos_counter

review = "The crib was amazing!"

total_reviews = len(pos_list) + len(neg_list)

percent_pos = len(pos_list) / total_reviews

percent_neg = len(neg_list) / total_reviews

percent_pos = 0.5
percent_neg = 0.5



total_pos = sum(pos_counter.values())
total_neg = sum(neg_counter.values())

review_words = review.split(" ")
# print(review_words)

word_in_pos, word_in_neg = {}, {}

pos_probability = 1
neg_probability = 1

review_words = review.split()

for word in review_words:
  word_in_pos = pos_counter[word]
  word_in_neg = neg_counter[word]
  
  pos_probability *= (word_in_pos + 1) / (total_pos + len(pos_counter)) #smoothening: result... 

  neg_probability *= (word_in_neg + 1) / (total_neg + len(neg_counter))

  final_pos, final_neg = pos_probability * percent_pos, neg_probability * percent_neg

  print(final_pos, final_neg)

  if final_pos > final_neg:
    print("The review is positive")
  else:
    print("The review is negative")




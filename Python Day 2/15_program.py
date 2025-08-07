#convert str1 to snake
str1 = 'All silver Tea Cup'
words = str1.lower().split()      # ['all', 'silver', 'tea', 'cup']
words[-1] += 's'                  # make last word plural
snake = '_'.join(words)           # 'all_silver_tea_cups'
print(snake)

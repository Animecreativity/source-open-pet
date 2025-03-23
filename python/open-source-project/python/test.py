for i, v in enumerate(['a', 'skip', 'b', 'c']):
    if v == 'skip':
        continue  # В некоторых случаях есть необходимость пропустить некоторые элементы.
    print(i, v)
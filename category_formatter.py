if __name__ == '__main__':
    category_file_old = open('CategoryList_unformatted.txt', 'r')
    Lines = category_file_old.readlines()

    category_file_new = open("CategoryList.txt", "w")

    for line in Lines:
        category_unformmated = line.strip()
        category_noCaps = category_unformmated.lower()
        category_formatted = category_noCaps.replace(" ", "-")

        print(category_formatted)
        category_file_new.write(category_formatted.strip() + "\n")

    category_file_new.close()

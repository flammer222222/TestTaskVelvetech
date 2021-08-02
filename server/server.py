from filter.filter import FilterBadWords


if __name__ == '__main__':
    test_string = "rkrrk aslpsap anus slfd sfaf anal analsssd ddd bunny fucker"
    my_filter = FilterBadWords('../filter/resources/list_of_bad_words.txt')
    print(my_filter.filter(test_string))
from word2number import w2n
# import enchant

def namingConventionCheck(Identifier):
    # d = enchant.Dict("en_US")
    # print(help(enchant))
    
    final_list = {}
    accepted = ['c','d','e','g','i','in','inOut','j','m','n','o','out','t','x','y','z']
    # print(len(identifier_list))
    # for Identifier in identifier_list:
    temp = Identifier.split("_")
    failed_convention = []
    count = 0
    i=0
    for elem in Identifier:
        if elem.isupper():
            count += 1
    if Identifier[0].isupper():
        failed_convention.append('Capitalization Anomaly')
        print('hi')
    if "__" in Identifier:
        failed_convention.append('Consecutice Underscores')
    # elif d.check(Identifier):
    #     return False
    # for i in temp:
    #     d = enchant("en-US")
    #     if d.check(temp[i]) is False:
    #         failed_convention.append('Dictonary Words')
    if count > 4:
        failed_convention.append('Excessive Words')
    if Identifier.startswith("_") or Identifier.endswith("_"):
        failed_convention.append('External Underscores')
    if len(Identifier) > 1:
        # print(Identifier)
        if Identifier[0].islower() and Identifier[1].isupper():
            failed_convention.append('Identidier Encoding')
    if len(Identifier) > 26:
        failed_convention.append('Long Identifier Name')
    lower_word_list = [word for word in temp if word.islower()]
    upper_word_list = [word for word in temp if word.isupper()]
    if len(lower_word_list) >= 1 and  len(upper_word_list) >=1:
        failed_convention.append('Naming Convention Anomaly')
    if count<2 or count>4:
        failed_convention.append('Number Of Words')
    try:
        for words in temp:
            w2n.word_to_num(words)
        failed_convention.append('Numeric Identifier Name')
    except:
        pass
    if len(Identifier)<8 and Identifier not in accepted:
        failed_convention.append('Short Identifier Name')
    # final_list[Identifier]=failed_convention
    # print(final_list) 
    print(failed_convention)
    return failed_convention


# print(namingConventionCheck("rajath1234"))
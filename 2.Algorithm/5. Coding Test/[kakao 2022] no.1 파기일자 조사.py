from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    terms_dict = defaultdict(str)
    for terms_input in range(len(terms)):
        term_name, term_month = terms[terms_input].split()
        terms_dict[term_name] = int(term_month)
    for checking in range(len(privacies)):
        cus_dates, cus_terms = privacies[checking].split()
        cus_year, cus_month, cus_date = cus_dates.split('.')
        cus_year = int(cus_year)
        cus_month = int(cus_month) + terms_dict[cus_terms]
        while cus_month > 12:
            cus_year += 1
            cus_month -= 12
        if int(''.join(str(cus_year) + str(cus_month) + cus_date)) <= int(today.replace(',', '')):
            answer.append(checking+1)


print(solution('2016.11.13', ))
from underscore import _
import re

BASIC_POSTCODE_REGEX = '^[A-Z]{1,2}[0-9R][0-9A-Z]? ?[0-9][A-Z]{2}$'


def format_address_string(address_string):

    def remove_whitespace(x, index, list):
        return x.strip()

    def uppercase_if_postcode(x, index, list):
        return x.upper() if re.search(BASIC_POSTCODE_REGEX,x.upper()) else x

    def handle_house_number(result, x, index):
        if index == 1 and result[0].isdigit():
            result = [result[0] + ' ' + x]
        else:
            result.append(x)
        return result

    def make_postcode_last(context, x, index):
        if index > 1 and re.search(BASIC_POSTCODE_REGEX,context[index-1]):
            postcode = context[index-1]
            context[index-1] = x
            context.append(postcode)
        else:
            context.append(x)
        return context

    return _(address_string.split(',')).chain()\
        .map(remove_whitespace)\
        .map(uppercase_if_postcode)\
        .reduce(handle_house_number, [])\
        .reduce(make_postcode_last, [])\
        .value()

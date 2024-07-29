import pytest
from source.palindrome import check_palindromes 

@pytest.mark.parametrize("input_words, expected", [
    (["madam", "admam", "mdama", "dmama"], {
        "madam": {
            "is_palindrome": True,
            "can_form_palindrome": True
        },
        "admam": {
            "is_palindrome": False,
            "can_form_palindrome": True
        },
        "mdama": {
            "is_palindrome": False,
            "can_form_palindrome": True
        },
        "dmama": {
            "is_palindrome": False,
            "can_form_palindrome": True
        }
    })
])
def test_check_palindromes(input_words, expected):
    result = check_palindromes(input_words)
    assert result == expected

import pytest
from processing import remove_links,remove_hastags,remove_numbers,remove_users, perform_stemming, perform_lemmatization

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Check out this #awesome link: http://example.com", "Check out this  link: "),
        ("No hashtags or links here!", "No hashtags or links here!"),
        (123, 123),  
    ],
)
def test_remove_hashtags_and_links(input_text, expected_output):
    processed_text = remove_hastags(remove_links(input_text))
    assert processed_text == expected_output
    
    
@pytest.mark.parametrize("input_text, expected_output", [
    ("Testing @user123 regex 456removal", "Testing  regex removal"),
    ("No changes needed", "No changes needed"),
    ("1234567890", ""),
    ("@user1 @user2 @user3", '  '),
])
def test_remove_numbers_and_users(input_text, expected_output):
    processed_text = remove_numbers(remove_users(input_text))
    assert processed_text == expected_output

@pytest.mark.parametrize("input_text, expected_output", [
    ("Python programmers often tend like programming in python because it's like english. We call people who program in python pythonistas.",
    "  python programm often tend like program in python becaus it be like english . we call peopl who program in python pythonista ."),
    ("The quick brown foxes are jumping over the lazy dogs.", "  the quick brown fox be jump over the lazi dog ."),
    ("The striped bats are hanging on their feet for best", "  the stripe bat be hang on their foot for good"),
    ('The SECs social media account announced the approval of an investment product linked to Bitcoin, which was viewed as a win.',
     '  the sec social medium account announc the approv of an inv product link to bitcoin , which wa view as a win .'),
     ('What happens in Vegas, it turns out, really does stay in Vegas','  what happen in vega , it turn out , realli doe stay in vega')
])
def test_remove_perform_lemmatization_and_stemming(input_text, expected_output):
    processed_text = perform_lemmatization(perform_stemming(input_text))
    assert processed_text == expected_output


if __name__ == "__main__":
    pytest.main()
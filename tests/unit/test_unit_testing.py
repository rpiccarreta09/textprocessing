import pytest
from processing import *

@pytest.mark.parametrize("text, expected", [
    ("Hi How are you!$%&/()", "Hi How are you"),
    ("This is an example/()=?", "This is an example"),
    ("Christmas is !""#the best time of the year%&/()==)()", "Christmas is the best time of the year"),
    
])
def test_remove_characters(text, expected):
    assert remove_characters(text) == expected

@pytest.mark.parametrize("text, expected", [
    (['I','like','playing','computer','games'], [ 'like', 'playing', 'computer', 'games']),
    (['hate', 'fast', 'food', 'restaurants'], ['hate', 'fast', 'food', 'restaurants']),
    (['The','best','book','of','all','times','is','from','kafka'], ['best', 'book', 'times', 'kafka'])
    
])
def test_remove_stopwords(text, expected):
    assert remove_stopwords2(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("THIS IS A TEST", "this is a test"),
    ("I LIKE READING COMICS", "i like reading comics"),
    ("THE APPLE PIE IS MY FAVOURITE", "the apple pie is my favourite")
    
])
def test_convert_to_lowercase(text, expected):
    assert convert_to_lowercase(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("🌟Just finished an amazing workout session! Feeling so energized and ready to conquer the day!💪", "Just finished an amazing workout session! Feeling so energized and ready to conquer the day!"),
    ("😞Stuck in traffic again... why does this always happen during rush hour?", "Stuck in traffic again... why does this always happen during rush hour?"),
    ("📉Disappointed with the latest company decision. Feels like a step backward instead of forward.", "Disappointed with the latest company decision. Feels like a step backward instead of forward."),
   
])
def test_remove_emojis(text, expected):
    assert remove_emojis(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("Stuck in traffic  again...  why  does  this", "Stuck in traffic again... why does this"),
    ("Just  finished  an  amazing workout  session", "Just finished an amazing workout session"),
    ("There's  nothing  like a  peaceful morning", "There's nothing like a peaceful morning"),
])
def test_remove_extra_spaces(text, expected):
    assert remove_extra_spaces(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("123abc456def789", "abcdef"),
    ("Stuck in traffic again 123abc456def789", "Stuck in traffic again abcdef"),
    ("Disappointed with the latest company decision. Feels 12343", "Disappointed with the latest company decision. Feels "),
    # Add more test cases here for remove_numbers
])
def test_remove_numbers(text, expected):
    assert remove_numbers(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("Just had an amazing brainstorming session with @TechInnovator21! Their innovative ideas are always inspiring. 💡🚀 #Collaboration #Innovation","Just had an amazing brainstorming session with  Their innovative ideas are always inspiring. 💡🚀 #Collaboration #Innovation"),
    ("Attended a seminar by @MarketingGuru45 today! Their insights on social media strategies were incredibly enlightening. 📱✨ #MarketingTips #LearnFromTheBest","Attended a seminar by  today! Their insights on social media strategies were incredibly enlightening. 📱✨ #MarketingTips #LearnFromTheBest"),
    ("Had a fantastic interview with @MusicMaestro88! Their passion for music truly shines through. 🎶🎤 #MusicalGenius #InterviewInsights","Had a fantastic interview with  Their passion for music truly shines through. 🎶🎤 #MusicalGenius #InterviewInsights")
])
def test_remove_users(text, expected):
    assert remove_users(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("Exploring new heights 🏞️ #AdventureTime #PeakViews", "Exploring new heights 🏞️  "),
    ("Baking bliss 🥖🍰 #HomeBakerJoys #OvenMagic", "Baking bliss 🥖🍰  "),
    ("Fitness journey begins! 💪🏋️ #NewGoals #HealthyHabits","Fitness journey begins! 💪🏋️  "),

])
def test_remove_hastags(text, expected):
    assert remove_hastags(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("This is a link: https://example.com", "This is a link: "),
    ("Learn how to master coding basics in no time! 💻🚀 Link: https://codinglessons.com/basics #CodingSkills #TechEducation", "Learn how to master coding basics in no time! 💻🚀 Link:  #CodingSkills #TechEducation"),
    # Add more test cases here for remove_links
])
def test_remove_links(text, expected):
    assert remove_links(text) == expected
    
    

def test_remove_stopwords_invalid_input():
    invalid_input = "This is a string, not a list"
    with pytest.raises(ValueError):
        remove_stopwords2(invalid_input)

@pytest.mark.parametrize("text, expected", [
    ("Programmers program with programming languages", " programm program with program languag"),
    ("Bitcoin will go to the stars for sure this year", " bitcoin will go to the star for sure thi year"),
    ("Donald Trump will beat the heck out of Joe Biden in the 2024 elections"," donald trump will beat the heck out of joe biden in the 2024 elect"),
    ('The paper has become one of the most common algorithms for stemming in English',' the paper ha becom one of the most common algorithm for stem in english'),
    ('If you are looking to reset your relationship with food, consider starting with some reading.',' if you are look to reset your relationship with food , consid start with some read .')])

def test_perform_stemming(text, expected):
  assert perform_stemming(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("The quick brown foxes are jumping over the lazy dogs.", "the quick brown fox be jump over the lazy dog ."),
    ("We call people who program in python pythonistas.", "we call people who program in python pythonistas ."),
    ("Get Python Testing with pytest now with the learning platform","get Python testing with pyt now with the learn platform"),
    ('The commenters have spoken, and they strongly recommend this recipe for rosemary white beans with frizzled onions and tomato.',
     'the commenter have speak , and they strongly recommend this recipe for rosemary white bean with frizzle onion and tomato .'),
     ('A series of powerful storms were wreaking havoc across the U.S. on Tuesday, bringing significant weather of nearly every variety to large parts of the Pacific Northwest, the Plains, the Midwest, the South and the East Coast.',
      'a series of powerful storm be wreak havoc across the U.S. on Tuesday , bring significant weather of nearly every variety to large part of the Pacific Northwest , the Plains , the Midwest , the South and the East Coast .')])

def test_perform_lemmatization(text, expected):
  assert perform_lemmatization(text) == expected


if __name__ == "__main__":
    pytest.main()



from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()

def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"

def generate_post(length, language, tag, tone):
    prompt = get_prompt(length, language, tag, tone)
    response = llm.invoke(prompt)
    post_text = response.content
    hashtags = few_shot.generate_hashtags([tag])  # Generate hashtags from the tag
    return post_text + "\n\n" + hashtags

def get_prompt(length, language, tag, tone):
    length_str = get_length_str(length)

    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    4) Tone: {tone}
    If Language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be in English.
    '''
    examples = few_shot.get_filtered_posts(length, language, tag)

    if len(examples) > 0:
        prompt += "5) Use the writing style as per the following examples."

    for i, post in enumerate(examples):
        post_text = post['text']
        prompt += f'\n\n Example {i+1}: \n\n {post_text}'

        if i == 1:  # Use max two samples
            break

    return prompt

if __name__ == "__main__":
    post = generate_post("Short", "English", "Job Search", "Professional")
    print(post)

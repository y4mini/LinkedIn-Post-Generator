
import json
import pandas as pd


class FewShotPosts:
    def __init__(self, file_path="data/processed_posts.json"):
        self.df = None  # Load posts into dataframe
        self.unique_tags = None  # Tags shown in dropdown
        self.load_posts(file_path)

    def load_posts(self, file_path):
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)
            self.df = pd.json_normalize(posts)
            self.df["length"] = self.df["line_count"].apply(self.categorize_length)
            all_tags = self.df['tags'].apply(lambda x: x).sum()
            self.unique_tags = set(list(all_tags))

    def get_tags(self):
        return self.unique_tags

    def generate_hashtags(self, tags):
        """Generate hashtags based on the selected tags."""
        hashtags = [f"#{tag.replace(' ', '').replace('-', '').capitalize()}" for tag in tags]
        return " ".join(hashtags)

    def get_filtered_posts(self, length, language, tag):
        df_filtered = self.df[
            (self.df['language'] == language) &
            (self.df['length'] == length) &
            (self.df['tags'].apply(lambda tags: tag in tags))
            ]
        return df_filtered.to_dict(orient="records")

    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"


if __name__ == "__main__":
    fs = FewShotPosts()
    posts = fs.get_filtered_posts("Medium", "English", "Job Search")
    print(posts)

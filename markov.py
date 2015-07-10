import random

class SimpleMarkovGenerator(object):

    def read_files(self, filenames):
        """Given a list of files, make chains from them."""

        for source_file in filenames:
            source_file = open(source_file)
            joined = source_file.read()
            split_source = joined.split()
        self.text = split_source
        return

    def make_chains(self):
        """Takes input text as string; stores chains."""
        corpus = self.text
        word_bank = {}
        for i in range(len(corpus)-2):
            key = (corpus[i], corpus[i+1])
            idv_value = corpus[i+2]
            # if key is not already there, make it (it has no value rn)
            if key not in word_bank.keys():
                word_bank[key] = []
            # stick the value in there
            word_bank[key].append(idv_value)
        self.chains = word_bank
        return

    def make_text(self, text_length):
        """Takes dictionary of markov chains; returns random text."""

        corpus = self.chains
        chosen_key = random.choice(corpus.keys())
        while chosen_key[0].istitle() == False:
            chosen_key = random.choice(corpus.keys())
        our_string = " ".join(chosen_key)
        character_count = 0
        while character_count < text_length:
            for value in corpus[chosen_key]:
                value = random.choice(corpus[chosen_key])
                our_string = our_string + " " + (value)
                split_string = our_string.split(" ")
                chosen_key = (split_string[-2], split_string[-1])
                character_count = len(our_string)
        while len(our_string) > text_length:
            split_string = our_string.split(" ")
            split_string.pop()
            our_string = " ".join(split_string)
        self.tweet = our_string
        return self.tweet

class TweetableMarkovGenerator(SimpleMarkovGenerator):
    def make_text(self):
        return super(TweetableMarkovGenerator, self).make_text(140)

if __name__ == "__main__":
    get_tweet = TweetableMarkovGenerator()
    get_tweet.read_files(["bb-sb.txt"])
    get_tweet.make_chains()
    print get_tweet.make_text() + "..."
    print len(get_tweet.make_text())